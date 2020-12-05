import os, sys
import shared

SEARCH_FOR = 2020

data = [int(l) for l in shared.get_data(1)]

nbr_data = len(data)

for i, x in enumerate(data):
    for j, y in enumerate(reversed(data)):
        if x + y == SEARCH_FOR:
            print(f"Found {x}, {y} = + {x+y} = * {x*y}")
        elif i + j > nbr_data:
            break

print("#" * 10)

for i, x in enumerate(data):
    for j, y in enumerate(data):
        for k, z in enumerate(data):
            if x + y + z == SEARCH_FOR:
                print(f"Found {x}, {y}, {z }= + {x+y+z} = * {x*y*z}")
                break
