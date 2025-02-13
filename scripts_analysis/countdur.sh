#!/bin/bash

# Usage: Measures the total duration of PCAP capture files in a folder recursively
# Modify '*.pcap*' on line 10 for other file extensions
# Author: Patrik Goldschmidt (igoldschmidt@fit.vut.cz)

OIFS="$IFS"
IFS=$'\n'

TOTAL_DUR=0
FILES=`find $1 -name '*.pcap*'`

for FILE in $FILES
do
   FILE_DUR=`capinfos -u "$FILE" | tail -n 1 | cut -f 6 -d ' '`
   TOTAL_DUR=`echo "$TOTAL_DUR + $FILE_DUR" | bc`
done

echo $TOTAL_DUR

IFS="$OIFS"
