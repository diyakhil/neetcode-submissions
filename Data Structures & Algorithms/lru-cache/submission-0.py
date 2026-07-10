class Node:
    def __init__(self, data):
        self.data = data
        self.next = None  # Pointer to the next node
        self.prev = None  # Pointer to the previous node

class LRUCache:

    def __init__(self, capacity: int):
        self.store = {} #storing the value and node like a tuple (value, node)
        self.capacity = capacity

        self.head = Node(0)  # dummy head (least recently used end)
        self.tail = Node(0)  # dummy tail (most recently used end)
        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, key: int) -> int:
        if not self.store.get(key):
            return -1
        
        value, node = self.store[key]
        prev = node.prev
        _next = node.next

        prev.next = _next
        _next.prev = prev

        last_node = self.tail.prev

        node.prev = last_node
        node.next = self.tail

        self.tail.prev = node
        last_node.next = node

        return value

    def put(self, key: int, value: int) -> None:
        #now check if the value we want to put already exists in hashmap
        if not self.store.get(key):
            #ONLY DO THIS STEP IF THE KEY DOESN'T ALREADY EXIST OTHERWISE WE EVICT A NODE UNNECESSARILY
            #first take out the first node in linked list to increase capacity
            if len(self.store.keys()) >= self.capacity:
                first_node = self.head.next
                _next = first_node.next
                self.store.pop(first_node.data)
                
                self.head.next = _next
                _next.prev = self.head

                first_node.next = None
                first_node.prev = None

            #just add node to end of list, no need to remove anything
            new_node = Node(key)

            last_node = self.tail.prev
            new_node.prev = last_node
            new_node.next = self.tail
            self.tail.prev = new_node
            last_node.next = new_node

            self.store[key] = (value, new_node)
        else:
            node = self.store[key][1]
            prev = node.prev
            _next = node.next

            prev.next = _next
            _next.prev = prev

            last_node = self.tail.prev

            node.prev = last_node
            node.next = self.tail
            self.tail.prev = node
            last_node.next = node

            self.store[key] = (value, node)
