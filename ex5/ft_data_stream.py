import random
import typing


def gen_event(Player_list: list[str], Action_list: list[str]) -> typing.Generator[tuple[str, str], None, None]:
    while True:
        yield (random.choice(Player_list), random.choice(Action_list))


def consume_event(lst: list[tuple[str, str]]) -> typing.Generator[tuple[str, str], None, None]:
    while True:
        size = len(lst)
        if size == 0:
            break
        temp = random.choice(lst)
        yield temp


if __name__ == "__main__":
    Player_list = ["Bob", "Dylan", "Alice", "Frank", "Sofia", "Deb"]
    Action_list = ["Run", "Sleep", "Move", "Climb", "Swim", "Grab"]

    i = 0
    event_gen = gen_event(Player_list, Action_list)
    while i <= 999:
        event = next(event_gen)
        print(f"Event {i}: Player {event[0]} did action {event[1]}")
        i += 1
    lst = []
    x = 10
    while x > 0:
        event = next(event_gen)
        lst.append(event)
        x -= 1
    print(f"Built list of 10 events: {lst}")
    lst_gen = consume_event(lst)
    while True:
        size = len(lst)
        if size == 0:
            break
        lst_tuple = next(lst_gen)
        print(f"Got event from list: {lst_tuple}")
        lst.remove(lst_tuple)
        print(f"Remains in list: {lst}")
