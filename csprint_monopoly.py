######################################################################
## 
## CSprint: Monome and polynome implementation 
## 
######################################################################
class Monome:
    """
    Monome is represented by a coefficient and a multiindex.
    Multiindex is represented by a list.
    """
    def __init__ (self, coeff=1, midxs=[]):
        self.coeff = coeff
        self.midxs = midxs

    def evaluate (self, vals):
        prod = 1
        for i in range(len(vals)):
            prod *= vals[i] ** self.midxs[i]
        return prod

    def tostr (self):
        s = str(self.coeff)
        for i in range(len(self.midxs)):
            if (self.midxs[i] != 0):
                s += ' ' + varnames[i]
                if (self.midxs[i] != 1):
                    s += '^' + str(self.midxs[i])
        return s

class Polynome:
    """
    Polynome is defined as a list of monomes.
    """
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
    """
    Create a polynome from a simple list of (coeff, multiindex) paris.
    """
    p = Polynome()
    for nm in data:
        m = Monome(nm[0], nm[1])
        p.mons.append(m)
    return p

def polyToMonomes (poly):
    return [elem for elem in poly.mons]

if __name__=='__main__':
    raw = [
        [3,[2,0]],
        [2,[4,1]],
        [5,[0,2]],
        [17,[0,7]],
        [1,[0,3]],
        [21,[1,1]]]
    vals = [3,5]
    poly = makePolynome(raw)
    monomes = polyToMonomes(poly)
    polystr = poly.tostr()
    polystr_check = ""
    print(polystr)
    polyeval = poly.evaluate(vals)
    polyeval_check = 0
    print(polyeval)