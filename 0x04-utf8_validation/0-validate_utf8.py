#!/usr/bin/python3
"""
Determines if a given data set represents a valid UTF-8 encoding
"""


def validUTF8(data):
    """Checks if data is a valid UTF-8 encoding"""
    bytes_to_process = 0

    for num in data:
        if bytes_to_process == 0:
            if (num >> 5) == 0b110:
                bytes_to_process = 1
            elif (num >> 4) == 0b1110:
                bytes_to_process = 2
            elif (num >> 3) == 0b11110:
                bytes_to_process = 3
            elif (num >> 7):
                return False
        else:
            if (num >> 6) != 0b10:
                return False
            bytes_to_process -= 1

    return bytes_to_process == 0
