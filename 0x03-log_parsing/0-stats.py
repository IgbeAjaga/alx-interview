#!/usr/bin/python3
"""
A script that reads stdin line by line and computes metrics
"""
import sys
import signal


def signal_handler(sig, frame):
    print_stats()
    sys.exit(0)

def print_stats():
    print(f"File size: {total_size}")
    for code in sorted(status_codes.keys()):
        if status_codes[code] > 0:
            print(f"{code}: {status_codes[code]}")

signal.signal(signal.SIGINT, signal_handler)

status_codes = {
    200: 0,
    301: 0,
    400: 0,
    401: 0,
    403: 0,
    404: 0,
    405: 0,
    500: 0
}

total_size = 0
counter = 0

try:
    for line in sys.stdin:
        counter += 1
        data = line.split()
        if len(data) > 2:
            try:
                code = int(data[-2])
                size = int(data[-1])
                total_size += size
                if code in status_codes:
                    status_codes[code] += 1
            except ValueError:
                pass
        if counter == 10:
            print_stats()
            counter = 0

except KeyboardInterrupt:
    print_stats()
    sys.exit(0)

