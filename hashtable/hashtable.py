class HashTableEntry:
    """
    Linked List hash table key/value pair
    """
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None


# Hash table can't have fewer than this many slots
MIN_CAPACITY = 8

'''
def djb2(key):
  hash = 5381
  for c in key:
    hash = (hash * 33) + ord(c)
  return hash
'''

# this node class is replicated by the hastable entry class
class Node:
    def __init__(self,value):
        self.value = value
        self.next = None

# this linked list class is replicated by the hashtable class
class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self,value):
        pass

    def delete(self,value):
        pass


# just as a linked list class uses a node class, the hastable class
# uses a hashtableentry class
class HashTable:
    """
    A hash table that with `capacity` buckets
    that accepts string keys

    Implement this.
    """

    def __init__(self, capacity):
        self.capacity = capacity
        self.bucket_array = [None for i in range(capacity)]
        self.count = 0



    def get_num_slots(self):
        """
        Return the length of the list you're using to hold the hash
        table data. (Not the number of items stored in the hash table,
        but the number of slots in the main list.)

        One of the tests relies on this.

        Implement this.
        """
        return self.capacity


    def get_load_factor(self):
        """
        Return the load factor for this hash table.

        Implement this.
        """
        # Your code here
        return self.count / self.capacity  


    def fnv1(self, key):
        """
        FNV-1 Hash, 64-bit

        Implement this, and/or DJB2.
        """

        # Your code here


    def djb2(self, key):
        """
        DJB2 hash, 32-bit

        Implement this, and/or FNV-1.
        """
        # Your code here
        self.hash = 5381

        for c in key:
            self.hash = (self.hash * 33) + ord(c)

        return self.hash

    def hash_index(self, key):
        """
        Take an arbitrary key and return a valid integer index
        between within the storage capacity of the hash table.
        """
        #return self.fnv1(key) % self.capacity
        return self.djb2(key) % self.capacity

    def put(self, key, value):
        """
        Store the value with the given key.

        Hash collisions should be handled with Linked List Chaining.

        Implement this.
        """

        # Your code here
        i = self.hash_index(key)
        # self.bucket_array[i] = value

        # create a new hashnode
        new_entry = HashTableEntry(key,value)
        # mark the corresponding bucket as current hashnode
        cur = self.bucket_array[i]

        # if theres already an entry in this bucket
        if cur:
            last = None
            while cur:
                # if the key matches, replace the existing value
                if cur.key == key:
                    cur.value = value
                    self.count -= 1
                    return
                last = cur
                cur = cur.next

            last.next = new_entry

        else:
            self.bucket_array[i] = new_entry
        # add a counter
        self.count += 1

        # check load factor
        if self.get_load_factor() > 0.7:
            self.resize(self.capacity * 2)

    def delete(self, key):
        """
        Remove the value stored with the given key.

        Print a warning if the key is not found.

        Implement this.
        """
        # Your code here
        i = self.hash_index(key)
        cur = self.bucket_array[i]
        if cur:
            last = None
            while cur:
                # if the key matches, replace the existing value
                if cur.key == key:
                    # if last exists, then set last.next to cur.next
                    if last:
                        last.next = cur.next
                    # else set the bucket value to the next hashnode
                    # which will be checked next
                    else:
                        self.bucket_array[i] = cur.next
                    # add a counter
                    self.count -= 1
        
                last = cur
                cur = cur.next

        


    def get(self, key):
        """
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        Implement this.
        """
        # Your code here
        i = self.hash_index(key)

        # switch this to cur = self.bucket_array
        # then, need to define value. value = key?
        #return self.bucket_array[i]
        cur = self.bucket_array[i]
        if cur:
            while cur:
                if cur.key == key:
                    return cur.value
                    # check the next value
                cur = cur.next

        return None



    def resize(self, new_capacity):
        """
        Changes the capacity of the hash table and
        rehashes all key/value pairs.

        Implement this.
        """
        # Your code here
        #print(new_capacity)
        old_bucket_array = self.bucket_array
        old_count = self.count
        #new_ht = HashTable(new_capacity)
        self.capacity = new_capacity
        self.bucket_array = [None for i in range(new_capacity)]
        

        for x in old_bucket_array:
            cur = x
            while cur:
                self.put(cur.key,cur.value)
                # need to move to the next hashnode in the bucket
                cur = cur.next

        #print(new_ht.capacity)
        self.count = old_count
        #return new_ht
        
        



if __name__ == "__main__":
    ht = HashTable(8)

    ht.put("line_1", "'Twas brillig, and the slithy toves")
    ht.put("line_2", "Did gyre and gimble in the wabe:")
    ht.put("line_3", "All mimsy were the borogoves,")
    ht.put("line_4", "And the mome raths outgrabe.")
    ht.put("line_5", '"Beware the Jabberwock, my son!')
    ht.put("line_6", "The jaws that bite, the claws that catch!")
    ht.put("line_7", "Beware the Jubjub bird, and shun")
    ht.put("line_8", 'The frumious Bandersnatch!"')
    ht.put("line_9", "He took his vorpal sword in hand;")
    ht.put("line_10", "Long time the manxome foe he sought--")
    ht.put("line_11", "So rested he by the Tumtum tree")
    ht.put("line_12", "And stood awhile in thought.")

    print('load',ht.get_load_factor(),'count',ht.count)

    print("")

    # Test storing beyond capacity
    for i in range(1, 13):
        print(ht.get(f"line_{i}"))

    # Test resizing
    old_capacity = ht.get_num_slots()
    ht.resize(ht.capacity * 2)
    new_capacity = ht.get_num_slots()

    print(f"\nResized from {old_capacity} to {new_capacity}.\n")

    # Test if data intact after resizing
    for i in range(1, 13):
        print(ht.get(f"line_{i}"))

    print("")
