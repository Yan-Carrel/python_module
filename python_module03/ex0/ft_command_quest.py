import sys

if __name__ == "__main__":
    print("=== Command Quest ===")
    argv_len: int = len(sys.argv)
    i: int = 1
    print(f"Program name: {sys.argv[0]}")
    if argv_len < 2:
        print("No arguments provided!")
    else:
        print(f"Arguments received: {argv_len - 1}")
        while i < argv_len:
            print(f"Argument {i}: {sys.argv[i]}")
            i += 1
    print(f"Total arguments: {argv_len}")
