# Datasets Analyses Notebooks

This folder contains Jupyter Notebooks for analyzing datasets and extracting information for the survey's paper comparative table. Their primary purpose is to provide an overview of the data without downloading. However, they have a few limitations, as described below.

## Datasets and Associated Notebooks

This table contains the name of the dataset (1st column) and its associated Jupyter Notebook filename (2nd column). If an associated notebook for a given dataset does not exist, the value `-` is provided. The notebooks are sorted by their data collection year and then alphabetically - same as in the survey paper.

_Work-in-progress: We are currently polishing/commenting available notebooks and will be pushing them in this folder between 2025-02-17 and 2025-02-21._

| #   | **Dataset**                    | **Notebook filename**            |
| --- | ------------------------------ | -------------------------------- |
| 1   | DARPA 1998                     | - |
| 2   | GureKDDcup                     | `1998-gurekddcup.ipynb` |
| 3   | KDD'99                         | `1998-kdd99.ipynb` |
| 4   | NSL-KDD                        | `1998-nslkdd.ipynb` |
| 5   | DARPA 1999                     | - |
| 6   | LLDOS                          | - |
| 7   | MAWILab                        | - |
| 8   | CAIDA DDoS Attack 2007         | - |
| 9   | Twente                         | - |
| 10  | ASNM-CDX                       | `2009--2018-asnm_all.ipynb` |
| 11  | CDX                            | - |
| 12  | ISOT Botnet                    | - |
| 13  | ISCX-IDS-2012                  | `2010-iscx_ids_2012.ipynb` |
| 14  | HogZilla                       | - |
| 15  | CTU-13                         | - |
| 16  | Booters                        | - |
| 17  | Botnet                         | - |
| 18  | SSHCure                        | - |
| 19  | ASNM-TUN                       | `2009--2018-asnm_all.ipynb` |
| 20  | AWID2                          | - |
| 21  | Kyoto 2006+                    | `2006--2015-kyoto2006.ipynb` |
| 22  | UNSW-NB15                      | `2015-unsw_nb15.ipynb` |
| 23  | DDoS 2016                      | `2016-ddos2016.ipynb` |
| 24  | Kent 2016                      | Sample analysis will be added |
| 25  | NDSec-1                        | - |
| 26  | NGIDS-DS                       | `2016-ngids-ds.ipynb` |
| 27  | UGR'16                         | - |
| 28  | Unified Host and Network       | - |
| 29  | 2017-SUEE8                     | - |
| 30  | CIC-IDS2017                    | - |
| 31  | CIDDS-001                      | - |
| 32  | CIDDS-002                      | - |
| 33  | Imp. CIC-IDS2017               | - |
| 34  | ISOT HTTP Botnet               | - |
| 35  | IoT host-based ID dataset      | - |
| 36  | LYCOS-IDS2017                  | - |
| 37  | TrabID                         | - |
| 38  | ISOT-CID                       | - |
| 39  | Kitsune Network Attack Dataset | - |
| 40  | NetML                          | - |
| 41  | NF-UQ-NIDS/ NF-UQ-NIDS-v2      | - |
| 42  | ASNM-NPBO                      | - |
| 43  | Bot-IoT                        | - |
| 44  | CSE-CIC-IDS2018                | - |
| 45  | Imp. CSE-CIC -IDS2018          | - |
| 46  | N-BaIoT                        | - |
| 47  | IoT-23                         | - |
| 48  | CIC-DDoS2019                   | - |
| 49  | CUPID                          | - |
| 50  | GTCS                           | - |
| 51  | IoT network intrusion          | - |
| 52  | IoTID20                        | - |
| 53  | TON_IoT                        | - |
| 54  | MedBIoT                        | - |
| 55  | WUSTL-IIoT-2021                | - |
| 56  | LITNET-2020                    | - |
| 57  | X-IIoTID                       | - |
| 58  | BOUN DDoS                      | - |
| 59  | DAPT 2020                      | - |
| 60  | InSDN                          | - |
| 61  | OPC UA                         | - |
| 62  | SDN Dataset                    | - |
| 63  | SR-BH 2020                     | - |
| 64  | VOIP Enterprise -- Attack      | - |
| 65  | UKM-IDS20                      | - |
| 66  | AWID3                          | - |
| 67  | CCD-INID-V1                    | - |
| 68  | CyberFORCE Scenario            | - |
| 69  | Edge-IIoTset                   | - |
| 70  | HIKARI-2021                    | - |
| 71  | I-Sec                          | - |
| 72  | PWNJUTSU                       | - |
| 73  | Unraveled                      | - |
| 74  | USB-IDS-1                      | - |
| 75  | CIC IoT dataset 2022           | - |
| 76  | LUFlow                         | - |
| 77  | VHS-22                         | - |
| 78  | UWF-Zeek Data22                | - |
| 79  | AIT Log Dataset 2.0            | - |
| 80  | ICS-Flow                       | - |
| 81  | OD-IDS2022                     | - |
| 82  | Simargl2022                    | - |
| 83  | UNR-IDD                        | - |
| 84  | CICIoT2023                     | - |
| 85  | TII-SSRC-23                    | - |
| 86  | Appraise H2020                 | - |
| 87  | FLNET2023                      | - |
| 88  | ROSIDS23                       | - |
| 89  | Westermo                       | - |

## Notebooks Limitations

Initially, these notebooks for data analysis were not purposed to be publicly shared. However, we later realized their potential value for the community. We thus shared the notebooks in the end, but unfortunately, this sharing mindset was adopted rather late in the reviewing process. While not directly affecting the comparative table itself, it brings two major implications for the notebooks:

* **No standard structure is followed**: Initially, our notebooks were mainly goal-driven - focusing on extracting key dataset details (most notably duration, number of classes, and data size) rather than analyzing the data. Later as we decided to share the data, additional data analysis steps were introduced. However, as each dataset is unique, different analysis steps were required. These facts lead to structural discrepancies among the notebooks.

* **Notebooks are not present for every dataset**: Since the analysis was initially not intended for sharing, some datasets, especially those with only raw PCAP data, were analyzed only via the command line and scripts without saved output. As a result, not all datasets have an associated Jupyter notebook.
