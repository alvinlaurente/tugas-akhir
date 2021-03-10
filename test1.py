import os
import pyshark
import xlsxwriter

timespan1 = 0
bits1 = 0
throughput1 = 0
latency_capture1 = 0
latency_display1 = 0
count1 = 0
total1 = 0

bytes = 0
total = 0
count = 0
timestamp1 = 0
timestamp2 = 0
timestamp3 = 0
timestamp4 = 0
timestamp5 = 0
timestamp6 = 0
timestamp7 = 0

cap = pyshark.FileCapture('eoip/10mb/1.pcapng', only_summaries=True)
cap

for pkt in cap:
    src_addr = pkt.source
    dst_addr = pkt.destination
    lengths = pkt.length
    timestamp = pkt.time

    timestamp4 = (float(timestamp) - float(timestamp3))
    timestamp3 = float(timestamp)

    if(src_addr == '10.0.0.114'):
        total += int(lengths)

        if count == 0:
            timestamp1 = float(timestamp)
            timestamp6 = float(timestamp)
        else:
            timestamp2 = float(timestamp)
            timestamp7 += timestamp3 - timestamp6
            timestamp6 = timestamp3

        count += 1
        timestamp5 += float(timestamp4)
        timespan = timestamp2 - timespan1
        bytes = total * 8
        throughput = bytes/timespan
        latency_capture1 = timestamp5 / count
        latency_display1 = timestamp7 / count

print("bytes", bytes)
print("timespan", timespan)
print("count", count)
print("latency_capture1", latency_capture1)
print("latency_display1", latency_display1)
