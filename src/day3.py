import shared
import collections

Position = collections.namedtuple("Position", ["x", "y"])

TREE_CHAR = "#"


def get_num_of_tree(data, slope, p):
    total_tree = 0
    while True:
        p = Position(p.x + slope.x, p.y + slope.y)
        if p.y >= len(data):
            break
        line = data[p.y]
        if line[p.x % len(line)] == TREE_CHAR:
            total_tree += 1
    print(
        f"Found {total_tree} tree with a slop {slope.x} ▶ {slope.y} ▼",
    )
    return total_tree


data = [l for l in shared.get_data(3)]

nt_3_1 = get_num_of_tree(
    data=data,
    slope=Position(3, 1),
    p=Position(0, 0),
)


nt_1_1 = get_num_of_tree(
    data=data,
    slope=Position(1, 1),
    p=Position(0, 0),
)

nt_5_1 = get_num_of_tree(
    data=data,
    slope=Position(5, 1),
    p=Position(0, 0),
)

nt_7_1 = get_num_of_tree(
    data=data,
    slope=Position(7, 1),
    p=Position(0, 0),
)

nt_1_2 = get_num_of_tree(
    data=data,
    slope=Position(1, 2),
    p=Position(0, 0),
)

print(f"Total tree: {nt_1_2* nt_1_1* nt_3_1* nt_5_1* nt_7_1}")