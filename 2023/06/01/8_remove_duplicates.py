# remove duplicates
# language: Python


list = input("Enter a list: \n")
list = list.split()


def remove_duplicates(list):
    new_list = []
    for i in list:
        if i not in new_list:
            new_list.append(i)
    return new_list


print(remove_duplicates(list))

# output:
# Enter a list:
# 1 2 3 4 5 6 7 8 9 10 1 2 3 4 5
# ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']
