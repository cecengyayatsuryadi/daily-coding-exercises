# check armstrong number
# language: Python


n = input("Enter a number: \n")
n = int(n)


def check_armstrong_number(n):
    n = str(n)
    sum = 0
    for i in n:
        sum += int(i) ** len(n)
    if sum == int(n):
        return True
    else:
        return False


print(check_armstrong_number(n))

# Output:
# Enter a number:
# 153
# True
# Enter a number:
# 123
# False
