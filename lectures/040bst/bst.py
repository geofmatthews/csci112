## Based on https://www.geeksforgeeks.org/deletion-in-binary-search-tree/

class Node:
    def __init__(self, key, left=None, right=None):
        self.key = key
        self.left = left
        self.right = right

def printTree(node, indent = 0):
    if node is None:
        return
    printTree(node.right, indent+1)
    print('  '*indent, end='')
    print(node.key)
    printTree(node.left, indent+1)

def insert(node, key):
    if node is None:
        return Node(key)
    elif key < node.key:
        node.left = insert(node.left, key)
    elif key > node.key:
        node.right = insert(node.right, key)
    return node

def minValueNode(node):
    current = node
    while current.left is not None:
        current = current.left
    return current

def deleteNode(root, key):
    if root is None:
        return root
    if key < root.key:
        root.left = deleteNode(root.left, key)
    elif key > root.key:
        root.right = deleteNode(root.right, key)
    else:
        if root.left is None:
            temp = root.right
            root = None
            return temp
        elif root.right is None:
            temp = root.left
            root = None
            return temp
        temp = minValueNode(root.right)
        root.key = temp.key
        root.right = deleteNode(root.right, temp.key)
    return root
        

if __name__ == '__main__':
    root = None
    for i in [50,30,20,40,70,60,80]:
        root = insert(root, i)
        printTree(root)
        print('-'*40)
        
    for i in [50,30,20,40,70,60,80]:
        root = deleteNode(root, i)
        printTree(root)
        print('-'*40)

        
    
