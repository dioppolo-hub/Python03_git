import math


def get_player_pos():
    try:
        print("Enter new coordinates as floats in format 'x, y, z': ", end="")
        s = input()
        t = ()
        parti = s.split()
        i = 0
        for x in parti:
            t = t + (float(x),)
            i += 1
        if i < 3:
            raise Exception
        elif i > 3:
            raise Exception
    except ValueError:
        print("Invalid syntax, retry with valid set of coordinates!")
        return get_player_pos()
    except Exception:
        if i < 3:
            print("Not enough arguments, please insert only 3 coordinates!")
            return get_player_pos()
        if i > 3:
            print("Too many arguments, please insert only 3 coordinates!")
            return get_player_pos()
    return t


if __name__ == "__main__":
    print("=== Game Coordinate System ===\n")
    print("Get a first set of coordinates")
    t = get_player_pos()
    print(f"Got a first tuple: {t}")
    print(f"It includes: X={t[0]}, Y={t[1]}, Z={t[2]}")
    center = math.sqrt((t[0]**2) + (t[1]**2) + (t[2]**2))
    print(f"Distance to center: {center:.4f}\n")
    print("Get a second set of coordinates")
    t2 = get_player_pos()
    two_center = math.sqrt(
        (t2[0] - t[0])**2 + (t2[1] - t[1])**2 + (t2[2] - t[2])**2
    )
    print(f"Distance between the 2 sets of coordinates: {two_center}")
