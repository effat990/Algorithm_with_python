"""Find the maximum of three numbers."""


def maximum_of_three(a, b, c):
    maximum = a

    if b > maximum:
        maximum = b

    if c > maximum:
        maximum = c

    return maximum


if __name__ == "__main__":
    first = float(input("Enter the first number: "))
    second = float(input("Enter the second number: "))
    third = float(input("Enter the third number: "))

    print("Maximum value:", maximum_of_three(first, second, third))
