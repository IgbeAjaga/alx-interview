#!/usr/bin/python3
"""
Determines if a given data set represents a valid UTF-8 encoding
"""


def validUTF8(data):
    """
    Checks if data is a valid UTF-8 encoding
    """
    bytes_to_process = 0
    n = len(data)
    for num in range(n):
        if bytes_to_process > 0:
            bytes_to_process -= 1
            continue
        if type(data[num]) != int or data[num] < 0 or data[num] > 0x10ffff:
            return False
        elif data[num] <= 0x7f:
            bytes_to_process = 0
        elif data[num] & 0b11111000 == 0b11110000:
            # 4-byte utf-8 character encoding
            span = 4
            if n - num >= span:
                next_body = list(map(
                    lambda x: x & 0b11000000 == 0b10000000,
                    data[num + 1: num + span],
                ))
                if not all(next_body):
                    return False
                bytes_to_process = span - 1
            else:
                return False
        elif data[num] & 0b11110000 == 0b11100000:
            # 3-byte utf-8 character encoding
            span = 3
            if n - num >= span:
                next_body = list(map(
                    lambda x: x & 0b11000000 == 0b10000000,
                    data[num + 1: num + span],
                ))
                if not all(next_body):
                    return False
                bytes_to_process = span - 1
            else:
                return False
        elif data[num] & 0b11100000 == 0b11000000:
            # 2-byte utf-8 character encoding
            span = 2
            if n - num >= span:
                next_body = list(map(
                    lambda x: x & 0b11000000 == 0b10000000,
                    data[num + 1: num + span],
                ))
                if not all(next_body):
                    return False
                bytes_to_process = span - 1
            else:
                return False
        else:
            return False
    return True
