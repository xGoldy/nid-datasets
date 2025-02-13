# List of Excluded Datasets

This document presents datasets that were excluded from the survey. Exclusion primarily happens due to two reasons: a) data being out-of-scope and b) data unavailability. This following two sections will present these datasets and provide links to their paper and dataset (if exist).

## Out-of-Scope Datasets

| **Dataset name**    | **Year** | **Paper** | **Data** | **Format** | **Labels** | **Description / Commentary** |
| ------------------- | -------- | --------- | -------- | ---------- | ---------- | -------------- |
| FIFA World Cup 1998 | 1998 | - | [Data](https://ita.ee.lbl.gov/html/contrib/WorldCup.html) | logs | no | Connections on FIFA servers during 1998, Not relevant for cybersecurity. |
| CIDD | 1999 | [Paper](https://ieeexplore.ieee.org/document/6209206) | [Data](http://groups.di.unipi.it/~hkholidy/projects/cidd/index.html) | logs | indirect | Cloud-based ID logs based on DARPA1999. Full dataset is unavailable. |
| Witty Worm | 2004 | - | [Data](https://catalog.caida.org/dataset/telescope_witty_worm) | packet | no | Capture of a specific worm behavior on a USCD Network Telescope Network. |
| LBNL | 2005 | [Paper](https://www.usenix.org/legacy/event/imc05/tech/full_papers/pang/pang_html/) | [Data](https://www.icir.org/enterprise-tracing/) | packet | no | General data capture containing mostly normal behavior. |
| Moore 2005 | 2005 | [Docs](https://qmro.qmul.ac.uk/xmlui/bitstream/handle/123456789/5050/RR-05-13.pdf) | [Data](https://www.cl.cam.ac.uk/research/srg/netos/projects/archive/nprobe/) | other | no | Purposed for traffic classification. |
| UNIBS-2009 | 2009 | [Paper](http://ccr.sigcomm.org/online/files/p13-v39n5b4-salgarelliA.pdf) | [Data](http://netweb.ing.unibs.it/~ntw/tools/traces/) | packet | yes | Focus on traffic classification. |
| UNIBS-2009 SSH tunnel | 2009 | [Paper](https://ieeexplore.ieee.org/document/5199557) | [Data](http://netweb.ing.unibs.it/~ntw/tools/traces/) | packet | yes | Focus on SSH tunel detection. |
| ICML-09 | 2009 | [Paper](https://cseweb.ucsd.edu/~jtma/papers/url-icml2009.pdf) | [Data](https://www.sysnet.ucsd.edu/projects/url/) | text | yes | Focus on malicious URLs analysis. |
| CSIC HTTP 2010 | 2010 | - | [Data](https://petescully.co.uk/research/csic-2010-http-dataset-in-csv-format-for-weka-analysis/) | text | yes | Focus on HTTP/1.1 malicious requests detection. |
| ADFA | 2013 | [Paper](https://ieeexplore.ieee.org/abstract/document/6555301) | [Data](https://research.unsw.edu.au/projects/adfa-ids-datasets) | logs | yes | Focus on host IDS via system calls. |
| ICS Cyber Attack Dataset | 2014, 2015 | [Paper](https://ieeexplore.ieee.org/abstract/document/7063234) | [Data](https://sites.google.com/a/uah.edu/tommy-morris-uah/ics-data-sets) | other | yes | Focus on ICS IDS. |
| WSN-DS | 2015 | [Paper](https://onlinelibrary.wiley.com/doi/10.1155/2016/4731953) | [Data](https://www.kaggle.com/datasets/bassamkasasbeh1/wsnds) | other | yes | Focus Wireless sensor networks IDS. |


| BATADAL | 2013, 2016, 2017, | [Paper](https://ascelibrary.org/doi/abs/10.1061/(ASCE)WR.1943-5452.0000969) | [Data](http://www.batadal.net/data.html) | other | yes | Focus on ICS anomaly detection. |
| SWaT | 2015 - 2020 | [Paper](https://link.springer.com/chapter/10.1007/978-3-319-71368-7_8) | [Data](https://itrust.sutd.edu.sg/itrust-labs_datasets/dataset_info/) | other | yes | Focus on ICS anomaly detection. |


## Unavailable Datasets

| **Dataset name**    | **Year** | **Paper** | **Data** | **Format** | **Labels** | **Description / Commentary** |
| ------------------- | -------- | --------- | -------- | ---------- | ---------- | -------------- |
| PU-IDS | 1998 | [Paper](https://univagora.ro/jour/index.php/ijccc/article/view/1924) | - | nethost | yes | Synthetic dataset based on NSL-KDD. |
| DEFCON | 2000 | - | [Data](https://defcon.org/html/links/dc-ctf.html) | packet | no | Captures from DEFCON CTF. Unavailable nowadays. |
| UCLA DDoS Dataset  | 2001 | [Paper](http://www.ijcseonline.isroset.org/pub_paper/7-IJCSE-01229.pdf) | - | packet | yes | - |
| CCRC 2006 | 2001 | [Paper](https://ieeexplore.ieee.org/abstract/document/4041181) | - | packet | yes | - |
| Suthaharan et al. 2010 | 2010 | [Paper](https://ieeexplore.ieee.org/abstract/document/5706782) | - | packet | yes | Anomaly detection for wireless sensor networks. |
| SSENet-2011  | 2011 | [Paper](https://ieeexplore.ieee.org/document/6113948) | - | packet (txt) | yes | - |
| VAST Challenge 2011   | 2011 | - | [Data](https://visualdata.wustl.edu/varepository/benchmarks.php) | logs | indirect | Focus on log analysis for scans, DoS, persistence, and social engineering events. |
| VAST Challenge 2012 | 2012 | [Paper](https://ieeexplore.ieee.org/document/6400529) | [Data](https://visualdata.wustl.edu/varepository/benchmarks.php) | logs | indirect | - |
| SANTA  | 2014 | [Paper](https://ieeexplore.ieee.org/document/7033608) | - | other | yes | - |
| SSENet-2014  | 2014 | [Paper](https://ieeexplore.ieee.org/document/7208978) | - | other | yes | - |
| IRSC | 2015 | [Paper](https://aaai.org/papers/252-flairs-2015-10368/) | - | packet, flow | yes |  |
| ISTS-12 | 2015 | - | [Data](https://www.netresec.com/?page=ISTS) | packet | no | Student cybersecurity competition capture. |
| TUIDS | 2015 | [Paper](https://link.springer.com/chapter/10.1007/978-3-642-32129-0_34) | - | packet, flow | yes | - |
| Heritrix | 2016 | [Paper](https://onlinelibrary.wiley.com/doi/abs/10.1002/sec.1441) | - | text | yes | Dataset with malicious and legitimate JavaScript websites. |
| MILCOM-2016 | 2016 | [Paper](https://ieeexplore.ieee.org/abstract/document/7795383) | [Data](https://cybervan.peratonlabs.com:9000/milcom-2016-data-sets) | packet | n.s. | Botnet activity simulation. |
