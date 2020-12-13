import inspect
import os
import sys


def _get_data_name():
    curframe = inspect.currentframe()
    callers = inspect.getouterframes(curframe, 2)
    caller = callers[2]  # 1 is caller 2 is module caller
    caller_fname = caller.filename

    data_tpl = "data.txt"
    if len(sys.argv) >= 2:
        # there is a template name
        data_tpl = sys.argv[1]
    data_name = os.path.join(os.path.dirname(caller_fname), data_tpl)
    return data_name


def get_data(num_day=None):
    with open(_get_data_name()) as data_fh:
        for line in data_fh:
            line = line.strip()
            yield line


def get_data_full(num_day=None):
    with open(_get_data_name()) as data_fh:
        return data_fh.read()
