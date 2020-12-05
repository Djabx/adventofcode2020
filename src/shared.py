import os, sys


def get_data(num_day, sample=False):
    fname = f"day{num_day}.txt" if not sample else f"day{num_day}_sample.txt"
    data_name = os.path.join(os.path.dirname(__file__), "..", "data", fname)
    with open(data_name) as data_fh:
        for line in data_fh:
            line = line.strip()
            if len(line):
                yield line
