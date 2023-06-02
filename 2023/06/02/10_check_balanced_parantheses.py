# check balanced parantheses
# language: Python


def check_balanced_parantheses(s):
    stack = []
    for i in s:
        if i == "(":
            stack.append(i)
        elif i == ")":
            if len(stack) == 0:
                return False
            stack.pop()
    if len(stack) == 0:
        return True
    else:
        return False


s = input("Enter a string: \n")
print(check_balanced_parantheses(s))

# Output:
# Enter a string:
# (a+b)
# True
# Enter a string:
# (a+b)*c
# True
# Enter a string:
# (a+b)*c)
# False
