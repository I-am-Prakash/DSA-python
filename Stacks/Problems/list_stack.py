class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        """Check if the stack is empty."""
        return len(self.items) == 0

    def push(self, item):
        """Add an item to the top of the stack."""
        self.items.append(item)

    def pop(self):
        """Remove and return the top item of the stack. Raise an error if the stack is empty."""
        if self.is_empty():
            raise IndexError("pop from empty stack")
        return self.items.pop()

    def peek(self):
        """Return the top item of the stack without removing it. Raise an error if the stack is empty."""
        if self.is_empty():
            raise IndexError("peek from empty stack")
        return self.items[-1]

    def size(self):
        """Return the number of items in the stack."""
        return len(self.items)


# Example usage:
if __name__ == "__main__":
    stack = Stack()
    stack.push(1)
    stack.push(2)
    stack.push(3)
    print("Stack:", stack.items)  # Output: Stack: [1, 2, 3]
    print("Top item:", stack.peek())  # Output: Top item: 3
    print("Popped item:", stack.pop())  # Output: Popped item: 3
    print("Stack after pop:", stack.items)  # Output: Stack after pop: [1, 2]
    print("Is stack empty?", stack.is_empty())  # Output: Is stack empty? False
    print("Stack size:", stack.size())  # Output: Stack size: 2



# Explanation:
# 1. __init__: Initializes an empty list to store stack items.
# 2. is_empty: Checks if the stack is empty.
# 3. push: Adds an item to the top of the stack.
# 4. pop: Removes and returns the top item of the stack. Raises an error if the stack is empty.
# 5. peek: Returns the top item without removing it. Raises an error if the stack is empty.
# 6. size: Returns the number of items in the stack.