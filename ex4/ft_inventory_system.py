import sys


def get_inventory(d, arg):
    key, value = arg.split(":")
    if key in d:
        raise Exception
    d[key] = value
    return d


if __name__ == "__main__":
    print("=== Inventory System Analysis ===\n")
    d: dict[str, str] = {}
    for arg in sys.argv[1:]:
        try:
            d = get_inventory(d, arg)
        except ValueError:
            print(f"Error - invalid parameter: '{arg}'")
        except Exception:
            print(f"Reduntant item '{arg}' - discarding")
    new_d: dict[str, int] = {}
    for k in d:
        try:
            new_d[k] = int(d[k])
        except ValueError:
            print(
                f"Quantity error for '{k}': invalid"
                f"literal fot int(): '{d[k]}'"
                )
    d_int: dict[str, int] = new_d
    print(f"Got inventory: {d_int}")
    items = d_int.keys()
    print(f"Item list: {items}")
    i = 0
    for count in d_int:
        i += 1
    num_item = sum(d_int.values())
    print(f"Total quantity of the {i} items: {num_item}")
    for item in d_int:
        quantity = round(((d_int[item] * 100) / num_item))
        print(f"Item {item} represents {quantity}%")
    biggest: int | None = None
    biggest_name: str | None = None
    for num in d_int:
        if biggest is None or d_int[num] > biggest:
            biggest = d_int[num]
            biggest_name = num
    print(f"Item most abundant: {biggest_name} with quantity {biggest}")
    lowest: int | None = None
    lowest_name: str | None = None
    for num in d_int:
        if lowest is None or d_int[num] < lowest:
            lowest = d_int[num]
            lowest_name = num
    print(f"Item least abundant: {lowest_name} with quantity {lowest}")
    d_int.update({'magic_item': 1})
    print(f"Updated inventory: {d_int}")
