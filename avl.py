#import random
#from tqdm import tqdm

class AVLNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        self.height = 1

class AVLTree:
    def __init__(self):
        self.root = None

    def insert(self, data):
        self.root = self.insert_recurse(self.root, data)

    def insert_recurse(self, root, data):
        if root == None:
            return AVLNode(data)
        
        if data > root.data:
            root.right = self.insert_recurse(root.right, data)
        else:
            root.left = self.insert_recurse(root.left, data)

        root.height = 1 + max(self.get_height(root.left), self.get_height(root.right))
        balance = self.get_balance(root)

        if balance > 1 and data < root.left.data:
            return self.rotate_right(root)
        
        if balance < -1 and data > root.right.data:
            return self.rotate_left(root)
        
        if balance > 1 and data > root.left.data:
            root.left = self.rotate_left(root.left)
            return self.rotate_right(root)
        
        if balance < -1 and data < root.right.data:
            root.right = self.rotate_right(self.right)
            return self.rotate_left(root)
        
        return root

    def get_height(self, root):
        if root == None:
            return 0
        
        return root.height
    
    def rotate_left(self, z):
        y = z.right
        t = y.left

        y.left = z
        z.right = t

        z.height = 1 + max(self.get_height(z.left), self.get_height(z.right))
        y.height = 1 + max(self.get_height(y.left), self.get_height(y.right))

        return y
    

    def rotate_right(self, z):
        y = z.left
        t = y.right

        y.right = z
        z.left = t

        z.height = 1 + max(self.get_height(z.left), self.get_height(z.right))
        y.height = 1 + max(self.get_height(y.left), self.get_height(y.right))

        return y
            

    def get_balance(self, root):
        if root == None:
            return 0
        
        return self.get_height(root.left) - self.get_height(root.right)

    def pre_order(self, root):
        if root == None:
            return
        
        print(f'{root.data}', end=' ')
        self.pre_order(root.left)
        self.pre_order(root.right)

def main():
    my_tree = AVLTree()
    my_tree.insert(5)
    my_tree.insert(7)
    my_tree.insert(9)
    my_tree.insert(11)
    my_tree.insert(3)
    my_tree.insert(1)

    my_tree.pre_order(my_tree.root)
"""
def main2():
    my_tree = AVLTree()
    for i in tqdm(range(10000000)):
        my_tree.insert(i)
    my_tree.pre_order(my_tree.root)
"""
main()
