def count_character_frequency(string):
    frequency = {}
    for char in string:
        frequency[char] = frequency.get(char, 0) + 1
    return frequency


def print_character_frequency(frequency):
    sorted_frequency = sorted(frequency.items(), key=lambda x: x[1], reverse=True)
    for char, count in sorted_frequency:
        print(f"{char}: {count}")


# Main program
user_input = input("Enter a string: ")
frequency = count_character_frequency(user_input)
print_character_frequency(frequency)
