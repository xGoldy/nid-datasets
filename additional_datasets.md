# List of Additional Datasets

This documents presents datasets discovered after the scope of the published survey (published after 2023). These datasets were discovered in a non-systematic manner, so the following list could not be considered a comprehensive list of all available NID datasets. Nevertheless, as our research on NID data is active even after the survey publication, so we occasionally discovered additional datasets, which we decided to list here.

As these datasets are out of scope, we collect significantly less information about them and leave detailed analyses for interested readers. Detailed descriptions of individual table fields are provided in our paper. However, for a quick reference:

* **Dataset**: The name of the dataset
* **Year**: The year, multiple years, or a year range when the dataset was collected
* **Paper**: Link to the dataset's corresponding paper or other metadata
* **Data**: Link to the dataset's download link
* **Format**: Distribution format of the data. Can be:
  * _packet_ - per-packet data
  * _flows_ - bi-directional or uni-directional NetFlow data
  * _logs_ - textual log data from host systems or network devices, e.g., firewalls
  * _nethost_ - pre-extracted features combining both network and host sources
  * _other_ - other data types not corresponding to any of the above - e.g., binary files, environment-specific values like sensors, etc.
* **Description/Commentary**: Brief description of the data or commentary about its properties

## Additional Datasets

| **Dataset**    | **Year** | **Paper** | **Data** | **Format** | **Labels** | **Description / Commentary** |
| ------------------- | -------- | --------- | -------- | ---------- | ---------- | -------------- |
| AnoShift | 2006-2015 | [Paper](https://proceedings.neurips.cc/paper_files/paper/2022/hash/d3bcbcb2a7b0b4716bf24ce4b2ea8d60-Abstract-Datasets_and_Benchmarks.html) | [Data](https://ita.ee.lbl.gov/html/contrib/WorldCup.html) | other | yes | Kyoto2006+ data for NIDS under data drift. |
| CREMEv2 | 2023 | [Paper](https://www.sciencedirect.com/science/article/abs/pii/S1084804521002137) | [Data](https://www.kaggle.com/datasets/masjohncook/cremev2-datasets) | flows | yes | Product of a dataset collection toolchain CREME. |
| CESNET-TimeSeries24 | 2024 | [Paper](https://www.nature.com/articles/s41597-025-04603-x) | [Data](https://zenodo.org/records/13382427) | flows | no | Large-scale capture from backbone ISP network. |
| USB-IDS-TC | 2024 | [Paper](https://www.scitepress.org/Papers/2025/132486/132486.pdf) | [Data](https://idsdata.ding.unisannio.it/index.html) | flows | yes | DoS attacks for 5 network configurations. |

## Research Side-Effects

| **Dataset**    | **Year** | **Paper** | **Data** | **Format** | **Labels** | **Description / Commentary** |
| ------------------- | -------- | --------- | -------- | ---------- | ---------- | -------------- |
| LycoS-Unicas-IDS2018 | 2018 | [Paper](https://ieeexplore.ieee.org/document/10704637) | [Data](https://github.com/MarcoCantone/LycoS-Unicas-IDS2018) | flows | yes | CSE-CIC-IDS2018 data processed via LycoStand. |

## Repositories

| **Repository Name** | **Link** | **Description** |
| ------------------- | -------- | --------------- |
| - | - | - |
