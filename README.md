# Week 01 — Basic Algorithmic Problems

## Objective
 learning about functions, loops, conditional statements, arithmetic operators, and basic problem-solving using Python.

## Tasks

### Task 1: Factorial Calculation
Problem: Calculate the factorial of a non-negative integer.

Approach:
1. Start with `result = 1`.
2. Multiply `result` by every integer from 1 through `n`.
3. Return the result.

 base case: `0! = 1`. The loop does not run when `n = 0`, so the initial value `1` is returned.

Complexity: Time `O(n)`; auxiliary space `O(1)`.

Example: Input `5` → Output `120`.

### Task 2: Even-Odd Identification
Problem: Determine whether an integer is even or odd.

Approach:
1. Divide the number by 2 using the modulo operator `%`.
2. If the remainder is 0, return `Even`.
3. Otherwise, return `Odd`.

Complexity: Time `O(1)`; auxiliary space `O(1)`.

Example: Input `7` → Output `Odd`.

### Task 3: Maximum Value Determination
Problem: Find the largest among three numbers.

Approach:
1. Assume the first number is the maximum.
2. Compare the second number with the current maximum.
3. Compare the third number with the updated maximum.
4. Return the largest value found.

Complexity: Time `O(1)`; auxiliary space `O(1)`.

Example: Input `(8, 3, 12)` → Output `12`.

### Task 4: Digit Sum Calculation
Problem: Calculate the sum of the digits of a positive integer.

Approach:
1. Get the last digit with `n % 10`.
2. Add that digit to a running total.
3. Remove the last digit with integer division, `n //= 10`.
4. Repeat until the number becomes 0.

Complexity: Time `O(d)`; auxiliary space `O(1)`, where `d` is the number of digits.

Example: Input `482` → Output `14`.

### Task 5: Prime Number Checking
Problem: Determine whether an integer is prime.

Approach:
1. Numbers less than 2 are not prime.
2. Check possible divisors starting from 2.
3. Stop when the divisor squared exceeds the number.
4. If any divisor divides the number exactly, it is not prime; otherwise, it is prime.

Checking only up to the square root is sufficient because a composite number must have a factor no greater than its square root.

Complexity: Time `O(√n)` in the worst case; auxiliary space `O(1)`.

Example: Input `13` → Output `Prime`.

### Task 6: Number Reversal
Problem: Reverse the digits of a positive integer.

Approach:
1. Extract the last digit using `n % 10`.
2. Append it to the reversed number using `reversed_number * 10 + digit`.
3. Remove the last digit with `n //= 10`.
4. Repeat until no digits remain.

Complexity: Time `O(d)`; auxiliary space `O(1)`, where `d` is the number of digits.

Example: Input `1234` → Output `4321`.

## Complexity Summary

| Task | Time Complexity | Auxiliary Space |
|---|---:|---:|
| Factorial | `O(n)` | `O(1)` |
| Even/Odd | `O(1)` | `O(1)` |
| Maximum of Three | `O(1)` | `O(1)` |
| Digit Sum | `O(d)` | `O(1)` |
| Prime Check | `O(√n)` | `O(1)` |
| Number Reversal | `O(d)` | `O(1)` |

Here, `n` is the input value and `d` is the number of digits where relevant. These are auxiliary-space complexities and exclude the storage required for the input and returned result.

## How to Run
Open a terminal in the `Week-01` folder and run any task, for example:

```bash
python factorial.py
python even_odd.py
python maximum_of_three.py
python digit_sum.py
python prime_check.py
python number_reversal.py
```



## Testing Checklist
- [ ] Factorial: test `0`, `1`, and a larger non-negative integer.
- [ ] Even/Odd: test an even number, an odd number, and a negative integer.
- [ ] Maximum: test when each of the three positions contains the maximum, including ties.
- [ ] Digit Sum: test a number containing zero, such as `405`.
- [ ] Prime: test `-3`, `0`, `1`, `2`, `9`, and `13`.
- [ ] Reversal: test a number ending in zero, such as `1200`.


