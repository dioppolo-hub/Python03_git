import random
import typing


def gen_event(Player_list, Action_list) -> typing.Generator[tuple, None, None]:
    t = ()
    Player_num = len(Player_list)
    Action_num = len(Action_list)
    while True:
        yield (random.choice(Player_list), random.choice(Action_list))



if __name__ == "__main__":
    Player_list = ["Bob", "Dylan", "Alice", "Frank", "Sofia", "Deb"]
    Action_list = ["Run", "Sleep", "Move", "Climb", "Swim", "Grab"]

    i = 0
    event_gen = gen_event(Player_list, Action_list)
    while i <= 999:
        event = next(event_gen)
        print(f"Event {i}: Player {event[0]} did action {event[1]}")
        i += 1