#!/usr/bin/python3
'''This script parses HTTP request logs.
'''
import re


def extract_input(input_line):
    '''Extract sections of a line from an HTTP request log.

    Args:
        input_line (str): A single line from the HTTP request log.

    Returns:
        dict: A dictionary containing the status code and file size extracted from the log line.
    '''
    fp = (
        r'\s*(?P<ip>\S+)\s*',
        r'\s*\[(?P<date>\d+\-\d+\-\d+ \d+:\d+:\d+\.\d+)\]',
        r'\s*"(?P<request>[^"]*)"\s*',
        r'\s*(?P<status_code>\S+)',
        r'\s*(?P<file_size>\d+)'
    )
    info = {
        'status_code': 0,
        'file_size': 0,
    }
    log_fmt = '{}\\-{}{}{}{}\\s*'.format(fp[0], fp[1], fp[2], fp[3], fp[4])
    resp_match = re.fullmatch(log_fmt, input_line)
    if resp_match is not None:
        status_code = resp_match.group('status_code')
        file_size = int(resp_match.group('file_size'))
        info['status_code'] = status_code
        info['file_size'] = file_size
    return info


def print_statistics(total_file_size, status_codes_stats):
    '''Print the accumulated statistics of the HTTP request log.

    Args:
        total_file_size (int): The total file size of all processed logs.
        status_codes_stats (dict): A dictionary with HTTP status codes as keys and their counts as values.
    '''
    print('File size: {:d}'.format(total_file_size), flush=True)
    for status_code in sorted(status_codes_stats.keys()):
        num = status_codes_stats.get(status_code, 0)
        if num > 0:
            print('{:s}: {:d}'.format(status_code, num), flush=True)


def update_metrics(line, total_file_size, status_codes_stats):
    '''Update the metrics from a given HTTP request log.

    Args:
        line (str): Line of input from which to retrieve the metrics.
        total_file_size (int): The running total of the file sizes.
        status_codes_stats (dict): A dictionary with HTTP status codes as keys and their counts as values.

    Returns:
        int: The new total file size.
    '''
    line_info = extract_input(line)
    status_code = line_info.get('status_code', '0')
    if status_code in status_codes_stats.keys():
        status_codes_stats[status_code] += 1
    return total_file_size + line_info['file_size']


def run():
    '''Start the log parser to process HTTP request logs from standard input.
    '''
    line_num = 0
    total_file_size = 0
    status_codes_stats = {
        '200': 0,
        '301': 0,
        '400': 0,
        '401': 0,
        '403': 0,
        '404': 0,
        '405': 0,
        '500': 0,
    }
    try:
        while True:
            line = input()
            total_file_size = update_metrics(
                line,
                total_file_size,
                status_codes_stats,
            )
            line_num += 1
            if line_num % 10 == 0:
                print_statistics(total_file_size, status_codes_stats)
    except (KeyboardInterrupt, EOFError):
        print_statistics(total_file_size, status_codes_stats)


if __name__ == '__main__':
    run()

