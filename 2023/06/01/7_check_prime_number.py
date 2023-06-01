# check prime number
# language: Python


number = input("Enter a number: \n")
number = int(number)


def isPrime(number):
    if number > 1:
        for i in range(2, number):
            if number % i == 0:
                return False
            return True
        else:
            return False


if isPrime(number):
    print("Prime")
else:
    print("Not Prime")

# output:
# Enter a number:
# 2
# Prime
# Enter a number:
# 3
# Prime
# Enter a number:
# 4
# Not Prime
# Enter a number:
# 5
# Prime
