# count vowels
# language: Python


number = input("Enter a number: \n")


def count_vowels(number):
    if int(number) % 2 == 0:
        print("Even")
    else:
        print("Odd")


count_vowels(number)

# output:
# Enter a number:
# 10
# Even
# Enter a number:
# 11
# Odd
