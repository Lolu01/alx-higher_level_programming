#!/usr/bin/python3

""" Script that reads stdin line by line and computes metrics"""

import sys


def print_metrics(status_codes, file_size):
    """ Print metrics """
    print("File size: {}".format(file_size))
    for key in sorted(status_codes.keys()):
        if status_codes[key] != 0:
            print("{}: {}".format(key, status_codes[key]))


if __name__ == "__main__":
    status_codes = {"200": 0, "301": 0, "400": 0, "401": 0,
                    "403": 0, "404": 0, "405": 0, "500": 0}
    file_size = 0
    line_counter = 0
    try:
        for line in sys.stdin:
            line_counter += 1
            parsed_line = line.split()
            try:
                file_size += int(parsed_line[-1])
            except Exception:
                pass
            try:
                status_codes[parsed_line[-2]] += 1
            except Exception:
                pass
            if line_counter % 10 == 0:
                print_metrics(status_codes, file_size)
        print_metrics(status_codes, file_size)
    except KeyboardInterrupt:
        print_metrics(status_codes, file_size)
        raise
