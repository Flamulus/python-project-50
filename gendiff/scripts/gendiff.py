#!/usr/bin/env python3

import argparse
import json


def generate_diff(file_path1, file_path2):
    file1 = json.load(open(file_path1))
    file2 = json.load(open(file_path2))
    keys = sorted(set(file1.keys()) | set(file2.keys()))
    data = []
    for key in keys:
        if (key in file1) and (key in file2):
            if file1[key] == file2[key]:
                data.append(f'    {key}: {file1[key]}')
            else:
                data.append(f'  - {key}: {file1[key]}')
                data.append(f'  + {key}: {file2[key]}')
        elif (key in file1):
            data.append(f'  - {key}: {file1[key]}')
        elif (key in file2):
            data.append(f'  + {key}: {file2[key]}')
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
