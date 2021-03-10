import pyshark

throughput = 0
latency_capture = 0
latency_display = 0

timespan = 0
bits = 0
kilobits = 0
bytes = 0
count = 0
initial_timestamp = 0
last_timestamp = 0
interval = 0
total_time = 0
total_interval = 0
total_actual_timestamp = 0

cap = pyshark.FileCapture('ipip/10mb/4.pcapng', only_summaries=True)
# cap

for pkt in cap:
    interval = (float(pkt.time) - float(last_timestamp))
    last_timestamp = float(pkt.time)

    if(pkt.source == '10.0.0.114'):
        bytes += int(pkt.length)

        if count == 0:
            initial_timestamp = float(pkt.time)
        else:
            total_time = float(pkt.time)
            total_actual_timestamp += last_timestamp

        count += 1
        total_interval += float(interval)
        timespan = total_time
        bits = bytes * 8
        latency_capture = total_interval / count
        latency_display = total_actual_timestamp / count
kilobits = bits / 1000
throughput = kilobits/timespan

print(bits, "bits")
print(bytes, "bytes")
print("timespan", timespan, "s")
print("count", count, "packets")
print("throughput", throughput, "kb/s")
print("latency_capture", latency_capture, "s")
print("latency_display", latency_display, "s")
print("")

print("initial_timestamp", initial_timestamp, "s")
print("last_timestamp", last_timestamp, "s")
print("interval", interval, "s")
print("total_time", total_time, "s")
print("total_interval", total_interval, "s")
print("total_actual_timestamp", total_actual_timestamp, "s")
