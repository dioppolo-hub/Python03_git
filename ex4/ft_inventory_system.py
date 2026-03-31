import sys


def get_inventory(d, arg):
    key, value = arg.split(":")
    if key in d:
        raise Exception
    d[key] = value
    return d


if __name__ == "__main__":
    print("=== Inventory System Analysis ===\n")
    d = {}
    for arg in sys.argv[1:]:
        try:
            d = get_inventory(d, arg)
        except ValueError:
            print(f"Error - invalid parameter: '{arg}'")
        except Exception:
            print(f"Reduntant item '{arg}' - discarding")
    new_d = {}
    for k in d:
        try:
            new_d[k] = int(d[k])
        except ValueError:
            print(f"Quantity error for '{k}': invalid literal fot int(): '{d[k]}'")
    d = new_d
    print(f"Got inventory: {d}")
    items = d.keys()
    print(f"Item list: {items}")
    i = 0
    for count in d:
        i += 1
    num_item = sum(d.values())
    print(f"Total quantity of the {i} items: {num_item}")
    for item in d:
        quantity = round(((d[item] * 100) / num_item))
        print(f"Item {item} represents {quantity}%")
