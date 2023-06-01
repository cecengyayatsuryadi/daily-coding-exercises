# check palindrome
# language: Python


number = input("Enter a number: \n")


def check_palindrome(number):
    if str(number) == str(number)[::-1]:
        return True
    else:
        return False


print(check_palindrome(number))

# output:
# Enter a number:
# 12321
# True
#
# Enter a number:
# 12345
# False
