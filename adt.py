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
    
