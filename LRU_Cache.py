class Node:         # sc is o(capacity)
    def __init__(self, key, value):
        self.key = key
        self.val = value
        self.pre = None
        self.next = None
        
class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.d = {}
        self.head = self.tail = Node(0, 0)
        self.head.next, self.tail.pre = self.tail, self.head
               
    def get(self, key: int) -> int: # tc is o(1)
        if key in self.d:
            node = self.d[key]
            self.rm(node)
            self.inst(node)
            return node.val
        return -1

    def put(self, key: int, value: int) -> None:  # tc is o(1)
        if key in self.d: self.rm(self.d[key])
        node = Node(key, value)
        self.inst(node)
        self.d[key] = node
        if len(self.d) > self.capacity:
            node = self.head.next
            self.rm(node)
            del self.d[node.key]
           
    def rm(self, node):                                       # remove node
        node.pre.next, node.next.pre = node.next, node.pre

    def inst(self, node):                                     # add node in the tail
        self.tail.pre.next, node.next = node, self.tail
        self.tail.pre, node.pre = node, self.tail.pre
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
