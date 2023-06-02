# reverse words in a string
# language: python


s = input("Enter a string: \n")
s = str(s)


def reverse_words_in_a_string(s):
    return " ".join(reversed(s.split()))


print(reverse_words_in_a_string(s))

# Output:
# Enter a string:
# I am a student.
# student. a am I
