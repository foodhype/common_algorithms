import heapq
import itertools
import os


def write_chunk(chunk, fname, chunk_index):
    partfile_name = "%s.part.%d" % (fname, chunk_index)
    partfile = open(partfile_name, "w")
    for line in chunk:
        partfile.write(line)
    partfile.close()

    return partfile_name 


def external_merge_sort(fname, chunk_size):
    chunk_index = 0
    partfile_names = []
    
    chunk = []
    with open(fname) as f:
    for line in f:
        chunk.append(line)

        if len(chunk) == chunk_size:
            chunk.sort()
            partfile_name = write_chunk(chunk, fname, chunk_index)
            partfile_names.append(partfile_name)
            chunk = []
            chunk_index += 1

    if chunk:
        partfile_name = write_chunk(chunk, fname, chunk_index)
        partfile_names.append(partfile_name)

    partfiles = [open(filename) for filename in partfile_names]

    for line in heapq.merge(*partfiles):
        yield line

    for partfile in partfiles:
        partfile.close()
    for partfile_name in partfile_names:
        os.remove(partfile_name)


def most_common_words(k, fname):
    most_common = []
    count = 0
    prev_line = None

    for line in external_merge_sort(fname, 100000):
        if line == prev_line:
            count += 1
        else:
            if len(most_common) < k:
                heapq.heappush(most_common, (count, line))
            elif count > most_common[0][0]:
                heapq.heappop(most_common)
                heapq.heappush(most_common, (count, line))
            count = 1
            prev_line = line

    return most_common


print most_common_words(10, "log.txt")
