# calculate average
# language: Python


def calculate_average(arr):
    return sum(arr) / len(arr)


if __name__ == "__main__":
    arr = [1, 2, 3, 4, 5]
    print(calculate_average(arr))

    arr = [1, 2, 3, 4, 5, 6]
    print(calculate_average(arr))

    arr = [1, 2, 3, 4, 5, 6, 7]
    print(calculate_average(arr))

# Output:
# 3.0
# 3.5
# 4.0
