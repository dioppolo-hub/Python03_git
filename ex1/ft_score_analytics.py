import sys


def calc_scores(argc, scores) -> None:
    print("Total players:", len(scores))
    total = sum(scores)
    print("Total score:", total)
    average = total / len(scores)
    print("Average score:", average)
    biggest = max(scores)
    print("High score:", biggest)
    little = min(scores)
    print("Low score:", little)
    wide = biggest - little
    print("Score range:", wide)
    print()


if __name__ == "__main__":
    print("=== Player Score Analytics ===")
    argc = len(sys.argv)
    if argc == 1:
        print("No scores provided")
    else:
        i = 1
        scores = []
        while i < argc:
            try:
                num = int(sys.argv[i])
                scores.append(num)
            except ValueError:
                print(f"Invalid parameter: '{sys.argv[i]}'")
            i += 1
        if not scores:
            print("No scores provided")
        else:
            i = 0
            print("Scores processed: [", end="")
            while i < len(scores):
                if i == len(scores) - 1:
                    print(f"{scores[i]}]")
                else:
                    print(f"{scores[i]}, ", end="")
                i += 1
            calc_scores(argc, scores)
