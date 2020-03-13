def hello(name):
    return "hello, " + name

if __name__ == "__main__":
    import sys
    args = sys.argv
    if len(args) > 1:
        print(hello(args[1]))
