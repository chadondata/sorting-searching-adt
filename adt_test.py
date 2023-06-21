# Test routines for unit testing
# abstract data types.

from adt import Stack

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

def test_main():
    r = ''
    while r != 'x':
        print('ADT Test')
        print('Select an option below:')
        print('1. Test Stack')
        print('x. Exit')
        r = input('Enter your choice: ')
        if r.isnumeric() and int(r) == 1:
            test_stack()

if __name__ == '__main__':
    test_main()
    
