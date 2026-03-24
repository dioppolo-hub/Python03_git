import math


def get_player_pos():
    print("Get a first set of coordinates")
    print("Enter new coordinates as floats in format 'x,y,z': ", end="")
    i = 0
    coords = []
    while i < 3:
        try:
            x = float(input())
            coords.append(x)
        except ValueError:
            print("Invalid syntax")
        i += 1
    touple = tuple(coords)
    i = 0
    while i < 3:
        if i == 2:
            print(f"{touple[i]}")
        else:
            print(f"{touple[i]}, ", end="")
        i += 1

if __name__ == "__main__":
    get_player_pos()