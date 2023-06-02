# generate prime numbers
# language: Python


def generate_prime_numbers(n):
    prime_numbers = []
    for i in range(2, n + 1):
        is_prime = True
        for j in range(2, i):
            if i % j == 0:
                is_prime = False
        if is_prime:
            prime_numbers.append(i)
    return prime_numbers


n = input("Enter a number: \n")
n = int(n)
print(generate_prime_numbers(n))

# Output:
# Enter a number:
# 10
# [2, 3, 5, 7]
