######################################################################
## 
## CSprint: Common utilities
## 
######################################################################
varnames = ['x','y','z','w','v','s','p','q']

class TreeNode:
    """Abstract tree node with some data and arbitrary number of children.
    
    """
    def __init__ (self, data=None, children=[]):
        self.children = children
        self.data = data
    def traverse (self, func):
        return func(self.data, [child.traverse(func) for child in children])

def cmpLex (a, b):
    """
    Compare lists lexicographically. The lists must be of the same length!
    """
    if len(a) != len(b):
        raise ValueError("The arguments have different length!");
    for i in range(len(a)):
        if a > b:
            return -1
        elif a < b:
            return 1
    return 0

def min2 (a,b):
    """
    Take minimum of two arguments
    """
    return (a < b and (a,) or (b,))[0]

def max2 (a,b):
    """
    Take maximum of two arguments
    """
    return (a > b and (a,) or (b,))[0]
