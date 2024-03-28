import sys
import signal

# Initialize variables to store metrics
total_file_size = 0
status_code_counts = {200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0}
line_count = 0

def handle_interrupt(signal, frame):
    print_statistics()
    sys.exit(0)

def print_statistics():
    print("Total file size:", total_file_size)
    for status_code in sorted(status_code_counts.keys()):
        if status_code_counts[status_code] > 0:
            print(f"{status_code}: {status_code_counts[status_code]}")

# Register interrupt handler
signal.signal(signal.SIGINT, handle_interrupt)

try:
    for line in sys.stdin:
        try:
            parts = line.split()
            ip_address = parts[0]
            date = parts[3][1:]
            status_code = int(parts[-3])
            file_size = int(parts[-2])
            
            # Check if the line matches the expected format
            if parts[5].startswith("GET") and len(parts) >= 10:
                total_file_size += file_size
                status_code_counts[status_code] += 1
                line_count += 1
            
            # Print statistics every 10 lines
            if line_count % 10 == 0:
                print_statistics()
        except (ValueError, IndexError):
            # Skip the line if it doesn't match the expected format
            continue
except KeyboardInterrupt:
    print_statistics()
    sys.exit(0)

