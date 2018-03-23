import random
import time


class Node:
    """
    Tree node: left child, right child and data
    """

    def __init__(self, l=None, r=None, p=None, d=None):
        """
        Node constructor
        @param A node data object
        """
        self.left = l
        self.right = r
        self.data = d
        self.parent = p


class Data:
    """
    Tree data: Any object which is used as a tree node data
    """

    def __init__(self, int_val, ascii_val):
        """
        Data constructor
        @param A list of values assigned to object's attributes
        """
        self.key = int_val
        self.charr = ascii_val


def addNode(root, node):
    if node.data.key >= root.data.key:
        node.parent = root
        root.right = node
    else:
        node.parent = root
        root.left = node


def printFun(n):
    print(n.left, n.right, n.parent, n.data.key, n.data.charr)


def InorderTreeWalk(n):
    if n != None:
        InorderTreeWalk(n.left)
        print(n.key)


d1 = Data(2, chr(2))
d2 = Data(3, chr(3))
d3 = Data(5, chr(5))

x = Node(None, None, None, d1)

y = Node(None, None, None, d2)

z = Node(None, None, None, d3)

addNode(x, y)
addNode(x, z)

printFun(x)
printFun(y)
printFun(z)


def random_list (min, max, elements):
    list = random.sample(range(min, max), elements)
    return list

l = random_list(1, 100, 50)

def foo(l):
    print("list: ", l)

start_time = time.clock()

#Blok Funkcije+---++++++++++++++----

def inOrderTreeWalk (varX):
    if varX is not None:
        inOrderTreeWalk(varX.left)
        print(varX.key)
        inOrderTreeWalk(varX.right)


def TreeSearch(varX,varK):
    if varX is None or varK == varX.key:
        return varX
    if varK < varX.key:
        return TreeSearch(varX.left,varK)
    else: return TreeSearch(varX.right,varK)

def IterativeTreeSearch(varX,varK):
    while varX is not None and varK!=varX.key:
        if varK<varX.key:
            varX=varX.left
        else: varX=varX.right
    return varX

def TreeMin(varX):
    while varX.left is not None:
        varX=varX.left
    return varX

def TreeMax(varX):
    while varX.right is not None:
        varX=varX.right
    return varX

def TreeSucc(varX):
    if varX.right is not None:
        return TreeMin(varX.right)
    varY=varX.p
    while varY is not None and varX==varY.right:
        varX=varY
        varY=varY.p
    return varY

def Tree_insert(T,z):
    y=None
    x=T.root
    while x!=None:
        y=x
        if z.key<x.key:
            x=x.left
        else:
            x=x.right
    z.p=y
    if y==None:
        T.root=z #Tree T was empty
    elif z.key<y.key:
        y.left=z
    else:
        y.right=z

def Tree_Delete(T,z):
    if z.left==None:
        Transplant(T,z,z.right)
    elif z.right==None:
        Transplant(T,z,z.left)
    else:
        y=TreeMin(z.right)
        if y.p!=z:
            Transplant(T,y,y.right)
            y.right=z.right
            y.right.p=y
        Transplant(T,z,y)
        y.left = z.left
        y.left.p=y

def Transplant(T,u,v):
    if u.p==None:
        T.root=v
    elif u==u.p.left:
        u.p.left=v
    else:
        u.p.right=v
    if v!= None:
        v.p=u.p



#Blok Funkcije

foo(l)

end_time = time.clock() - start_time
print("Duration: ", end_time)

