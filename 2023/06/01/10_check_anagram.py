# check anagram
# language: Python


str1 = input("Enter two strings: \n")
str2 = input("Enter two strings: \n")


def check_anagram(str1, str2):
    if len(str1) != len(str2):
        return False
    else:
        for i in range(len(str1)):
            if str1[i] != str2[-(i + 1)]:
                return False
        return True


print(check_anagram(str1, str2))

# output:
# Enter two strings:
# abc
# Enter two strings:
# cba
# True
#
# Enter two strings:
# abc
# Enter two strings:
# cbaa
# False
