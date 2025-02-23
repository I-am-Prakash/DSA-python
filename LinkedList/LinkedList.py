class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def print_list(self):
        temp = self.head
        count = 1
        print(f"Values in Linked List are: ")
        while temp is not None:
            print(f"Node ->{count} =>{temp.value}")
            temp = temp.next
            count+=1
        print(f"current length of Linked List : {self.length}")

    def append(self, value):
        new_node = Node(value)

        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = self.tail.next
        self.length+=1
        return True
    
    def pop(self): 
        # 3 - Edge cases we need write code for
        
        temp = self.head
        prev = self.head
        #1 : empty Linked List
        if(self.length == 0):
            return None
        #2 : 2 or more Items - general case
        while temp.next is not None:
            prev = temp
            temp = temp.next
        self.tail = prev
        self.tail.next = None
        self.length -=1
        #3 : only 1 item => still head and tail points to 1st node -> as while loop is not executed
        if(self.length == 0):
            self.head = None
            self.tail = None
        return temp
    
    def prepend(self, value):
        # create node 
        new_node = Node(value)

        #if empty 
        if(self.length == 0):
            self.head = new_node
            self.tail = new_node
        #1 or > elements
        else:
            new_node.next = self.head
            self.head = new_node
        self.length +=1

        return True

    def popFirst(self):
        #if empty list
        if(self.length == 0):
            return None
        #if >1 element
        else:
            temp = self.head
            self.head = self.head.next
            temp.next = None
        
        self.length-=1
        #if only 1 element
        if self.length == 0:
            self.tail = None
        return True

    def get(self, index):
        #edge cases
        # Make sure Index is within Range
        #some one send index => -ve values
        # index > length of Linked list 
        if(index < 0 or index >= self.length):
            return None
        temp = self.head
        for _ in range(index):
            temp = temp.next
        return temp

    def set_value(self, index, value):
        '''===========Actual Logic from scratch ===================
        
        # cover edge cases - Index should be Within Range
        if(index < 0 or index >= self.length):
            return None

        # create temp variable to store head => and use it for Traversing through the Linked list
        temp = self.head

        # iterate the temp until you reach node at given index
        for _ in range(index):
            temp = temp.next
        # after end of iteration now temp stands at correct index node position
        # now change update it's value
        temp.value = value
        return True
        '''

        #use get method to get the node at particular index
        temp = self.get(index)
        # check if temp is None 
        if temp:
            temp.value = value
            return True
        return False

    def insert(self, index, value):
        #Cover Edge cases like - empty Linked list and index within range
        # use proper methods which already exist
        # use get method to get node at particular index
        if(index < 0 or index > self.length):
            return False
        if(index==0):
            return self.prepend(value)
        if(index == self.length):
            return self.append(value)
        #not in the above cases - then index in middle 
        #1. create new node
        #2. get the prev node
        #3. map the relation - for inserting new node at given index
        #4. return True
        temp = self.get(index-1)
        new_node = Node(value)
        if temp:
            new_node.next = temp.next
            temp.next = new_node
            self.length +=1
            return True
        return False

    def remove(self, index):
        # cover all edge case
        # use already avail methods to solve this 

        # check if index within range otherwise return None -> bcz this method returns node an object/null
        if(index < 0  or index >= self.length):
            return None
        
        #check if removing index at first or last
        if(index == 0):
            return self.popFirst()
        if(index == self.length-1):
            return self.pop()
        
        #no above case :  then Index at middle
        prev = self.get(index-1)
        temp = prev.next
        prev.next = temp.next
        temp.next = None
        self.length -= 1
        return temp

    def reverse(self):
        #if empty linked list
        if(self.length == 0):
            return None
        # first head and tail switched
        temp = self.head
        self.head = self.tail
        self.tail = temp

        # using 3 variables will move pointer in reverse direction
        after = temp.next   
        prev = None
        for _ in range(self.length):
            after = temp.next
            temp.next = prev
            prev = temp
            temp = after
        return True


my_linked_list = LinkedList(3)
my_linked_list.append(5)
my_linked_list.append(7)



print(my_linked_list.print_list())

# pop_element = my_linked_list.pop()
# print("After Popping last element : ")
# print(my_linked_list.print_list())

# my_linked_list.prepend(pop_element.value)
# print("After pre-pending last element : ")
# print(my_linked_list.print_list())

# print(f"The value at index 2 is: {my_linked_list.get(2).value}")

# my_linked_list.set_value(2, 10)

# print(f"After setting value at index 2 : {my_linked_list.get(2).value}")
# print(my_linked_list.print_list())

#Insert
my_linked_list.insert(2, 20)
print(my_linked_list.print_list())

#Remove
my_linked_list.remove(2)
print(my_linked_list.print_list())

#Reverse
my_linked_list.reverse()
print(f"After Reversing the Linked List : ")
my_linked_list.print_list()

