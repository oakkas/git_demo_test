import sys


def default():
    print("hello")


def cat():
    print("Miav")


def dog():
    print("Hav")


def main():
    if sys.argv[1] == "dog":
        dog()
    elif sys.argv[1] == "cat":
        cat()
    else:
        default()


if __name__ == "__main__":
    main()
