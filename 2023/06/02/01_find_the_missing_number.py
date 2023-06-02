# find the missing number
# language: Python


def find_missing_number(arr):
    n = len(arr) + 1
    # The sum of the numbers from 1 to n is n * (n + 1) / 2.
    total = n * (n + 1) / 2
    sum_of_arr = sum(arr)
    return total - sum_of_arr


if __name__ == "__main__":
    arr = [1, 2, 3, 4, 6, 7]
    print(find_missing_number(arr))

    arr = [1, 2, 3, 4, 5, 6, 7, 9]
    print(find_missing_number(arr))

    arr = [1, 2, 3, 4, 5, 6, 7, 8, 10]
    print(find_missing_number(arr))

# Output:
# 5
# 8
