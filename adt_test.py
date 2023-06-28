# Test routines for unit testing
# abstract data types. 

from adt import Stack
from adt import Queue

def test_stack():
    s = Stack()
    empty_item = s.pop()
    if empty_item == None:
        print("Empty stack pop works!")
    else:
        print("Empty stack pop failed!")
        exit(-1)
    
    s.push('bananas')
    print(s.peek())

    s.push('oranges')
    print(s.peek())

    print(s.pop())
    print(s.peek())

def test_queue():
    q = Queue()
    empty_queue = q.dequeue()
    if empty_queue == None:
        print("Empty queue test passed")
    else:
        print("Empty queue test failed")
        exit(-1)
    
    for i in range(10):
        q.enqueue(i)
    
    print(q.size())
    for j in range(q.size()):
        print(q.dequeue())


def test_main():
    r = ''
    while r != 'x':
        print('ADT Test')
        print('Select an option below:')
        print('1. Test Stack')
        print('2. Test Queue')
        print('x. Exit')
        r = input('Enter your choice: ')
        if r.isnumeric():
            selection = int(r)
            match selection:
                case 1:
                    test_stack()
                case 2:
                    test_queue()
                case _:
                    print("Not implemented")

if __name__ == '__main__':
    test_main()
    
