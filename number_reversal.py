"""Reverse the digits of a positive integer."""


def reverse_number(n):
    if n <= 0:
        raise ValueError("Please enter a positive integer.")

    reversed_number = 0
    while n > 0:
        digit = n % 10
        reversed_number = reversed_number * 10 + digit
        n //= 10

    return reversed_number


if __name__ == "__main__":
    value = int(input("Enter a positive integer: "))
    try:
        print("Reversed number:", reverse_number(value))
    except ValueError as error:
        print(error)
