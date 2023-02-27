number = int(input("Enter a number: "))

total = 0

total += number % 10
number = number // 10

total += number % 10
number = number // 10

total += number % 10
number = number // 10

total += number % 10
number = number // 10

total += number

print("Total :", total)

