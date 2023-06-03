# Implement a Stack: Create a class that represents a stack data structure with methods like push(), pop(), and is_empty().


# Solution 1: Using a list
class Stack:
    def __init__(self):
        self.items = []  # Create an empty list

    def push(self, item):
        self.items.append(item)  # Add the item to the end of the list

    def pop(self):
        return self.items.pop()  # Remove and return the last item in the list

    def is_empty(self):
        return self.items == []  # Return True if the list is empty

    def peek(self):
        if not self.is_empty():
            return self.items[-1]  # Return the last item in the list
        return None

    def size(self):
        return len(self.items)  # Return the length of the list

    def clear(self):
        self.items = []  # Clear the list


# Test the Stack class
stack = Stack()

# Test the push() method
stack.push(1)
stack.push(2)
stack.push(3)

# Test the size() method
print(stack.size())

# Test the pop() method
print(stack.pop())
print(stack.pop())

# Test the peek() method
print(stack.peek())

# Test the is_empty() method
print(stack.is_empty())

# Test the clear() method
stack.clear()

# Test the is_empty() method
print(stack.is_empty())

# Output:
# 3
# 3
# 2
# 1
# False
# True
