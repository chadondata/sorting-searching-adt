import random
from tqdm import tqdm

class BSTNode:
    def __init__(self, data):
        if data == None:
            raise ValueError("parm data must have a value")

        self.data = data
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root = None
    
    def add(self, data):
        if data == None:
            raise ValueError("parm data must have a value")
        
        # If empty list, root is new node
        if self.root == None:
            self.root = BSTNode(data)
            return
        
        current = self.root
        while True:
            if data > current.data:
                # Go right
                if current.right == None:
                    current.right = BSTNode(data)
                    return
                else:
                    current = current.right
            else:
                # Go left
                if current.left == None:
                    current.left = BSTNode(data)
                    return
                else:
                    current = current.left

    def to_list(self):
        # In-order traversal
        the_list = []
        self.visit_subtree(self.root, the_list)
        return the_list

    def visit_subtree(self, start, the_list):
        if start.left != None:
            self.visit_subtree(start.left, the_list)
        
        the_list.append(start.data)

        if start.right != None:
            self.visit_subtree(start.right, the_list)
    
    def search(self, data):
        if self.root == None:
            return False
        
        current = self.root
        while True:
            if current.data == data:
                return True
            
            if data < current.data:
                current = current.left
            else:
                current = current.right
            
            if current == None:
                return False
        


def main():
    bst = BST()

    N = 100000

    for i in range(N):
        bst.add(random.randint(0, N*10))

    #print(bst.to_list())

    to_find = int(input("What to find? "))
    print(bst.search(to_find))

def new_main():
    bst = BST()

    N = 100000

    for i in tqdm(range(N)):
        bst.add(i)
    
    to_find = int(input("What to find? v2 "))
    print(bst.search(to_find))

main()
new_main()