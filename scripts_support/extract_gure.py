#!/bin/python

# Extraction script for GureKDDCup dataset. Works for both full and 6percent variants
# Author: Patrik Goldschmidt (igoldschmidt@fit.vut.cz)

import os
import subprocess
import sys


DAY_TO_NUMBER = {
    'Monday': 1,
    'Tuesday': 2,
    'Wednesday': 3,
    'Thursday': 4,
    'Friday': 5
}

FILE_OF_INTEREST = 'gureKddcup-matched.list'


def main(gure_path: str):
    # Extract per-week tar.gz archive
    for root_fname_zipped in os.listdir(gure_path):
        command_extr_root_file = ['tar', '-xf', os.path.join(gure_path, root_fname_zipped), '--directory', gure_path]
        subprocess.run(command_extr_root_file, capture_output=True)

        # Check for non-week files - e.g., ARFF in the 6percent case
        if 'Week' not in root_fname_zipped:
            continue

        # If the file is a week, define it's parameter and continue extraction
        week_name = root_fname_zipped.split('.')[0]
        week_id = int(week_name[-1])
        week_dirpath = os.path.join(gure_path, week_name)

        # Extract contents of the current week
        for day_name_zipped in os.listdir(week_dirpath):
            day_name = day_name_zipped.split('.')[0]
            day_dirpath = os.path.join(week_dirpath, day_name)

            command_extr_days = ['tar', '-xf', os.path.join(week_dirpath, day_name_zipped), '--directory', week_dirpath]
            subprocess.run(command_extr_days, capture_output=True)

            # Extract the contents of each day after extraction
            for day_data_zipped in os.listdir(day_dirpath):
                day_data_path = os.path.join(day_dirpath, day_data_zipped)
                command_extr_item = ['tar', '-xf', day_data_path, '--directory', day_dirpath]

                subprocess.run(command_extr_item, capture_output=True)

            # Rename the non-payload list of connections to have a specific name for future handling
            matched_list_newname = f'{week_id:02d}-{DAY_TO_NUMBER[day_name]:02d}.csv'
            data_filepath = os.path.join(day_dirpath, FILE_OF_INTEREST)

            if os.path.exists(data_filepath):
                os.rename(data_filepath, os.path.join(day_dirpath, matched_list_newname))

    # Remove all .tar.gz files after extraction
    command_remove_tar_gz = ['find', gure_path, '-name', '*.tar.gz', '-delete']
    subprocess.run(command_remove_tar_gz, capture_output=True)


if __name__ == '__main__':
    main(sys.argv[1])
