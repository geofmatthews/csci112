## Based on https://en.wikipedia.org/wiki/Binary_search_tree

class Node:
    def __init__(self, key, left=None, right=None):
        self.key = key
        self.left = left
        self.right = right
        self.parent = None


def printTree(node, indent = 0):
    if node is None:
        return
    printTree(node.right, indent+1)
    print('  '*indent, end='')
    print(node.key)
    printTree(node.left, indent+1)

def search(x, key):
    while x is not None and key != x.key:
        if key < x.key:
            x = x.left
        else:
            x = x.right
    return x

def succ(x):
    if x is None:
        return None
    if x.right is not None:
        return minimum(x.right)
    y = x.parent
    while y is not None and x == y.right:
        x,y = y,y.parent
    return y

def minimum(x):
    while x.left is not None:
        x = x.left
    return x

def insert(T, z):
    z = Node(z)
    if T is None:
        return z
    y = None
    x = T
    while x is not None:
        y = x
        if z.key < x.key:
            x = x.left
        elif z.key > x.key:
            x = x.right
    z.parent = y
    if y is None:
        return z
    elif z.key < y.key:
        y.left = z
    elif z.key > y.key:
        y.right = z
    return T

def shift(T, u, v):
    if u.parent is None:
        T = v
    elif u == u.parent.left:
        u.parent.left = v
    else:
        u.parent.right = v
    if v is not None:
        v.parent = u.parent
    return T

def deleteNode(T, key):
    D = search(T, key)
    if D is None:
        return T
    if D.left is None:
        T = shift(T, D, D.right)
    elif D.right is None:
        T = shift(T, D, D.left)
    else:
        E = succ(D)
        if E.parent != D:
            T = shift(T, E, E.right)
            E.right = D.right
            E.right.parent = E
        T = shift(T, D, E)
        E.left = D.left
        E.left.parent = E
    return T

if __name__ == '__main__':
    root = None
    for i in [50,30,20,40,70,60,80]:
        root = insert(root, i)
        printTree(root)
        print('-'*40)

    print(search(root, 80).key)
    print('-'*40)
    for i in [50,30,20,40,70,60,80]:
        root = deleteNode(root, i)
        printTree(root)
        print('-'*40)
        
        
    
