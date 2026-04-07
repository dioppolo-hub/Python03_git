import random


if __name__ == "__main__":
    print("=== Game Data Alchemist ===\n")
    lst = ["Alice", "luca", "Sofia", "Franci", "samu", "bob", "Charlie"]
    print(f"Initial list of players: {lst}")
    cap_lst = [i.capitalize() for i in lst]
    print(f"New list with all names capitalized: {cap_lst}")
    only_cap = [i for i in lst if i == i.capitalize()]
    print(f"New list of capitalized names only: {only_cap}")
    dct = {x: random.randint(250, 750) for x in cap_lst}
    print(f"Score dict: {dct}")
    for i in dct:
        num = sum(dct.values())
    avrg = round(num / len(dct))
    print(f"Score average is {avrg}")
    dct = {x: random.randint(avrg, 750) for x in cap_lst}
    print(f"High scores: {dct}")
