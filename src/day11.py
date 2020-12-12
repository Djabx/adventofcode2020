"""
--- Day 11: Seating System ---

Your plane lands with plenty of time to spare. The final leg of your journey is a ferry that goes directly to the tropical island where you can finally start your vacation. As you reach the waiting area to board the ferry, you realize you're so early, nobody else has even arrived yet!

By modeling the process people use to choose (or abandon) their seat in the waiting area, you're pretty sure you can predict the best place to sit. You make a quick map of the seat layout (your puzzle input).

The seat layout fits neatly on a grid. Each position is either floor (.), an empty seat (L), or an occupied seat (#). For example, the initial seat layout might look like this:

L.LL.LL.LL
LLLLLLL.LL
L.L.L..L..
LLLL.LL.LL
L.LL.LL.LL
L.LLLLL.LL
..L.L.....
LLLLLLLLLL
L.LLLLLL.L
L.LLLLL.LL

Now, you just need to model the people who will be arriving shortly. Fortunately, people are entirely predictable and always follow a simple set of rules. All decisions are based on the number of occupied seats adjacent to a given seat (one of the eight positions immediately up, down, left, right, or diagonal from the seat). The following rules are applied to every seat simultaneously:

    If a seat is empty (L) and there are no occupied seats adjacent to it, the seat becomes occupied.
    If a seat is occupied (#) and four or more seats adjacent to it are also occupied, the seat becomes empty.
    Otherwise, the seat's state does not change.

Floor (.) never changes; seats don't move, and nobody sits on the floor.

After one round of these rules, every seat in the example layout becomes occupied:

#.##.##.##
#######.##
#.#.#..#..
####.##.##
#.##.##.##
#.#####.##
..#.#.....
##########
#.######.#
#.#####.##

After a second round, the seats with four or more occupied adjacent seats become empty again:

#.LL.L#.##
#LLLLLL.L#
L.L.L..L..
#LLL.LL.L#
#.LL.LL.LL
#.LLLL#.##
..L.L.....
#LLLLLLLL#
#.LLLLLL.L
#.#LLLL.##

This process continues for three more rounds:

#.##.L#.##
#L###LL.L#
L.#.#..#..
#L##.##.L#
#.##.LL.LL
#.###L#.##
..#.#.....
#L######L#
#.LL###L.L
#.#L###.##

#.#L.L#.##
#LLL#LL.L#
L.L.L..#..
#LLL.##.L#
#.LL.LL.LL
#.LL#L#.##
..L.L.....
#L#LLLL#L#
#.LLLLLL.L
#.#L#L#.##

#.#L.L#.##
#LLL#LL.L#
L.#.L..#..
#L##.##.L#
#.#L.LL.LL
#.#L#L#.##
..L.L.....
#L#L##L#L#
#.LLLLLL.L
#.#L#L#.##

At this point, something interesting happens: the chaos stabilizes and further applications of these rules cause no seats to change state! Once people stop moving around, you count 37 occupied seats.

Simulate your seating area by applying the seating rules repeatedly until no seats change state. How many seats end up occupied?

--- Part Two ---

As soon as people start to arrive, you realize your mistake. People don't just care about adjacent seats - they care about the first seat they can see in each of those eight directions!

Now, instead of considering just the eight immediately adjacent seats, consider the first seat in each of those eight directions. For example, the empty seat below would see eight occupied seats:

.......#.
...#.....
.#.......
.........
..#L....#
....#....
.........
#........
...#.....

The leftmost empty seat below would only see one empty seat, but cannot see any of the occupied ones:

.............
.L.L.#.#.#.#.
.............

The empty seat below would see no occupied seats:

.##.##.
#.#.#.#
##...##
...L...
##...##
#.#.#.#
.##.##.

Also, people seem to be more tolerant than you expected: it now takes five or more visible occupied seats for an occupied seat to become empty (rather than four or more from the previous rules). The other rules still apply: empty seats that see no occupied seats become occupied, seats matching no rule don't change, and floor never changes.

Given the same starting layout as above, these new rules cause the seating area to shift around as follows:

L.LL.LL.LL
LLLLLLL.LL
L.L.L..L..
LLLL.LL.LL
L.LL.LL.LL
L.LLLLL.LL
..L.L.....
LLLLLLLLLL
L.LLLLLL.L
L.LLLLL.LL

#.##.##.##
#######.##
#.#.#..#..
####.##.##
#.##.##.##
#.#####.##
..#.#.....
##########
#.######.#
#.#####.##

#.LL.LL.L#
#LLLLLL.LL
L.L.L..L..
LLLL.LL.LL
L.LL.LL.LL
L.LLLLL.LL
..L.L.....
LLLLLLLLL#
#.LLLLLL.L
#.LLLLL.L#

#.L#.##.L#
#L#####.LL
L.#.#..#..
##L#.##.##
#.##.#L.##
#.#####.#L
..#.#.....
LLL####LL#
#.L#####.L
#.L####.L#

#.L#.L#.L#
#LLLLLL.LL
L.L.L..#..
##LL.LL.L#
L.LL.LL.L#
#.LLLLL.LL
..L.L.....
LLLLLLLLL#
#.LLLLL#.L
#.L#LL#.L#

#.L#.L#.L#
#LLLLLL.LL
L.L.L..#..
##L#.#L.L#
L.L#.#L.L#
#.L####.LL
..#.#.....
LLL###LLL#
#.LLLLL#.L
#.L#LL#.L#

#.L#.L#.L#
#LLLLLL.LL
L.L.L..#..
##L#.#L.L#
L.L#.LL.L#
#.LLLL#.LL
..#.L.....
LLL###LLL#
#.LLLLL#.L
#.L#LL#.L#

Again, at this point, people stop shifting around and the seating area reaches equilibrium. Once this occurs, you count 26 occupied seats.

Given the new visibility method and the rule change for occupied seats becoming empty, once equilibrium is reached, how many seats end up occupied?
"""

