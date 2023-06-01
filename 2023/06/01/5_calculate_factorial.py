# calculate factorial
# language: Python


number = input("Enter a number: \n")
number = int(number)


def calculate_factorial(number):
    if number == 1:
        return number
    else:
        return number * calculate_factorial(number - 1)


print(calculate_factorial(number))

# output:
# Enter a number: 5
# 120
# Enter a number: 10
# 3628800
