"""Determine whether an integer is even or odd."""


def even_or_odd(n):
    if n % 2 == 0:
        return "Even"
    return "Odd"


if __name__ == "__main__":
    value = int(input("Enter an integer: "))
    print(f"{value} is {even_or_odd(value)}.")
