
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class Stack:
    def __init__(self, value):
        new_node = Node(value)
        self.top = new_node
        self.height = 1

    def print_stack(self):
        temp = self.top
        while temp is not None:
            print(temp.value)
            temp=temp.next

    def push(self, value):
        # Create new node
        new_node = Node(value)
        # Edge cases
        # if Stack is Empty
        if self.height == 0:
            self.top = new_node
        else:
            new_node.next = self.top
            self.top = new_node
        self.height += 1
        return True
    
    def pop(self):
        # If Stack is Empty
        if self.height == 0:
            return None
        
        # if self.height == 1:
        #     self.top = None
    # the above cond check not req since 1 or >1 the below code will take care => since there is not pointer at tail or bottom
        else:
            temp = self.top
            self.top = self.top.next
            temp.next = None
        self.height -=1

my_stack = Stack(25)

my_stack.push(20)
my_stack.push(15)
my_stack.push(10)

# print('before pushing the stack is : ')
# my_stack.print_stack()

# my_stack.push(30)
# print('After pushing the stack is : ')
# my_stack.print_stack()


print('before Popping the stack is : ')
my_stack.print_stack()

my_stack.pop()

print('After Popping the stack is : ')
my_stack.print_stack()


        
        