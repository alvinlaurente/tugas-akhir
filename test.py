import os
import pyshark
import xlsxwriter

workbook = xlsxwriter.Workbook('test.xlsx')
scenario = ['eoip', 'gre', 'ipip']
for x in scenario:
    worksheet = workbook.add_worksheet(x)
    row = 0
    col = 0
    test_file = ['10mb', '20mb', '30mb', '40mb', '50mb']
    for y in test_file:
        timespan1 = 0
        bits1 = 0
        throughput1 = 0
        latency_capture1 = 0
        latency_display1 = 0
        count1 = 0
        total1 = 0
        worksheet.write(row, 0, y)
        row += 1
        i = 0

        worksheet.write(row, 0, 'No')
        worksheet.write(row, 1, 'Packet')
        worksheet.write(row, 2, 'Bytes')
        worksheet.write(row, 3, 'Bits')
        worksheet.write(row, 4, 'Timespan')
        worksheet.write(row, 5, 'Throughput')
        worksheet.write(row, 6, 'LatencyCapture')
        worksheet.write(row, 7, 'LatencyDisplay')
        row += 1

        data = ['1.pcapng', '2.pcapng', '3.pcapng', '4.pcapng', '5.pcapng',
                '6.pcapng', '7.pcapng', '8.pcapng', '9.pcapng', '10.pcapng']
        for z in data:
            location = x + '/' + y + '/' + z
            bits = 0
            total = 0
            count = 0
            timestamp1 = 0
            timestamp2 = 0
            timestamp3 = 0
            timestamp4 = 0
            timestamp5 = 0
            timestamp6 = 0
            timestamp7 = 0

            cap = pyshark.FileCapture(location, only_summaries=True)
            cap

            for pkt in cap:
                src_addr = pkt.source
                dst_addr = pkt.destination
                lengths = pkt.length
                timestamp = pkt.time
