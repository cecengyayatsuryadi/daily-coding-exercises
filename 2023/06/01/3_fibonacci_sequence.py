# fibonacci sequence
# language: Python


number = input("Enter a number: \n")
number = int(number)


def fibonacci_sequence(number):
    if number <= 1:
        return number
    else:
        return fibonacci_sequence(number - 1) + fibonacci_sequence(number - 2)


print(fibonacci_sequence(number))

# output:
# Enter a number:
# 10
# 55
