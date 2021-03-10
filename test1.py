import pyshark

throughput = 0
average_latency = 0

timespan = 0
bits = 0
kilobits = 0
bytes = 0
total_packets = 0
initial_timestamp = 0
last_timestamp = 0
latency = 0
total_time = 0
total_latency = 0
# delay = 0
total_packet_loss = 0
packet_loss = 0

cap = pyshark.FileCapture('gre/50mb/2.pcapng', only_summaries=True)
cap

filtered_cap = pyshark.FileCapture('gre/50mb/2.pcapng', only_summaries=True, display_filter='tcp.analysis.retransmission')
filtered_cap

for pkt in cap:
    src_addr = pkt.source
    lengths = pkt.length
    current_timestamp = pkt.time

    latency = (float(current_timestamp) - float(last_timestamp))
    last_timestamp = float(current_timestamp)

    if(src_addr == '10.0.0.114'):
        bytes += int(lengths)

        if total_packets == 0:
            initial_timestamp = float(current_timestamp)
        else:
            total_time = float(current_timestamp)

        total_packets += 1
        total_latency += float(latency)
        timespan = total_time
        bits = bytes * 8
        average_latency = total_latency / total_packets

for retransmission in filtered_cap:
    src_addr = retransmission.source

    if(src_addr == '10.0.0.114'):
        total_packet_loss += 1

kilobits = bits / 1000
throughput = kilobits/timespan
packet_loss = (total_packet_loss/total_packets) * 100

print(bits, "bits")
print(bytes, "bytes")
print("timespan", timespan, "s")
print("total_packets", total_packets, "packets")
print("throughput", throughput, "kb/s")
print("average_latency", average_latency, "s")
print("total_packet_loss", total_packet_loss, "packets")
print("packet_loss", packet_loss, "%")

print("")

# print("Last Packet Information")
# print("initial_timestamp", initial_timestamp, "s")
# print("current_timestamp", current_timestamp, "s")
# print("last_timestamp", last_timestamp, "s")
# print("latency", latency, "s")
# print("total_time", total_time, "s")
# print("total_latency", total_latency, "s")
