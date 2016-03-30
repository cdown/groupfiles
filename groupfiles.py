#!/usr/bin/env python

import collections
import os
import sys


FileSize = collections.namedtuple('FileSize', ['size', 'filename'])


if __name__ == '__main__':
    target_size = int(sys.argv[1])
    stdin_chomped = (line.rstrip('\n') for line in sys.stdin)
    file_sizes_by_size = sorted(
        FileSize(os.path.getsize(filename), filename)
        for filename in stdin_chomped
    )
    file_size_groups = []
    current_file_size_group = []
    current_file_size_group_size = 0

    for size, filename in file_sizes_by_size:
        if current_file_size_group_size + size <= target_size:
            current_file_size_group.append(filename)
            current_file_size_group_size += size
        else:
            file_size_groups.append(current_file_size_group)
            current_file_size_group = [filename]
            current_file_size_group_size = size

    if current_file_size_group:
        file_size_groups.append(current_file_size_group)

    for group in file_size_groups:
        print('\0'.join(group) + '\0\0')
