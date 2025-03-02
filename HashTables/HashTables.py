# a D.S => lookup -> O(1)
# 1. Built in -> Dictionary is Hash Table
# 
# What makes it unique ?
# 1. Has Hash function -> takes key -> returns index -> where to store
# 2. It's one way -> and Deterministic Process -> Always returns same index for the same key
# 3. different keys can result into same index - called Collision
#   a. chaining -> placing a list at that index and append all the items with that index
#   b. Linear Probing -> finding next open index - to get in =>called- Open Addressing
# 4. Create Hashtable of size - Prime number - for randomeness and -> proper distribution -> to reduce collisions
# 5. getting all the keys into a list
# 6. find a key that exists in the Hash Table or not


# Let's build our Hash Table

class HashTable:
    def __init__(self, size = 7):
        self.data_map = [None]*size
    
    def __hash(self,key):
        hash_index = 0
        for char in key:
            hash_index = (hash_index+ord(char))*23%(len(self.data_map))
        return hash_index
    
    def set(self, key, value):
        hash_index = self.__hash(key)
        if self.data_map[hash_index] ==None:
            self.data_map[hash_index] = []
            self.data_map[hash_index].append [key, value]

    def get(self, key, value):
        hash_index = self.__hash(key)
        if self.data_map[hash_index] ==None:
            self.data_map[hash_index] = []
            self.data_map[hash_index].append [key, value]

my_hash_table = HashTable()

my_hash_table.set('bolts', 400)
my_hash_table.set('washers ', 400)
my_hash_table.set('bolts', 400)

my_hash_table.print_table()