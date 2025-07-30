# Network Intrusion Datasets Survey

This is an official repository of the "_Network Intrusion Datasets: A Survey, Limitations, and Recommendations_" paper published at [Computers & Security](https://www.sciencedirect.com/journal/computers-and-security) in September 2025. This repository provides Jupyter notebooks and auxilliary scripts to promote Open Science, facilitate the analysis of other datasets or provide a quick reference of the datasets' structures.

**Authors:**

- Patrik Goldschmidt (<igoldschmidt@fit.vut.cz> / <patrik.goldschmidt@kinit.sk>)
- Daniela Chudá (<daniela.chuda@kinit.sk>)

**Paper (published version):**

- [https://www.sciencedirect.com/science/article/pii/S0167404825001993](https://www.sciencedirect.com/science/article/pii/S0167404825001993)

**Paper (accepted version preprint):**

- [https://arxiv.org/abs/2502.06688](https://arxiv.org/abs/2502.06688)

If you prefer numerical citations instead of the parenthetical style used in the accepted and camera-ready versions, please refer to the second version of our preprint [https://arxiv.org/abs/2502.06688v2](https://arxiv.org/abs/2502.06688v2). Its contents are nearly identical to the final version, with only minor rewording of a few paragraphs to accommodate the line width required by the new (longer) citation format.

## Abstract

Data-driven cyberthreat detection has become a crucial defense technique in modern cybersecurity. Network defense, supported by Network Intrusion Detection Systems (NIDSs), has also increasingly adopted data-driven approaches, leading to greater reliance on data. Despite the importance of data, its scarcity has long been recognized as a major obstacle in NIDS research. In response, the community has published many new datasets recently. However, many of them remain largely unknown and unanalyzed, leaving researchers uncertain about their suitability for specific use cases.

In this paper, we aim to address this knowledge gap by performing a systematic literature review (SLR) of 89 public datasets for NIDS research. Each dataset is comparatively analyzed across 13 key properties, and its potential applications are outlined. Beyond the review, we also discuss domain-specific challenges and common data limitations to facilitate a critical view on data quality. To aid in data selection, we conduct a dataset popularity analysis in contemporary state-of-the-art NIDS research. Furthermore, the paper presents best practices for dataset selection, generation, and usage. By providing a comprehensive overview of the domain and its data, this work aims to guide future research toward improving data quality and the robustness of NIDS solutions.

## Repository Structure

```bash
.
├── ntbks_analysis/         # Notebooks with datasets analyses
│   ├── other/              # Notebooks of datasets not included in the survey
│   ├── README.md           # Links notebooks to their corresponding datasets
│   └── ...
├── ntbks_support/          # Notebooks with supportive code
│   ├── plot_popul.ipynb    # Dataset popularity plot
│   └── plot_publ.ipynb     # Dataset publications by-year plot
├── scripts_analysis/       # Scripts for data analyses
│   ├── coundur.sh          # Measure the overall duration of PCAP data
│   ├── countflows.sh       # Count the number of entries (flows)
│   ├── countpkts.sh        # Count the number of packets in PCAP data
│   ├── countsize.sh        # Measure the size of PCAP files in bytes
│   ├── measure_dur_pcap.py # Measure duration and continuity of pcap dataset
│   └── measure_dur_pd.py   # Measure duration and continuity of pandas dataset
├── scripts_support/        # Scripts for data manipulation
│   ├── cloudstor_down.py   # Download data from the Cloudstor service
│   ├── extract_gure.py     # Prepare GureKDDCup dataset for processing
│   └── fixpkts.sh          # Fix folder with broken PCAP files
├── trends_analysis/        # XLSX (Excel) files with analysis of NIDS trends
│   ├── popularity.xlsx     # Data popularity on SOTA NIDS papers
│   └── trends.xlsx         # List of datasets and their trends analysis
├── additional_datasets.md  # List of additional datasets discovered after 2023
├── excluded_datasets.md    # List of excluded datasets from the survey
├── LICENSE                 # License file
└── README.md               # This file
```

## Excluded Datasets

As mentioned in our paper, we focused purely on publicly available datasets suitable for Network Intrusion Detection (NID) research and development. All datasets not available at the time of writing the paper (2024), along with datasets designed for other IDS types (e.g., host-based IDS, Industry Control Systems IDS) without network features, were excluded from the paper. However, we understand that other datasets, or even unavailable ones, might interest others with different goals. Therefore, we list all the excluded datasets (without their detailed analysis) along with the reason for their exclusion in the `excluded_datasets.md` file.

## Additional Datasets

Although our published survey is a static paper, our research on NID data continues. While the survey (and the accompanying `excluded_datasets.md`) includes datasets published up to 2023 (included), we also maintain a separate list `additional_datasets.md`, including datasets published after the scope of the study (2024+) discovered during continued research. However, note that these entries are not thoroughly analyzed, so an associated notebook in the `ntbks_analysis/other/` might thus not be available. Furthermore, this list was compiled in a non-systematic manner, so it should not be considered a comprehensive, up-to-date resource of all NID datasets. It rather serves as a supplementary resource for readers interested in further independent exploration. Also, feel free to contribute to this list via a pull request.

## Miscellaneous

### Similar Projects

Although several papers focused on NIDS datasets have been released (more in our paper), we would like to endorse the [COMIDDS project](https://fkie-cad.github.io/COMIDDS/). This project is similar to our work, as its authors aim to review Intrusion Detection Datasets (both host and network) and continually update the database with new datasets. The project is beneficial for folks searching for a suitable dataset, as the properties of each dataset are summarized within a table along with its brief description and a snippet of the original data format. All datasets are further listed in a comparison table. Although its scope is, for now, smaller than our study, continual updates of the project have the potential to provide a more comprehensive view of the IDS datasets within a short time.

Initially, our project was inspired by [Ring et al.'s 2019 paper](https://www.sciencedirect.com/science/article/pii/S016740481930118X), which comparatively studied various NIDS datasets available until 2018. Nevertheless, many new datasets have been released since, and newer works (e.g., [Yang et al. 2022 paper](https://www.sciencedirect.com/science/article/pii/S0167404822000736)) did not cover them in sufficient detail, so we decided to perform a systematic study on all publicly available datasets until 2023 on our own.

A recent survey by [Pinto et al.](https://www.sciencedirect.com/science/article/pii/S1389128625001458), published a few months prior to our study, also reviews datasets for intrusion detection. Despite some overlap with our study--particularly, in their Section IV discussing the evolution and classification of NID datasets--the two studies are largely complementary. Our work places a strong emphasis on data quality, with detailed discussions of specific dataset properties, common issues, and the best practices for data handling. In contrast, Pinto et al. focus on tools for data collection and traffic analysis, an area only briefly mentioned but left largely unaddressed in our study. For this reason, we believe readers would benefit from both contributions.

### Licence

The code in this repository is published under the **BSD licence**. See the `LICENCE.txt` file for more information.

### Referencing

If you use our code or mention our article, please cite us using the following format:

#### Plaintext (APA)

P. Goldschmidt and D. Chudá. _Network Intrusion Datasets: A Survey, Limitations, and Recommendations_. (2025). Computers & Security. Volume 156. 104510. ISSN 0167-4048. [https://doi.org/10.1016/j.cose.2025.104510](https://doi.org/10.1016/j.cose.2025.104510)

#### BibTeX

```bibtex
@article{goldschmidt2025_nid_data_survey,
  title = {Network intrusion datasets: A survey, limitations, and recommendations},
  author = {Patrik Goldschmidt and Daniela Chud\'a},
  journal = {Computers \& Security},
  volume = {156},
  pages = {104510},
  year = {2025},
  issn = {0167-4048},
  doi = {10.1016/j.cose.2025.104510},
  url = {https://www.sciencedirect.com/science/article/pii/S0167404825001993}
}
```
