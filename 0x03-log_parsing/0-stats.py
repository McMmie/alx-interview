#!/usr/bin/python3
"""
Log parsing: Reads log entries from standard input,
parses them, and provides statistics.
"""

import sys
from collections import defaultdict


if __name__ == '__main__':
    # Initialize variables
    filesize = 0
    codes = {"200", "301", "400", "401", "403", "404", "405", "500"}
    stats = defaultdict(int)

    def print_stats(stats: dict, file_size: int) -> None:
        """
        Prints statistics based on status codes and total file size.

        Args:
            stats (dict): Dictionary containing counts of each status code.
            file_size (int): Total size of the file.
        """

        print("File size: {:d}".format(file_size))
        for code, count in sorted(stats.items()):
            if count:
                print(f"{code}: {count}")

    try:

        # Read log entries from standard input
        with sys.stdin as file:
            for count, line in enumerate(file, start=1):
                try:
                    # Split log entry by spaces
                    data = line.split()
                    # Extract status code and update statistics
                    status_code = data[-2]

                    if status_code in codes:
                        stats[status_code] += 1
                        #  Extract file size and update total file size
                        filesize += int(data[-1])

                except (IndexError, ValueError):
                    # Skip malformed log entries
                    pass
                # Print statistics every 10 lines
                if count % 10 == 0:
                    print_stats(stats, filesize)

            print_stats(stats, filesize)
        except KeyboardInterrupt:
            print_stats(stats, filesize)
            raise
