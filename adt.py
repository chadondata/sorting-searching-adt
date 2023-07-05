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
        return self.get_data() == other.get_data()
    
    def __gt__(self, other):
        return self.get_data() > other.get_data()
    
    def __str__(self):
        return str(self.get_data())
    
    