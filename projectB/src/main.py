def subtraction(a, b):
    return a - b

if __name__ == "__main__":
    import sys
    args = sys.argv
    if len(args) > 2:
        print(subtraction(int(args[1]), int(args[2])))
