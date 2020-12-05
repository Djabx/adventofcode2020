import os, sys
import dataclasses
import shared

SEARCH_FOR = 2020

data = []


@dataclasses.dataclass
class Line:
    min: int
    max: int
    char: str
    pwd: str
    count: int = dataclasses.field(init=False)

    def __post_init__(self):
        self.count = self.pwd.count(self.char)

    def is_ok(self):
        test = self.min <= self.count and self.count <= self.max
        return test

    def _idx_is_char(self, idx):
        if (idx + 1) < len(self.pwd):
            return self.pwd[idx + 1] == self.char
        return False

    def is_ok_for_cop(self):
        test_min = self._idx_is_char(self.min)
        test_max = self._idx_is_char(self.max)
        return test_min != test_max

    @classmethod
    def from_line(cls, line):
        info = line.replace(": ", " ").replace("-", " ")
        min_, max_, char, pwd = info.split(" ")
        min_ = int(min_)
        max_ = int(max_)
        x = cls(min=min_, max=max_, char=char, pwd=pwd)
        return x


data = [Line.from_line(l) for l in shared.get_data(2)]

nbr = len([x for x in data if x.is_ok()])
print(f"{nbr} pwd are valid")

nbr = len([x for x in data if x.is_ok_for_cop()])
print(f"{nbr} pwd are valid for cop")