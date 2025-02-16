# Datasets Analyses Notebooks

This folder contains Jupyter Notebooks for analyzing datasets and extracting information for the survey's paper comparative table. Their primary purpose is to provide an overview of the data without downloading. However, they have a few limitations, as described below.

## Datasets and Associated Notebooks

This table contains the name of the dataset (1st column) and its associated Jupyter Notebook filename (2nd column). If an associated notebook for a given dataset does not exist, the value `-` is provided.

_Work-in-progress: We are currently polishing/commenting available notebooks and will pushing them in this folder between 2025-02-17 and 2025-02-21._

| **Dataset**                    | **Notebook filename**            |
| ------------------------------ | -------------------------------- |
| DARPA 1998                     | - |
| GureKDDcup                     | - |
| KDD'99                         | - |
| NSL-KDD                        | - |
| DARPA 1999                     | - |
| LLDOS                          | - |
| MAWILab                        | - |
| CAIDA DDoS Attack 2007         | - |
| Twente                         | - |
| ASNM-CDX                       | - |
| CDX                            | - |
| ISOT Botnet                    | - |
| CTU-13                         | - |
| HogZilla                       | - |
| ISCX-IDS-2012                  | - |
| Booters                        | - |
| Botnet                         | - |
| SSHCure                        | - |
| ASNM-TUN                       | - |
| AWID2                          | - |
| Kyoto 2006+                    | - |
| UNSW-NB15                      | - |
| DDoS 2016                      | - |
| Kent 2016                      | - |
| NDSec-1                        | - |
| NGIDS-DS                       | - |
| UGR'16                         | - |
| Unified Host and Network       | - |
| 2017-SUEE8                     | - |
| CIC-IDS2017                    | - |
| CIDDS-001                      | - |
| CIDDS-002                      | - |
| Imp. CIC-IDS2017               | - |
| ISOT HTTP Botnet               | - |
| IoT host-based ID dataset      | - |
| LYCOS-IDS2017                  | - |
| TrabID                         | - |
| ISOT-CID                       | - |
| Kitsune Network Attack Dataset | - |
| NetML                          | - |
| NF-UQ-NIDS/ NF-UQ-NIDS-v2      | - |
| ASNM-NPBO                      | - |
| Bot-IoT                        | - |
| CSE-CIC-IDS2018                | - |
| Imp. CSE-CIC -IDS2018          | - |
| N-BaIoT                        | - |
| IoT-23                         | - |
| CIC-DDoS2019                   | - |
| CUPID                          | - |
| GTCS                           | - |
| IoT network intrusion          | - |
| IoTID20                        | - |
| TON_IoT                        | - |
| MedBIoT                        | - |
| WUSTL-IIoT-2021                | - |
| LITNET-2020                    | - |
| X-IIoTID                       | - |
| BOUN DDoS                      | - |
| DAPT 2020                      | - |
| InSDN                          | - |
| OPC UA                         | - |
| SDN Dataset                    | - |
| SR-BH 2020                     | - |
| VOIP Enterprise -- Attack      | - |
| UKM-IDS20                      | - |
| AWID3                          | - |
| CCD-INID-V1                    | - |
| CyberFORCE Scenario            | - |
| Edge-IIoTset                   | - |
| HIKARI-2021                    | - |
| I-Sec                          | - |
| PWNJUTSU                       | - |
| Unraveled                      | - |
| USB-IDS-1                      | - |
| CIC IoT dataset 2022           | - |
| LUFlow                         | - |
| VHS-22                         | - |
| UWF-Zeek Data22                | - |
| AIT Log Dataset 2.0            | - |
| ICS-Flow                       | - |
| OD-IDS2022                     | - |
| Simargl2022                    | - |
| UNR-IDD                        | - |
| CICIoT2023                     | - |
| TII-SSRC-23                    | - |
| Appraise H2020                 | - |
| FLNET2023                      | - |
| ROSIDS23                       | - |
| Westermo                       | - |

## Notebooks Limitations

Initially, these notebooks for data analysis were not purposed to be publicly shared. However, we later realized their potential value for the community. We thus shared the notebooks in the end, but unfortunately, this sharing mindset was adopted rather late in the reviewing process. While not directly affecting the comparative table itself, it brings two major implications for the notebooks:

* **No standard structure is followed**: Initially, our notebooks were mainly goal-driven - focusing on extracting key dataset details (most notably duration, number of classes, and data size) rather than analyzing the data. Later as we decided to share the data, additional data analysis steps were introduced. However, as each dataset is unique, different analysis steps were required. These facts lead to structural discrepancies among the notebooks.

* **Notebooks are not present for every dataset**: Since the analysis was initially not intended for sharing, some datasets, especially those with only raw PCAP data, were analyzed only via the command line and scripts without saved output. As a result, not all datasets have an associated Jupyter notebook.
