"""
@desc:
    - Pratice with for loop

@Problem:
    - Given positive integer number n, determine whether it is a primer number or not

@Solution:
    - 5: 1, 5; 7: 1, 7; 11: 1, 11
    - 9: 1, 3, 9
    - 2: 1, 2
    - 1: 1
    - Bruteforce: naive solution
    - Loop from 1 to n: find all divisors of n
    - Using for loop

@Note:
    - range(n): from 0 to n - 1, [0, n)
    - range(n + 1): from 0 to n, [0, n + 1)
    - range(1, n + 1): from 1 to n, [1, n + 1)

@Debug
@handy example 1:
    - n = 5
    - step 1: divisor = 1 --> count = 1
    - step 2: divisor = 2 --> count = 1
    - step 3: divisor = 3 --> count = 1
    - step 4: divisor = 4 --> count = 1
    - step 5: divisor = 5 --> count = 5

@handy example 2:
    - n = 6
    - step 1: divisor = 1 --> count = 1
    - step 2: divisor = 2 --> count = 2
    - step 3: divisor = 3 --> count = 3
    - step 4: divisor = 4 --> count = 3
    - step 5: divisor = 5 --> count = 3
    - step 6: divisor = 6 --> count = 4
"""
n = int(input("Enter a positive integer number: "))

count = 0
for divisor in range(1, n + 1):
    if n % divisor == 0:
        count += 1

if count == 2:
    print(f"{n} is a prime  number")
else:
    print(f"{n} is not a prime  number")

