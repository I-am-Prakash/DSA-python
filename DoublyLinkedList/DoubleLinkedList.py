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
    
    def printDLL(self):
        temp = self.head
        for _ in range(self.length):
            print(temp.value)
            temp = temp.next


    def append(self, value):
        new_node = Node(value)
        if(self.head is None):
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = self.tail.next
        self.length += 1
        return True

    def prepend(self, value):
        # Create new_node
        new_node = Node(value)
        # Edge cases
        # 1. when DLL is empty
        # 2. when DLL is having >1 element
        if(self.length == 0):
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
        self.length += 1
        return True


    def pop(self):

        if self.length == 0:
            return None
        temp = self.tail
        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            self.tail = self.tail.prev
            self.tail.next = None
            temp.prev = None
        self.length -= 1
        return temp

    def popFirst(self):
        # Edge Cases
        # 1. empty DLL
        # 2. only 1'le element
        # 3. >1 elements
        if(self.length == 0):
            return None
        temp = self.head
        if(self.length == 1):
            self.head = None
            self.tail = None
        else:
            self.head = self.head.next
            temp.next = None
            self.head.prev = None
        self.length -=1
        return temp


    def get(self, index):
        # get element at particular index
        # no direct Index - So traversing Strategy
        # 1. if index < 0.5*length -> traverse from head
        # 2. if index > 0.5*length -> traverse from tail

        # Edge case if index is outof DLL range -> return None
        if(index<0 or index >= self.length):
            return None

        if(index < (self.length/2)):
            temp = self.head
            for _ in range(index):
                temp = temp.next
        else:
            temp = self.tail
            for _ in range(self.length-1, index, -1):
                temp = temp.prev
        return temp

    def set_value(self, index, value):
        # use get to fetch node at given index
        # edge case -> if get return not None -> then update the value
        temp = self.get(index)
        if temp is not None:
            temp.value = value
            return True
        return False
        
    def insert(self, index, value):
        # edge case -> if index out of range => return None
        if(index < 0 or index > self.length):
            return False
        # if index = 0 => prepend
        if(index == 0):
            return self.prepend(value)
        # if index = length => append
        if(index == self.length):
            return self.append(value)
        else:
            # create new node
            new_node = Node(value)
            # get before Node of given index
            before = self.get(index-1)
            # get Node at given index
            after = before.next
            #  perform insert Operation - involves 4 links
            new_node.next = after
            new_node.prev = before
            before.next = new_node
            after.prev = new_node
            self.length += 1
        return True

    def remove(self, index):
        # edge case index should be within length of DLL
        if(index < 0 or index >= self.length):
            return None
        # if index = 0 use pop
        if(index == 0):
            return self.popFirst()
        if(index == self.length-1):
            return self.pop()
        else:
            # use get to get the Node at index
            
            # i can use 2 more pointers -> before and after and use them to remove node
            before = self.get(index-1)
            temp = before.next
            after = temp.next
            temp.next = None
            temp.prev = None
            before.next = after
            after.prev = before
            # I am going to use 1'le temp itself for removing the Node
            '''temp = self.get(index)
            temp.next.prev = temp.prev
            temp.prev.next = temp.next
            temp.next = None
            temp.prev = None'''
            self.length -=1
            return temp.value
        

my_DLL=  DoublyLinkedList(25)

my_DLL.append(20)
my_DLL.append(15)

# my_DLL.pop()
# my_DLL.prepend(30)
# my_DLL.popFirst()
# get_2 = my_DLL.get(2)
# get_neg_1 = my_DLL.get(-1)
# my_DLL.set_value(1, 21)
# print(my_DLL.insert(1, 22.5)) # True
# print(my_DLL.insert(5, 22.5)) # False
print("removed" ,my_DLL.remove(1))

print(my_DLL.printDLL())
# print(get_2.value)
# print(get_neg_1)




            

