######################################################################
## 
## Tnirps: Common utilities
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
        return func(self.data, [child.traverse(func) for child in self.children])

def cmpLex (a, b):
    """
    Compare lists lexicographically. The lists must be of the same length!
    """
    if len(a) != len(b):
        raise ValueError("The arguments have different length!");
    for i in range(len(a)):
        if a[i] > b[i]:
            return 1
        elif a[i] < b[i]:
            return -1
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

def doTests (tests):
    testcnt = 0
    for test in tests:
        if not test[0]:
            print('%s failed' % test[1])
            testcnt += 1
        else:
            print('%s succeeded' % test[1])
    if testcnt > 0:
        print('%i of %i tests failed!' % (testcnt, len(tests)))
    else:
        print('Well done!')

if __name__=='__main__':
    tests = [
        [len(TreeNode('', [1,2,3]).children) == 3, "TreeNode init"],
        [cmpLex([7,5],[5,7]) > 0 and cmpLex([0,0],[0,2]) < 0 and cmpLex([],[]) == 0, "cmpLex"],
        [min2(3.141, 2.718) == 2.718, "min2"],
        [max2(42, 24) == 42, "max2"]]
    doTests(tests)