import shared
import dataclasses
import typing
import copy

FLOOR = "."
SEAT_EMPTY = "L"
SEAT_OCCUPIED = "#"


@dataclasses.dataclass
class Position:
    x: int
    y: int


@dataclasses.dataclass
class RoomConfiguration:
    conf: typing.List[typing.List[str]]

    state: typing.List[typing.List[str]] = dataclasses.field(init=False)

    def __str__(self):
        return "\n".join("".join(l) for l in self.state)

    def __post_init__(self):
        self.state = copy.deepcopy(self.conf)

    def __iter__(self) -> typing.Iterator[Position]:
        for x in range(len(self.state)):
            for y in range(len(self.state[x])):
                p = Position(x, y)
                if self.is_valid(p):
                    yield p

    def is_valid(self, pos: Position) -> bool:
        return (
            0 <= pos.x < len(self.state)
            and 0 <= pos.y < len(self.state[pos.x])
            and self.is_seat(pos)
        )

    def is_floor(self, pos: Position) -> bool:
        return self.state[pos.x][pos.y] == FLOOR

    def is_seat(self, pos: Position) -> bool:
        return not self.is_floor(pos)

    def is_seat_empty(self, pos: Position) -> bool:
        return self.state[pos.x][pos.y] == SEAT_EMPTY

    def is_seat_occupied(self, pos: Position) -> bool:
        return self.state[pos.x][pos.y] == SEAT_OCCUPIED

    def get_adjacent_seats(self, pos: Position) -> typing.Iterator[Position]:
        for dx in (-1, 0, 1):
            for dy in (-1, 0, 1):
                if dx == dy == 0:
                    continue
                p = Position(pos.x + dx, pos.y + dy)
                if self.is_valid(p):
                    yield p

    def compute_next_state(self) -> bool:
        changed = False
        new_state = copy.deepcopy(self.state)

        def set_new_state(pos: Position, state: str):
            new_state[pos.x][pos.y] = state

        for pos in self:
            if self.is_seat_empty(pos) and all(
                self.is_seat_empty(adj) for adj in self.get_adjacent_seats(pos)
            ):
                changed = True
                set_new_state(pos, SEAT_OCCUPIED)
            if self.is_seat_occupied(pos):
                adjs = list(self.get_adjacent_seats(pos))
                num_occupied = len([1 for adj in adjs if self.is_seat_occupied(adj)])
                if 4 <= num_occupied:
                    changed = True
                    set_new_state(pos, SEAT_EMPTY)

        if changed:
            self.state = new_state
        return changed

    def count_occupied(self) -> int:
        return sum(1 for pos in self if self.is_seat_occupied(pos))


def load_data():
    return [list(x) for x in shared.get_data(11)]


def part1():
    rc = RoomConfiguration(load_data())
    changed = True
    while changed:
        print("-" * 10)
        print(str(rc))
        changed = rc.compute_next_state()
    print(f"Found {rc.count_occupied()} occupied")


part1()