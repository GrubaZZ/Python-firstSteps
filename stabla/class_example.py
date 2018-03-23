import random


class Node:
    """
    Tree node: left child, right child and data
    """

    def __init__(self, p=None, l=None, r=None, d=None):
        """
        Node constructor
        @param A node data object
        """
        self.parent = p
        self.left = l
        self.right = r
        self.data = d


class Data:
    """
    Tree data: Any object which is used as a tree node data
    """

    def __init__(self, val1, val2):
        """
        Data constructor
        @param A list of values assigned to object's attributes
        """
        self.a1 = val1
        self.a2 = val2


def add_1(root, n):
    if root.data.a1 > n.data.a1:
        root.left = n
    else:
        root.right = n
    n.left = None
    n.right = None


"""
def add_2(root, n1, n2):
    if root.data>n1.data:
        root.left=n1
    else if root.data<n1.data:
        root.right=n1
    if root.data>n1.data:
        root.left=n1
    else if root.data<n1.data:
        root.right=n1
"""


def add(self, val, node):
    if (val < node.data.a1):
        if (node.left != None):
            self._add(val, node.l)
        else:
            node.left = Node(val)
    else:
        if (node.right != None):
            self.add(val, node.right)
        else:
            node.right = Node(val)


def inordered_tree_walk(x):
    if x != None:
        inordered_tree_walk(x.left)
        print("(Inordered tree order) Data: ", x.data.a1)
        inordered_tree_walk(x.right)


def tree_search(x, k):
    if x == None or k == x.data.a1:
        return x
    if k <= x.data.a1:
        return tree_search(x.left, k)
    else:
        return tree_search(x.right, k)


def iterative_tree_search(x, k):
    while x != None and k != x.data.a1:
        if k < x.data.a1:
            x = x.left
        else:
            x = x.right
    return x


def tree_minimum(x):
    while x.left != None:
        x = x.left
    return x


def tree_maximum(x):
    while x.right != None:
        x = x.right
    return x


def tree_succesor(x):
    if x.right != None:
        return tree_minimum(x.right)
    y = x.p
    while y != None and x == y.right:
        x = y
        x = y.p
    return y


def tree_succesor(x):
    if x.right != None:
        return tree_minimum(x.right)
    y = x.p
    while y != None and x == y.right:
        x = y
        y = y.p
    return y


def tree_insert(T, z):
    y = None
    x = T.parent
    while x != None:
        y = x
        if z.data < x.data:
            x = x.left
        else:
            x = x.right
    z.p = y
    if y == None:
        T.root = z
    elif z.data < y.data:
        y.left = z
    else:
        y.right = z


def tree_Delete(T, z):
    if z.left == None:
        transplant(T, z, z.right)
    elif z.right == None:
        transplant(T, z, z.left)
    else:
        y = tree_minimum(z.right)
        if y.p != z:
            transplant(T, y, y.right)
            y.right = z.right
            y.right.p = y
        transplant(T, z, y)
        y.left = z.left
        y.left.p = y


def transplant(T, u, v):
    if u.p == None:
        T.root = v
    elif u == u.p.left:
        u.p.left = v
    else:
        u.p.right = v
    if v != None:
        v.p = u.p


# def random_list (min, max, elements):
#    list = random.sample(range(min, max), elements)
#    return list

if __name__ == "__main__":
    d1 = Data(1, 2)
    d2 = Data(2, 3)
    d3 = Data(3, 3)
    d4 = Data(4, 3)

    n1 = Node(None, None, None, d1)
    n2 = Node(None, None, None, d2)
    n3 = Node(None, None, None, d3)
    n4 = Node(None, None, None, d4)

    # l1=[]
    # l2=random_list(1, 100, 10)

    add_1(n2, n1)
    add_1(n2, n3)

    print("Printing inordered tree: ")
    inordered_tree_walk(n2)
    print("Searching for 3 and found: ", tree_search(n2, 3).data.a1)
    print("Iterative searching for 3 and found: ", iterative_tree_search(n2, 3).data.a1)
    print("Searching for minimum and found: ", tree_minimum(n2).data.a1)
    print("Searching for maximum and found: ", tree_maximum(n2).data.a1)
    # print("Searching for maximum and found: ", succesor(n2).data.a1)
    print("Inserting 4! ")
    tree_insert(n3, n4)
    print("Printing inordered tree with added 4: ")
    inordered_tree_walk(n2)

    # print("Data of root: ", n2.data.a1, "Data of left child: ", n2.left.data.a1, "Data of right child: ", n2.right.data.a1)