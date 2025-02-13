#!/bin/bash

# Fixes PCAP files with packet errors. Requires root directory as input.
# Author: Patrik Goldschmidt (igoldschmidt@fit.vut.cz)

shopt -s globstar

# Set to 1 if the old corrupted file has to be replaced
# If set to 0, a copy named originalFile_fix.pcap will be kept
REPLACE=1

FILES_OK=0
FILES_FIXED=0

for PCAP_FILE in $1/**/*.pcap
do
    FIXED_FNAME="${PCAP_FILE%.*}_fix.${PCAP_FILE##*.}"

    echo "Processing $PCAP_FILE"

    pcapfix -o "$FIXED_FNAME" "$PCAP_FILE"

    # Counting of the corrupted files apparently does not work, as the pcapfix
    # always returns 0 even if the file is corrupted - conflicting its manpage
    if [[ $? -eq 0 ]]
    then
        FILES_OK=$((FILES_OK + 1))
    else
        FILES_FIXED=$((FILES_FIXED + 1))
    fi

    # Replace the file if desired
    if [[ $REPLACE -eq 1 ]] && [ -f $FIXED_FNAME ]
    then
        mv "$FIXED_FNAME" "$PCAP_FILE"
    fi
done

echo ""
echo "FILES OK    : $FILES_OK"
echo "FILES FIXED : $FILES_FIXED"
