import random


def gen_player_achievements(achievements):
    num = random.randint(5, 10)
    rand_ach = []
    while num:
        rand_ach.append(random.choice(achievements))
        num -= 1
    return set(rand_ach)


if __name__ == "__main__":
    print("=== Achievement Tracker System ===\n")
    achievements = [
        'Crafting Genius', 'Strategist', 'World Savior',
        'Speed Runner', 'Survivor', 'Master Explorer', 'Treasure Hunter',
        'Unstoppable', 'First Steps', 'Collector Supreme', 'Untouchable',
        'Sharp Mind', 'Boss Slayer'
    ]
    first_set = gen_player_achievements(achievements)
    second_set = gen_player_achievements(achievements)
    third_set = gen_player_achievements(achievements)
    fourth_set = gen_player_achievements(achievements)
    print(f"Player Alice: {first_set}")
    print(f"Player Bob: {second_set}")
    print(f"Player Charlie: {third_set}")
    print(f"Player Dylan: {fourth_set}\n")

    All_ach = set().union(first_set, second_set, third_set, fourth_set)
    print(f"All distinct achievements: {All_ach}\n")

    Same_ach = first_set.intersection(second_set, third_set, fourth_set)
    print(f"Common achievmets: {Same_ach}\n")

    first_diff = first_set.difference(second_set, third_set, fourth_set)
    second_diff = second_set.difference(first_set, third_set, fourth_set)
    third_diff = third_set.difference(second_set, first_set, fourth_set)
    fourth_diff = fourth_set.difference(second_set, third_set, first_set)
    print(f"Only Alice has: {first_diff}")
    print(f"Only Bob has: {second_diff}")
    print(f"Only Charlie has: {third_diff}")
    print(f"Only Dylan has: {fourth_diff}\n")

    first_miss = All_ach.difference(first_set)
    second_miss = All_ach.difference(second_set)
    third_miss = All_ach.difference(third_set)
    fourth_miss = All_ach.difference(fourth_set)
    print(f"Alice is missing: {first_miss}")
    print(f"Bob is missing: {second_miss}")
    print(f"Charlie is missing: {third_miss}")
    print(f"Dylan is missing: {fourth_miss}")
