"""Check whether an integer is prime."""


def is_prime(n):
    if n < 2:
        return False

    divisor = 2
    while divisor * divisor <= n:
        if n % divisor == 0:
            return False
        divisor += 1

    return True


if __name__ == "__main__":
    value = int(input("Enter an integer: "))
    if is_prime(value):
        print(f"{value} is a prime number.")
    else:
        print(f"{value} is not a prime number.")
