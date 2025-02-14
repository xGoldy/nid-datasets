# List of Excluded Datasets

This document presents datasets excluded from the main survey. Exclusion primarily happens for two reasons: a) data being out of scope and b) data unavailability. The following sections present these datasets and provide links to their respective papers and data (if exist).

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

## Out-of-Scope Datasets

| **Dataset**    | **Year** | **Paper** | **Data** | **Format** | **Labels** | **Description / Commentary** |
| ------------------- | -------- | --------- | -------- | ---------- | ---------- | -------------- |
| FIFA World Cup 1998 | 1998 | - | [Data](https://ita.ee.lbl.gov/html/contrib/WorldCup.html) | logs | no | Connections on FIFA servers during 1998. Irrelevant for cybersecurity. |
| CIDD | 1999 | [Paper](https://ieeexplore.ieee.org/document/6209206) | [Data](http://groups.di.unipi.it/~hkholidy/projects/cidd/index.html) | logs | indir. | Cloud-based ID logs based on DARPA1999. Full data unavailable. |
| Witty Worm | 2004 | - | [Data](https://catalog.caida.org/dataset/telescope_witty_worm) | packet | no | Witty worm behavior on a USCD Network Telescope Network. |
| LBNL | 2005 | [Paper](https://www.usenix.org/legacy/event/imc05/tech/full_papers/pang/pang_html/) | [Data](https://www.icir.org/enterprise-tracing/) | packet | no | General data containing mostly normal behavior. |
| Moore 2005 | 2005 | [Docs](https://qmro.qmul.ac.uk/xmlui/bitstream/handle/123456789/5050/RR-05-13.pdf) | [Data](https://www.cl.cam.ac.uk/research/srg/netos/projects/archive/nprobe/) | other | no | Traffic classification. |
| UNIBS-2009 | 2009 | [Paper](http://ccr.sigcomm.org/online/files/p13-v39n5b4-salgarelliA.pdf) | [Data](http://netweb.ing.unibs.it/~ntw/tools/traces/) | packet | yes | Traffic classification. |
| UNIBS-2009 SSH tunnel | 2009 | [Paper](https://ieeexplore.ieee.org/document/5199557) | [Data](http://netweb.ing.unibs.it/~ntw/tools/traces/) | packet | yes | SSH tunel detection. |
| ICML-09 | 2009 | [Paper](https://cseweb.ucsd.edu/~jtma/papers/url-icml2009.pdf) | [Data](https://www.sysnet.ucsd.edu/projects/url/) | text | yes | Malicious URLs. |
| CSIC HTTP 2010 | 2010 | - | [Data](https://petescully.co.uk/research/csic-2010-http-dataset-in-csv-format-for-weka-analysis/) | text | yes | HTTP/1.1 malicious requests. |
| ADFA | 2013 | [Paper](https://ieeexplore.ieee.org/abstract/document/6555301) | [Data](https://research.unsw.edu.au/projects/adfa-ids-datasets) | logs | yes | Host IDS via system calls. |
| ICS Cyber Attack Dataset | 2014, 2015 | [Paper](https://ieeexplore.ieee.org/abstract/document/7063234) | [Data](https://sites.google.com/a/uah.edu/tommy-morris-uah/ics-data-sets) | other | yes | ICS IDS. |
| WSN-DS | 2015 | [Paper](https://onlinelibrary.wiley.com/doi/10.1155/2016/4731953) | [Data](https://www.kaggle.com/datasets/bassamkasasbeh1/wsnds) | other | yes | Wireless sensor networks IDS. |
| Modbus Dataset | 2016 | [Paper](https://www.usenix.org/conference/cset16/workshop-program/presentation/lemay) | [Data](https://github.com/antoine-lemay/Modbus_dataset) | pcap, other | yes | ICS IDS via Modbus. |
| Kharon | 2016 | [Paper](https://www.usenix.org/conference/laser2016/program/presentation/kiss) | [Data](https://cidre.gitlabpages.inria.fr/malware/malware-website/) | other | yes | Android malware detection. |
| BATADAL | 2013, 2016, 2017, | [Paper](https://ascelibrary.org/doi/abs/10.1061/(ASCE)WR.1943-5452.0000969) | [Data](http://www.batadal.net/data.html) | other | yes | ICS anomaly detection. |
| UGRansomware | 2016, 2018 | [Paper](https://www.mdpi.com/2078-2489/12/10/405) | [Data](https://www.researchgate.net/publication/342200905_An_Ensemble_Learning_Framework_for_Anomaly_Detection_in_the_Existing_Network_Intrusion_Detection_Landscape) | other | yes | Merge of UGR'16 and Ransomware data. |
| All Eyes on You | 2018 | [Paper](https://ieeexplore.ieee.org/abstract/document/8584985) | [Data](https://www.kaggle.com/datasets/francoisxa/ds2ostraffictraces) | logs | yes | IDS for IoT microservices via host logs. |
| ISOT Ransomware Detection Dataset | 2018 | - | [Data](https://onlineacademiccommunity.uvic.ca/isot/2022/11/27/botnet-and-ransomware-detection-datasets/) | packet, logs | n.s. | Ransomware detection. Data availability on-request. |
| MUD IoT Attack Dataset | 2018 | [Paper](https://dl.acm.org/doi/abs/10.1145/3314148.3314352) | [Data](https://iotanalytics.unsw.edu.au/attack-data.html) | packet, flows | yes | Volumetric attacks on IoT MUD monitoring. |
| WUSTL-IIoT-2018 | 2018 | [Paper](https://www.mdpi.com/1999-5903/10/8/76) | [Data](https://www.cse.wustl.edu/~jain/iiot/index.html) | packet, other | yes | ICS SCADA IDS. |
| MTA-KDD'19 | 2018 | [Paper](https://ricerca.univaq.it/bitstream/11697/145526/1/ITASEC20.pdf) | [Data](https://github.com/IvanLetteri/MTA-KDD-19/) | flows | yes | Pre-normalized with limited usability. |
| IoT-SH | 2019 | [Paper](https://ieeexplore.ieee.org/abstract/document/8753563) | - | packet | yes | Side-effect data available on-request. |
| DARPA OpTC | 2019 | - | [Data1](https://github.com/FiveDirections/OpTC-data/tree/master) [Data2](https://ieee-dataport.org/open-access/operationally-transparent-cyber-optc) | other, logs | indir. | APT dataset primarily for log correlation and HIDS. |
| Electra| 2019 | [Paper](https://ieeexplore.ieee.org/abstract/document/8926471) | [Data](http://perception.inf.um.es/ICS-datasets/) | other | yes | ICS IDS. |
| SWaT | 2015 - 2020 | [Paper](https://link.springer.com/chapter/10.1007/978-3-319-71368-7_8) | [Data](https://itrust.sutd.edu.sg/itrust-labs_datasets/dataset_info/) | other | yes | ICS anomaly detection. |
| CIRA-CIC-DoHBrw-2020 | 2020 | [Paper](https://ieeexplore.ieee.org/abstract/document/9251211) | [Data](https://ieeexplore.ieee.org/abstract/document/9251211) | packet, flows | yes | DNS over HTTPS detection. |
| DAD | 2020 | [Paper](https://www.mdpi.com/1424-8220/20/13/3745) | [Data](https://github.com/dad-repository/dad) | packet | yes | IoT NIDS via MQTT. |
| Goncalves 2020 | 2020 | [Paper](https://ieeexplore.ieee.org/document/9348149) | [Data](https://github.com/fabio-r-goncalves/dataset-collection) | other | yes | VANET-specific data & format |
| MQTT-IoT-IDS2020 | 2020 | [Paper](https://link.springer.com/chapter/10.1007/978-3-030-64758-2_6) | [Data](https://ieee-dataport.org/open-access/mqtt-iot-ids2020-mqtt-internet-things-intrusion-detection-dataset) | packet, flows | yes | IoT MQTT NIDS. |
| MQTTset | 2020 | [Paper](https://www.mdpi.com/1424-8220/20/22/6578) | [Data](https://www.kaggle.com/datasets/cnrieiit/mqttset/) | packet | yes | IoT MQTT NIDS. |
| WUSTL-EHMS | 2020 | - | [Data](https://www.cse.wustl.edu/~jain/ehms/index.html) | other | yes | Internet of Medical Things (IoMT) attacks. |
| DoS/DDoS-MQTT-IoT | 2021 | [Paper](https://www.sciencedirect.com/science/article/pii/S1389128623002542) | [Data](https://www.kaggle.com/datasets/alaaalatram/dosddos-mqtt-iot) | packet | yes | DoS and DDoS attacks within IoT MQTT. |
| SOCBED Example Dataset | 2021 | [Paper](https://dl.acm.org/doi/10.1145/3485832.3488020) | [Data](https://github.com/fkie-cad/socbed-eval-acsac-2021) | logs | no | Example capture from a replicable environment, no network data. |
| WDT | 2021 | [Paper](https://ieeexplore.ieee.org/abstract/document/9526562) | [Data](https://ieee-dataport.org/open-access/hardware-loop-water-distribution-testbed-wdt-dataset-cyber-physical-security-testing) | other | yes | CPS attacks. |
| 5G-NIDD | 2022 | [Paper](https://arxiv.org/abs/2212.01298) | [Data](https://ieee-dataport.org/documents/5g-nidd-comprehensive-network-intrusion-detection-dataset-generated-over-5g-wireless) | packet, flows | yes | 5G network NID data. |
| DDoS attack Dataset in VANETs | 2022 | [Paper](https://link.springer.com/chapter/10.1007/978-3-031-19211-1_21) | [Data](https://github.com/YangFanAHU/DDoS-attacks-dataset-in-VANETs) | other | yes | DDoS attacks with VANET-specific features. |
| 5GC PFCP IDS | 2023 | [Paper](https://ieeexplore.ieee.org/document/10176693) | [Data](https://zenodo.org/records/7888347) | flows | yes | 5G PFCP DoS attacks, CICFlowMeter features. |
| can-train-and-test | 2023 | [Paper](https://ieeexplore.ieee.org/document/10333756) | [Data](https://bitbucket.org/brooke-lampe/can-train-and-test/src/master/) | other | yes | CAN environment and specific features. |
| CICEV2023 DDoS | 2023 | [Paper](https://www.computer.org/csdl/proceedings-article/pst/2023/10320202/1SjejFg2aKA) | [Data](https://www.unb.ca/cic/datasets/cicev2023.html) | other | yes | Electric vehicles DDoS. |
| WCN Anomaly Dataset | 2023 | [Paper](https://www.sciencedirect.com/science/article/pii/S2352340923004602) | [Data](https://doi.org/10.7910/DVN/NKTFZM) | other | yes | Wireless Community Networks anomalies. |

## Unavailable Datasets

| **Dataset**    | **Year** | **Paper** | **Data** | **Format** | **Labels** | **Description / Commentary** |
| ------------------- | -------- | --------- | -------- | ---------- | ---------- | -------------- |
| PU-IDS | 1998 | [Paper](https://univagora.ro/jour/index.php/ijccc/article/view/1924) | - | nethost | yes | Synthetic dataset based on NSL-KDD. |
| DEFCON | 2000 | - | [Data](https://defcon.org/html/links/dc-ctf.html) | packet | no | DEFCON CTF captures. Nowadays unavailable. |
| UCLA DDoS Dataset  | 2001 | [Paper](http://www.ijcseonline.isroset.org/pub_paper/7-IJCSE-01229.pdf) | - | packet | yes | - |
| CCRC 2006 | 2001 | [Paper](https://ieeexplore.ieee.org/abstract/document/4041181) | - | packet | yes | - |
| Suthaharan et al. 2010 | 2010 | [Paper](https://ieeexplore.ieee.org/abstract/document/5706782) | - | packet | yes | Anomaly detection for wireless sensor networks. |
| SSENet-2011  | 2011 | [Paper](https://ieeexplore.ieee.org/document/6113948) | - | packet | yes | - |
| VAST Challenge 2011   | 2011 | - | [Data](https://visualdata.wustl.edu/varepository/benchmarks.php) | logs | indirect | Log analysis. |
| VAST Challenge 2012 | 2012 | [Paper](https://ieeexplore.ieee.org/document/6400529) | [Data](https://visualdata.wustl.edu/varepository/benchmarks.php) | logs | indirect | - |
| SANTA  | 2014 | [Paper](https://ieeexplore.ieee.org/document/7033608) | - | other | yes | - |
| SSENet-2014  | 2014 | [Paper](https://ieeexplore.ieee.org/document/7208978) | - | other | yes | - |
| IRSC | 2015 | [Paper](https://aaai.org/papers/252-flairs-2015-10368/) | - | packet, flows | yes |  |
| ISTS-12 | 2015 | - | [Data](https://www.netresec.com/?page=ISTS) | packet | no | Cybersecurity competition capture. |
| TUIDS | 2015 | [Paper](https://link.springer.com/chapter/10.1007/978-3-642-32129-0_34) | - | packet, flows | yes | - |
| Heritrix | 2016 | [Paper](https://onlinelibrary.wiley.com/doi/abs/10.1002/sec.1441) | - | text | yes | Malicious and legitimate JavaScript websites. |
| MILCOM-2016 | 2016 | [Paper](https://ieeexplore.ieee.org/abstract/document/7795383) | [Data](https://cybervan.peratonlabs.com:9000/milcom-2016-data-sets) | packet | n.s. | Botnet activity simulation. |
| SNMP-MIB | 2016 | [Paper](https://scholar.google.com/scholar?cluster=6997320114336392313) | - | other | yes | On request, but authors do not respond. |
| BKIDset | 2017 | [Paper](https://ieeexplore.ieee.org/document/9668224) | - | flows | yes | Based on CIC-IDS2017. |
| Brahanyaa 2018 SNMP dataset | 2017 | [Paper](https://ieeexplore.ieee.org/document/8782319) | - | other | yes | - |
| PUF | 2018 | [Paper](https://www.sciencedirect.com/science/article/pii/S1877050918308111) | - | flows | yes | - |
| CYSAS-S3 | 2019 | [Paper](https://dl.acm.org/doi/10.1145/3407023.3409222) [Paper2](https://www.mdpi.com/1424-8220/22/14/5104) | - | flow, other | yes | APT simulation. |
| RPL-NIDS17 | 2019 | [Paper](https://link.springer.com/article/10.1007/s11277-019-06485-w) | - | flows | yes | RPL-based 6LoWPAN data, removed from Zenodo. |
| CoAP-DoS | 2021 | [Paper](https://ieeexplore.ieee.org/document/9845285) | - | other | yes | IoT CoAP DoS attacks. Repository deleted. |
| IoT and IIoT attack dataset | 2021 | [Paper](https://www.mdpi.com/1424-8220/21/4/1528) | - | other | yes | - |
| IoT-RPL | 2021 | [Paper](https://ieeexplore.ieee.org/abstract/document/9615841) | - | other | yes | - |
| TCP FIN Flood and Zbassocflood | 2021 | [Paper](https://jit.ndhu.edu.tw/article/view/2874) | [Data](https://ieee-dataport.org/documents/tcp-fin-flood-and-zbassocflood-dataset) | packet | yes | Behind IEEEDataport Paywall. |
| VDDD | 2021 | [Paper](https://journals.sagepub.com/doi/10.1177/15501477211000287) | - | other | yes | - |
| ZYELL-NCTU NetTraffic-1.0 | 2021 | [Paper](https://ieeexplore.ieee.org/document/9602909) | - | other | yes | - |
| CoAP-IoT Dataset for Anomaly Detection | 2022 | [Paper](https://www.mdpi.com/2076-3417/13/7/4482) | [Data](https://github.com/dad-repository/cidad) | packet | yes | PCAP files removed from the repository. |
| Hybrid IoT/OT Honeypots | 2022 | [Paper](https://dl.acm.org/doi/10.1145/3564625.3564645) | [Data](https://data.dtu.dk/articles/dataset/A_dataset_of_hybrid_IoT_OT_honeypots/21088651) | packet | yes | Data on request, but the e-mail is irresponsive. |
| Koga2022 | 2022 | [Paper](https://ieeexplore.ieee.org/document/10062777) | - | nethost | yes | - |
| LATAM-DDoS-IoT | 2022 | [Paper](https://ieeexplore.ieee.org/abstract/document/9908531) | [Data](https://ieee-dataport.org/documents/latam-ddos-iot-dataset) | packet, flows | yes | Behind IEEEDataport Paywall. |
| SUNBURST2022 | 2022 | [Paper](https://www.techscience.com/csse/v47n2/53670) | - | flows | yes | SUNBURST Solarwinds attack simulation. |
| UAN-12 | ???? - 2022 | [Paper](https://www.mdpi.com/1424-8220/22/5/1847) | [Data](https://securitylab.uan.mx/dataset-uan12.htm) | packet, flows | yes | Download links do not work. |
