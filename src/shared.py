import os, sys


def get_data(num_day):
    data_tpl = "day{num_day}.txt"
    if len(sys.argv) >= 2:
        # there is a template name
        data_tpl = sys.argv[1]
    fname = data_tpl.format(num_day=num_day)
    data_name = os.path.join(os.path.dirname(__file__), "..", "data", fname)
    with open(data_name) as data_fh:
        for line in data_fh:
            line = line.strip()
            yield line
