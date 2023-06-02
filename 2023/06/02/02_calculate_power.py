# calculate power
# language: Python


x = input("Enter a number: \n")  # x is the base
n = input("Enter the power: \n")  # n is the exponent
x = int(x)
n = int(n)


def calculate_power(x, n):
    if n == 0:
        return 1
    else:
        return x * calculate_power(x, n - 1)


print(calculate_power(x, n))

# Output:
# Enter a number:
# 2
# Enter the power:
# 3
# 8
