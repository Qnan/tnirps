varnames = ['x','y','z']

class Monome:
    def __init__ (self):
        self.coeff = 1
        self.terms = []

    def evaluate (self, vals):
        prod = 1
        for i in range(len(vals)):
            prod *= vals[i] ** self.terms[i]
        return prod

    def tostr (self):
        s = str(self.coeff)
        for i in range(len(self.terms)):
            if (self.terms[i] != 0):
                s += ' ' + varnames[i]
                if (self.terms[i] != 1):
                    s += '^' + str(self.terms[i])
        return s

class Polynome:
    def __init__ (self):
        self.mons = []
    def evaluate (self, vals):
        t = 0
        for i in range(len(self.mons)):
            t += self.mons[i].evaluate(vals)
        return t
    def tostr (self):
        s = ""
        for i in range(len(self.mons)):
            if (s != ""):
                s += " + "
            s += self.mons[i].tostr()
        return s

def makePolynome (data):
    p = Polynome()
    for nm in data:
        m = Monome()
        m.coeff = nm[0]
        m.terms = nm[1]        
        p.mons.append(m)
    return p

def polyToMonomes (poly):
    return [elem.terms for elem in poly.mons]

def cmpLex (a, b):
    for i in range(len(a)):
        if a > b:
            return -1
        elif a < b:
            return 1
    return 0

def min2 (a,b):
    return (a < b and (a,) or (b,))[0]

def monomeMin (a, b):
    return [min2(a[i],b[i]) for i in range(len(a))]

def monomeIsZero (m):
    for a in m:
        if a != 0:
            return False
    return True

def monomeDiv (m, d):
    return [m[i] - d[i] for i in range(len(d))]
        
degs = [
    [1,[2,0]],
    [1,[4,1]],
    [1,[0,2]],
    [1,[0,7]],
    [1,[0,3]],
    [1,[1,1]]
    ]
vals = [3,5]
poly = makePolynome(degs)
#print(poly.tostr())
#print(poly.evaluate(vals))
monomes = polyToMonomes(poly)

print(str(monomes))
monomes.sort(cmp=cmpLex)
print(str(monomes))

def split (mons):
    mcm=mons[0]
    for i in range(len(mons)):
        m = monomeMin(mcm, mons[i])
        if monomeIsZero(m):
            return mcm, [monomeDiv(el, mcm) for el in mons[:i]], mons[i:]
        mcm = m
    return mcm, [monomeDiv(el, mcm) for el in mons], []

class TreeNode:
    def __init__ (self, data=None, children=[]):
        self.children = children
        self.data = data
    def traverse (self, func):
        return func(self.data, [child.traverse(func) for child in children])

def monomesToTree (monomes):
    if len(monomes) == 1:
        return TreeNode(monomes[0])
    else:
        children = []
        mcm, ml1, ml2 = split(monomes)
        if len(ml1) > 1:
            lnode = TreeNode('*', [TreeNode(mcm), monomesToTree(ml1)])
        else:
            lnode = TreeNode(mcm)
        if len(ml2) > 0:
            rnode = monomesToTree(ml2)
            return TreeNode('+', [lnode, rnode])
        else:
            return lnode

def printTree (tree, offset = 0):
    print('  ' * offset + str(tree.data))
    [printTree(child, offset + 1) for child in tree.children]

tree = monomesToTree(monomes)

printTree(tree)

print(str(split(monomes)))    
print('Done')