class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None
        

class DoublyLinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next
        
    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
        self.length += 1
        return True

 
    # My - Logic
    def is_palindrome(self):
        # 2 pointer method - 1 start at first another starts at tail
        # while left < right
        
        leftN = self.head
        rightN = self.tail
        leftP =0
        rightP = self.length-1
        while(leftP < rightP):
            if(leftN.value != rightN.value):
                return False
            leftN = leftN.next
            leftP+=1
            rightN = rightN.prev
            rightP -=1
        return True

    # Actual easy logic is - you know number of iterations - always be floor division of length of DLL
    def is_palindrome_easy(self):
        leftN = self.head
        rightN = self.tail

        for _ in range(self.length // 2):
            if leftN.value != rightN.value:
                return False
            leftN = leftN.next
            rightN = rightN.prev
        return True



my_dll_1 = DoublyLinkedList(1)
my_dll_1.append(2)
my_dll_1.append(3)
my_dll_1.append(2)
my_dll_1.append(1)

print('my_dll_1 is_palindrome:')
print( my_dll_1.is_palindrome() )


my_dll_2 = DoublyLinkedList(1)
my_dll_2.append(2)
my_dll_2.append(3)

print('\nmy_dll_2 is_palindrome:')
print( my_dll_2.is_palindrome() )



"""
    EXPECTED OUTPUT:
    ----------------
    my_dll_1 is_palindrome:
    True

    my_dll_2 is_palindrome:
    False

"""

