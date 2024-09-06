#!/usr/bin/env python3

import argparse
from gendiff.parser import parse_files


def format_to_string(data, key, prefix=" "):
    if data[key] in (True, False, None):
        data_f = str(data[key]).lower()
        return f'  {prefix} {key}: {data_f}'
    return f'  {prefix} {key}: {data[key]}'


def generate_diff(file_path1, file_path2):
    file1, file2 = parse_files(file_path1, file_path2)
    keys = sorted(set(file1.keys()) | set(file2.keys()))
    data = []
    for key in keys:
        if (key in file1) and (key in file2):
            if file1[key] == file2[key]:
                format_to_string(file1, key)
                data.append(format_to_string(file1, key))
            else:
                data.append(format_to_string(file1, key, prefix='-'))
                data.append(format_to_string(file2, key, prefix='+'))
        elif (key in file1):
            data.append(format_to_string(file1, key, prefix='-'))
        elif (key in file2):
            data.append(format_to_string(file2, key, prefix='+'))
    result = "\n".join(data)
    return f'{{\n{result}\n}}'


def main():
    parser = argparse.ArgumentParser(
        description="Compares two configuration files and shows a difference."
    )
    parser.add_argument('first_file')
    parser.add_argument('second_file')
    parser.add_argument(
        '-f', '--format',
        help='set format of output'
    )

    parser.parse_args()


if __name__ == '__main__':
    main()
