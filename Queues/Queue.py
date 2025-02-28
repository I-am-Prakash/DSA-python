class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class Queue:
    def __init__(self, value):
        new_node = Node(value)
        self.first = new_node
        self.last = new_node
        self.length = 1
    
    def print_queue(self):
        temp = self.first

        while temp is not None:
            print(temp.value)
            temp = temp.next
    
    def enqueue(self, value):
        # create new node
        new_node = Node(value)

        # edge case when queue is empty
        if(self.length == 0):
            self.first = new_node
            self.last = new_node
        else:
            # temp = self.last
            self.last.next = new_node
            self.last = new_node
        self.length+=1
    
    def dequeue(self):
        # Edge case
        # when Queue is empty
        if(self.length == 0):
            return None
        if(self.length == 1):
            self.first = None
            self.last = None
        else:
            temp = self.first
            self.first = self.first.next
            temp.next = None
        self.length -=1
        return temp
        
my_Queue = Queue(25)

my_Queue.enqueue(20)
my_Queue.enqueue(15)
my_Queue.enqueue(10)

# print("Before enqueuing the Que is:")
# my_Queue.print_queue()

# my_Queue.enqueue(5)

# print("After enqueuing the Que is:")
# my_Queue.print_queue()

print("Before dequeuing the Que is:")
my_Queue.print_queue()

my_Queue.dequeue()

print("After dequeuing the Que is:")
my_Queue.print_queue()