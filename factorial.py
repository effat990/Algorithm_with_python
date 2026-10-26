"""Calculate the factorial of a non-negative integer."""


def factorial(n):
    if n < 0:
        raise ValueError("Factorial is not defined for negative integers.")

    result = 1
    for number in range(1, n + 1):
        result *= number

    return result


if __name__ == "__main__":
    value = int(input("Enter a non-negative integer: "))
    try:
        print(f"{value}! = {factorial(value)}")
    except ValueError as error:
        print(error)
