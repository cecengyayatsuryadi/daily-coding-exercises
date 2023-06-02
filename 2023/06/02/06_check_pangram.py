# check pangram
# language: Python


s = input("Enter a string: \n")


def check_pangram(s):
    s = s.lower()
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    for i in alphabet:
        if i not in s:
            return False
    return True


print(check_pangram(s))

# Output:
# Enter a string:
# The quick brown fox jumps over the lazy dog.
# True
# Enter a string:
# The quick brown fox jumps over the lazy cat.
# False
