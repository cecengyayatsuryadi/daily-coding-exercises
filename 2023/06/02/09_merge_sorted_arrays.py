# merge sorted arrays
# language: Python


def merge_sorted_arrays(arr1, arr2):
    merged_array = []
    i = 0
    j = 0
    while i < len(arr1) and j < len(arr2):
        if arr1[i] <= arr2[j]:
            merged_array.append(arr1[i])
            i += 1
        else:
            merged_array.append(arr2[j])
            j += 1
    while i < len(arr1):
        merged_array.append(arr1[i])
        i += 1
    while j < len(arr2):
        merged_array.append(arr2[j])
        j += 1
    return merged_array


if __name__ == "__main__":
    arr1 = [1, 3, 5, 7, 9]
    arr2 = [2, 4, 6, 8, 10]
    print(merge_sorted_arrays(arr1, arr2))

    arr1 = [1, 3, 5, 7, 9, 11]
    arr2 = [2, 4, 6, 8, 10]
    print(merge_sorted_arrays(arr1, arr2))

    arr1 = [1, 3, 5, 7, 9]
    arr2 = [2, 4, 6, 8, 10, 12]
    print(merge_sorted_arrays(arr1, arr2))

# Output:
# [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
# [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 12]
