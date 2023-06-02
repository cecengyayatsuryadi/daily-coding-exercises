# find common elements
# language: Python


arr1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
arr2 = [2, 4, 6, 8, 10, 12, 14, 16, 18]


def find_common_elements(arr1, arr2):
    common_elements = []
    for i in arr1:
        if i in arr2:
            common_elements.append(i)
    return common_elements


print(find_common_elements(arr1, arr2))

# Output:
# [2, 4, 6, 8]
