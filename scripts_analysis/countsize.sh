#!/bin/bash

# Usage: Measure the total size (in bytes) of PCAP files in a folder recursively
# Modify line 6 for other file extensions

FILES=`find $1 -name "*.pcap*"`
FILES_CNT=0
BYTES_TOTAL=0

for PCAP_FILE in $FILES
do
    FILE_BYTES=`du -sb $PCAP_FILE | cut -f 1 -d$'\t'`
    BYTES_TOTAL=$((FILE_BYTES + BYTES_TOTAL))
    FILES_CNT=$((FILES_CNT+1))
done

echo TOTAL FILES: $FILES_CNT
echo TOTAL BYTES: $BYTES_TOTAL
