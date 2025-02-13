# Given a link, download data from CloudStorage
# Author: Patrik Goldschmidt (igoldschmidt@fit.vut.cz)

import os
import sys
import requests
from bs4 import BeautifulSoup
from urllib.parse import urlparse, urljoin


def download_file(url, save_path):
    response = requests.get(url, stream=True)
    with open(save_path, 'wb') as file:
        for chunk in response.iter_content(chunk_size=8192):
            if chunk:
                file.write(chunk)

def download_cloudstor(link, download_dir):
    # Make a GET request to the CloudStor link
    response = requests.get(link)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        # Find all links on the page
        links = soup.find_all('a', href=True)

        for link in links:
            href = link['href']
            # Check if it's a file or a directory
            if not href.startswith('/') and not href.startswith('?'):
                file_url = urljoin(link.get('base'), href)
                file_name = os.path.basename(urlparse(file_url).path)
                file_save_path = os.path.join(download_dir, file_name)
                download_file(file_url, file_save_path)
                print(f"Downloaded: {file_url}")
    else:
        print(f"Failed to access the CloudStor link. Status code: {response.status_code}")


if __name__ == "__main__":
    cloudstor_link = sys.argv[1]
    download_directory = './down'

    if not os.path.exists(download_directory):
        os.makedirs(download_directory)

    download_cloudstor(cloudstor_link, download_directory)

