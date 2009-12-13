######################################################################
## 
## CSprint: Monome and polynome implementation 
## 
######################################################################
from csprint_utils import *
from csprint_midx_lb import Midx

class Monome:
    """Monome is represented by a coefficient and a multiindex.

    """
    def __init__ (self, coeff=1, midx=Midx()):
        self.coeff = coeff
        self.midx = midx
    def evaluate (self, vals):
        return self.coeff * self.midx.evaluate(vals)
    def tostr (self):
        return '%i %s' % (self.coeff, self.midx.tostr())

class Polynome:
    """Polynome is defined as a list of monomes.

    """
    def __init__ (self, data=[]):
        self.mons = [Monome(nm[0], Midx(nm[1])) for nm in data]
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
    def toMonomes (poly):
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
    poly = Polynome(raw)
    monomes = poly.toMonomes()
    tests = [
        [poly.tostr() ==
         "3 <0>^2 + 2 <0>^4 <1> + 5 <1>^2 + 17 <1>^7 + 1 <1>^3 + 21 <0> <1>",
         "Polynome.tostr"],
        [poly.evaluate(vals) == 1329527, "Polynome.evaluate"]]
    doTests(tests)