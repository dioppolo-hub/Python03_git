import sys

if __name__ == "__main__":
    print("=== Command Quest ===")
    argc = len(sys.argv)
    i = 0
    print("Program name:", sys.argv[i])
    if argc == 1:
        print("No arguments provided!")
    else:
        print("Arguments received:", argc - 1)
    i += 1
    while i < argc:
        print("Argument 1:", sys.argv[i])
        i += 1
    print("Total arguments:", argc)
    print()
