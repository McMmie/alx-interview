#!/usr/bin/python3
"""
Log parsing: Reads log entries from standard input,
parses them, and provides statistics.
"""

import sys
from collections import defaultdict


if __name__ == '__main__':
    # Initialize variables
    file_size, count = 0, 0
    codes = {"200", "301", "400", "401", "403", "404", "405", "500"}
    stats = {k: 0 for k in codes}

    def print_stats(stats: Counter, file_size: int) -> None:
        """
        Prints statistics based on status codes and total file size.

        Args:
            stats (dict): Dictionary containing counts of each status code.
            file_size (int): Total size of the file.
        """

        print("File size: {:d}".format(file_size))
        for k, v in sorted(stats.items()):
            if v:
                print(f"{k}: {v}")

    try:

        # Read log entries from standard input
        for line in sys.stdin:
            count += 1
            data = line.split()
                try:
                    status_code = data[-2]
                        if status_code in stats:
                            stats[status_code] += 1

                except BaseException:
                    pass
                try:
                    file_size += int(data[-1])
                except BaseException:
                    pass
                if count % 10 == 0:
                    print_stats(stats, filesize)

            print_stats(stats, filesize)
        except KeyboardInterrupt:
            print_stats(stats, filesize)
            raise
