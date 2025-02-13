# Usage: Measures the duration and continuity of a PCAP, given its path
# Author: Patrik Goldschmidt (igoldschmidt@fit.vut.cz)

from scapy.all import PcapReader


def compute_pcap_true_duration(filepath: str, max_gap_sec: int):
    contiguous = True
    total_dur = 0
    last_time = 0

    for pkt in PcapReader(filepath):
        pkt_time = pkt.time

        # First packet in the file
        if last_time == 0:
            last_time = pkt_time

        # Check if the specified gap has not been reached
        if last_time + max_gap_sec >= pkt_time:
            total_dur += pkt_time - last_time
        elif contiguous:
            contiguous = False

        last_time = pkt_time

    return float(total_dur), contiguous
