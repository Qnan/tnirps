class Monome:
    def __init__ (self):
        self.degs = {}

    def evaluate (self, vals):
        prod = 1
        for var in self.degs.keys():
            prod *= vals[var] ** self.degs[var]
        return prod

    def tostr (self, coeff=""):
        s = coeff
        for var in self.degs.keys():
            if (s != ""):
                s += ' '
            s += str(var)
            if (self.degs[var] != 1):
                s += "^" + str(self.degs[var])
        return s

class NMonome:
    def __init__ (self):
        self.monome = Monome()
        self.coeff = 0

    def evaluate (self, vals):
        return self.monome.evaluate(vals) * self.coeff

    def tostr (self):
        return self.monome.tostr(str(self.coeff))

class Polynome:
    def __init__ (self):
        self.nmonomes = []
    def evaluate (self, vals):
        t = 0
        for nmonome in self.nmonomes:
            t += nmonome.evaluate(vals)
        return t
    def tostr (self):
        s = ""
        for nmonome in self.nmonomes:
            if (s != ""):
                s += " + "
            s += nmonome.tostr()
        return s

def makePolynome (data):
    p = Polynome()
    for nm in data:
        m = NMonome()
        m.coeff = nm[0]
        m.monome.degs = nm[1]        
        p.nmonomes.append(m)
    return p
        
degs = [[1,{'x':2}],[1,{'x':1,'y':1}],[1,{'y':2}]]
vals = {'x':3,'y':5}
poly = makePolynome(degs)
print(poly.tostr())
print(poly.evaluate(vals))
#print('Hello world')
#print(str(evaluatePolynome(degs, vals)))
