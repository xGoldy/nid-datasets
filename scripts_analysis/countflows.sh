#!/bin/bash

# Usage: Counts the total number of flows (i.e., CSV entries) in the folder recursively
# Modify '*.csv' for other file extensions
# Author: Patrik Goldschmidt (igoldschmidt@fit.vut.cz)

# Fix for spaces in paths
OIFS="$IFS"
IFS=$'\n'

FILES=`find "$1" -name "*.csv"`
FILES_TOTAL=0
HEADER_SIZE=1
SUM=0

for FLOW_FILE in $FILES
do
    echo "Processing $FLOW_FILE"
    FILE_PKTCNT=`cat "$FLOW_FILE" | wc -l`
    SUM=$((FILE_PKTCNT + SUM - HEADER_SIZE))
    FILES_TOTAL=$((FILES_TOTAL + 1))
done
echo TOTAL FILES: $FILES_TOTAL
echo TOTAL FLOWS: $SUM

IFS="$OIFS"
