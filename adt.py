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
    
class LinkedList:
    def __init__(self):
        self.head = None
    
    def append(self, data):
        # check for empty list
        if self.head == None:
            self.head = Node(data)
            return
        
        current = self.head
        while current.get_next() != None:
            current = current.get_next()
        current.set_next(Node(data))
        # Modify this class and function to be O(1)
        # ( It's currently O(N) )

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
        count = 0
        current = self.head
        while current != None:
            count += 1
            current = current.get_next()
        
        return count
    # Challenge! Change the class and this method to 
    # make this function O(1). It's currently O(N)

    def remove(self, data):
        if self.head == None:
            return
        
        if self.head.get_data() == data:
            self.head = self.head.get_next()
        
        current = self.head
        while current.get_next() != None and current.get_next().get_data() != data:
            current = current.get_next()
        
        if current.get_next() != None:
            current.set_next(current.get_next().get_next())
        