import pyshark
import xlsxwriter

workbook = xlsxwriter.Workbook('test.xlsx')
scenario = ['eoip', 'gre', 'ipip']
for scenario in scenario:
    worksheet = workbook.add_worksheet(scenario)
    row = 0
    col = 0
    file_size = ['10mb', '20mb', '30mb', '40mb', '50mb']

    for file_size in file_size:
        worksheet.write(row, 0, file_size)
        row += 1
        counter = 0

        worksheet.write(row, 0, 'No')
        worksheet.write(row, 1, 'Bits')
        worksheet.write(row, 2, 'Bytes')
        worksheet.write(row, 3, 'Total Packets')
        worksheet.write(row, 4, 'Timespan (s)')
        worksheet.write(row, 5, 'Throughput (kb/s)')
        worksheet.write(row, 6, 'Average Latency (s)')
        worksheet.write(row, 7, 'Total Packet Lost')
        worksheet.write(row, 8, 'Packet Loss (%)')
        row += 1

        sum_bits = 0
        sum_bytes = 0
        sum_total_packets = 0
        sum_timespan = 0
        sum_throughput = 0
        sum_average_latency = 0
        sum_total_packet_lost = 0

        test_file = ['1.pcapng', '2.pcapng', '3.pcapng', '4.pcapng', '5.pcapng',
                     '6.pcapng', '7.pcapng', '8.pcapng', '9.pcapng', '10.pcapng']

        for test_file in test_file:
            file_path = scenario + '/' + file_size + '/' + test_file

            bits = 0
            kilobits = 0
            bytes = 0
            total_packets = 0
            timespan = 0
            initial_timestamp = 0
            last_timestamp = 0
            latency = 0
            total_time = 0
            total_latency = 0
            total_packet_lost = 0
            throughput = 0
            average_latency = 0
            packet_loss = 0

            cap = pyshark.FileCapture(file_path, only_summaries=True)
            cap

            for packet in cap:
                src_addr = packet.source
                length = packet.length
                current_timestamp = packet.time

                latency = (float(current_timestamp) - float(last_timestamp))
                last_timestamp = float(current_timestamp)

                if(src_addr == '10.0.0.114'):
                    bytes += int(length)

                    if total_packets == 0:
                        initial_timestamp = float(current_timestamp)
                    else:
                        total_time = float(current_timestamp)

                    total_packets += 1
                    total_latency += float(latency)
                    timespan = total_time - initial_timestamp
                    bits = bytes * 8
                    average_latency = total_latency / total_packets

            retransmission_cap = pyshark.FileCapture(
                file_path, only_summaries=True, display_filter='tcp.analysis.retransmission')
            retransmission_cap

            for packet in retransmission_cap:
                src_addr = packet.source

                if(src_addr == '10.0.0.114'):
                    total_packet_lost += 1

            kilobits = bits / 1000
            throughput = kilobits/timespan
            packet_loss = (total_packet_lost/total_packets) * 100
            counter += 1

            worksheet.write(row, 0, counter)
            worksheet.write(row, 1, bits)
            worksheet.write(row, 2, bytes)
            worksheet.write(row, 3, total_packets)
            worksheet.write(row, 4, timespan)
            worksheet.write(row, 5, throughput)
            worksheet.write(row, 6, average_latency)
            worksheet.write(row, 7, total_packet_lost)
            worksheet.write(row, 8, packet_loss)
            row += 1

            sum_bits += bits
            sum_bytes += bytes
            sum_total_packets += total_packets
            sum_timespan += timespan
            sum_throughput += throughput
            sum_average_latency += average_latency
            sum_total_packet_lost += total_packet_lost

        worksheet.write(row, 0, "Average")
        worksheet.write(row, 1, sum_bits / counter)
        worksheet.write(row, 2, sum_bytes / counter)
        worksheet.write(row, 3, sum_total_packets / counter)
        worksheet.write(row, 4, sum_timespan / counter)
        worksheet.write(row, 5, sum_throughput / counter)
        worksheet.write(row, 6, sum_average_latency / counter)
        worksheet.write(row, 7, sum_total_packet_lost / counter)
        worksheet.write(
            row, 8, (sum_total_packet_lost / sum_total_packets) * 100)
        row += 1

workbook.close()
