def is_even(number):
    """
    @params:
         - number: positive integer
    @return:
         - True: if number is an even number
         -  False: otherwise
    """
    print("Hehehe 01")
    return (number % 2 == 0)

print("Heheheh 02")
number = int(input())
if (is_even(number)):
    print(f"{number} is an even number")
else:
    print(f"{number} is an odd number")

