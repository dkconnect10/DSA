# ===================================================
#  Objective: Assignment 20: Binary Search Tree Part-1
# ===================================================
'''
 1. Define a class Node with instance variables left, item, and right.
    The variables left and right are used to refer left and right child node.
    The item variable is used to hold data item.

 2. Define a class BST to implement Binary Search Tree data structure.
    Make __init__() method to create root instance variable 
    to hold the reference of root node.

 3. In class BST, define insert method to store new data item 
    in the binary search tree.

 4. In class BST, define a search method to find a given item 
    in the binary search tree and return the node reference.
    It should return None if search failed.

 5. In class BST, define a method to implement inorder traversal.

 6. In class BST, define a method to implement preorder traversal.

 7. In class BST, define a method to implement postorder traversal.

'''



class Node:
    def __init__(self, item=None, left=None, right=None):
        self.item = item
        self.left = left
        self.right = right


class BST:
    def __init__(self):
        self.root = None

    def insert(self, data):
        self.root = self.rinsert(self.root, data)

    def rinsert(self, root, data):
        if root is None:
            return Node(data)
        if data < root.item:
            root.left = self.rinsert(root.left, data)
        elif data > root.item:
            root.right = self.rinsert(root.right, data)
        return root

    def search(self, data):
        return self.rsearch(self.root, data)

    def rsearch(self, root, data):
        if root is None or root.item == data:
            return root
        if data < root.item:
            return self.rsearch(root.left, data)
        return self.rsearch(root.right, data)

    def inorder(self):
        result = []
        self.rinorder(self.root, result)
        return result

    def rinorder(self, root, result):
        if root:
            self.rinorder(root.left, result)
            result.append(root.item)
            self.rinorder(root.right, result)

    def preorder(self):
        result = []
        self.rpreorder(self.root, result)
        return result

    def rpreorder(self, root, result):
        if root:
            result.append(root.item)
            self.rpreorder(root.left, result)
            self.rpreorder(root.right, result)

    def postorder(self):
        result = []
        self.rpostorder(self.root, result)
        return result

    def rpostorder(self, root, result):
        if root:
            self.rpostorder(root.left, result)
            self.rpostorder(root.right, result)
            result.append(root.item)


bst = BST()
bst.insert(50)
bst.insert(30)
bst.insert(70)
bst.insert(20)
bst.insert(40)
bst.insert(60)
bst.insert(80)

print("Inorder:", bst.inorder())    # [20, 30, 40, 50, 60, 70, 80]
print("Preorder:", bst.preorder())  # [50, 30, 20, 40, 70, 60, 80]
print("Postorder:", bst.postorder())# [20, 40, 30, 60, 80, 70, 50]

found = bst.search(60)
print("Search 60:", "Found" if found else "Not Found")
