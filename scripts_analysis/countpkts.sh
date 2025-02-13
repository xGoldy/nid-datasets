#!/bin/bash

# Usage: Count the total number of packets in the folder recursively
# Modify line 11 for other file extensions
# Author: Patrik Goldschmidt (igoldschmidt@fit.vut.cz)

shopt -s globstar

FILES_CNT=0
PKTS_TOTAL=0

for PCAP_FILE in $1/**/*.pcap*
do
    echo "Processing $PCAP_FILE"
    FILE_PKTCNT=`capinfos -M -c "$PCAP_FILE" 2> /dev/null | tail -n 1 | cut -f 6 -d ' '`
    PKTS_TOTAL=$((FILE_PKTCNT + PKTS_TOTAL))
    FILES_CNT=$((FILES_CNT + 1))
done

echo ""
echo TOTAL FILES  : $FILES_CNT
echo TOTAL PACKETS: $PKTS_TOTAL
