# 1. create Node class => needed when writing insert method
    # a. It has Value
    # b. left pointer
    # c. right pointer
# 2. BST-> Has root Node and -> can be None -> no need to intialize it with some value
    # a. so constructor won't call Node 
# 3. Write BST constructor -> root -> None
# 4. Write helper methods for BST
    # a. Insert method
    # b. Contains method

class Node:
    def __init__(self, value):
        self.value = value
        self.left  = None
        self.right = None

class BinarySearchtree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        '''
        # Algorithm for insert Operation for BST

        1. create new node
        2. edge case -1 :- if root -> None => root = new_node => return False
        3. Don't know how many Nodes exist in tree -> so using -> while Loop -> make it run infinite
            a. But exit while loop using return statements
        4. make temp = root => for traversing -> helps finding the correct position for new_node
        5. Edge case -2 :- if same element already exist in tree -> return False
        6. since BST 
            a. -> Node value less than root ->goes -> left side
            b. -> Node value greater than root ->goes -> right side
        7. if temp becomes None -> somewhere in process -> will insert there
        '''

        new_node = Node(value)
        if self.root == None:
            self.root = new_node
            return True
        temp = self.root

        while True:
            if(new_node.value < temp.value):
                if(temp.left == None):
                    temp.left = new_node
                    return True
                temp = temp.left
            elif(new_node.value > temp.value):
                if(temp.right == None):
                    temp.right = new_node
                    return True
                temp = temp.right
            else:
                return False
            
    def contain(self, value):
        '''
        # Algorithm to find a value in BST
        1. Edge case -1 => if BST is empty -> return False
        2. temp = root -> for traversing tree and find matched value or no
        3. since BST 
          a. given value < root -> travels left
          b. given value > root -> travels right
          c. if matched -> return True

        ''' 
        if self.root == None :
            return False
        temp = self.root

        while temp is not None:
            if(value < temp.value):
                temp = temp.left
            elif(value > temp.value):
                temp = temp.right
            else:
                return True
        return False


            
            
my_bst = BinarySearchtree()

my_bst.insert(47)
my_bst.insert(21)
# my_bst.insert(21)
my_bst.insert(52)

print(my_bst.root.value)
print(my_bst.root.left.value)
print(my_bst.root.right.value)

print(my_bst.contain(21))
print(my_bst.contain(17))


