# Abstract data types module

# Stack
# A specialized list
# Last in, First out (LIFO)
class Stack:
    def __init__(self):
        # Initialize empty list
        self.the_stack = []

    def push(self, item):
        self.the_stack.append(item)

    def pop(self):
        if self.is_empty():
            return None
        
        the_item = self.the_stack[-1]
        del self.the_stack[-1]
        return the_item
    
    def peek(self):
        if self.is_empty():
            return None
        
        return self.the_stack[-1]
    
    def size(self):
        return len(self.the_stack)
    
    def is_empty(self):
        return self.size() == 0
    

class Queue:
    def __init__(self):
        self.the_queue = []
    
    def enqueue(self, item):
        self.the_queue.append(item) # add to the back
    
    def size(self):
        return len(self.the_queue)
    
    def is_empty(self):
        return self.size() == 0
    
    def dequeue(self):
        if self.is_empty():
            return None
        
        item = self.the_queue.pop(0)
        return item
    
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
    
    def get_data(self):
        return self.data
    def get_next(self):
        return self.next
    def set_data(self, data):
        if data == None:
            return
        
        self.data = data
    def set_next(self, next):
        self.next = next

    def __eq__(self, other):
        if not isinstance(other, Node):
            return False
        
        return self.get_data() == other.get_data()
    
    def __gt__(self, other):
        if not isinstance(other, Node):
            return False

        return self.get_data() > other.get_data()
    
    def __str__(self):
        return str(self.get_data())
    
class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self._size = 0
    
    def append(self, data):
        # check for empty list
        if self.head == None:
            self.head = Node(data)
            self.tail = self.head 
            self._size = 1
            return
        
        self.tail.set_next(Node(data))
        self.tail = self.tail.get_next()
        self._size += 1
        
    def find(self, data):
        current = self.head
        while current != None and current.get_data() != data:
            current = current.get_next()
        
        return current != None
        # Change the Node class and this method to utilize
        # built in comparison
        # current != data instead of current.get_data() != data
        # Do this last!

    def size(self):
        return self._size

    def remove(self, data):
        # Oh no! this function is broken. Can you fix it?
        if self.head == None:
            return
        
        if self.head.get_data() == data:
            self.head = self.head.get_next()
            self.size -= 1
            return
        
        current = self.head
        while current.get_next() != None and current.get_next().get_data() != data:
            current = current.get_next()
        
        if current.get_next() != None:
            current.set_next(current.get_next().get_next())
            self.size -= 1
        