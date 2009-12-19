######################################################################
## 
## Tnirps: Monome and polynome implementation 
## 
######################################################################
import tnirps_utils; Utils = tnirps_utils
import tnirps_midx_lb; Midx = tnirps_midx_lb

class Monome:
    """Monome is represented by a coefficient and a multiindex.

    """
    def __init__ (self, coeff=1, midx=Midx.zero()):
        self.coeff = coeff
        self.midx = Midx.make(midx)
    def evaluate (self, vals):
        return self.coeff * Midx.eval(self.midx, vals)
    def tostr (self, inExpr=False):
        c = self.coeff
        s = ''
        if inExpr:
            s += ' ' + (c < 0 and '-' or '+') + ' '
            c = abs(c)
        isZero = Midx.isZero(self.midx)
        if c != 1 or isZero:
            s += str(c)
            if not isZero:
                s += ' '
        s += Midx.tostr(self.midx)
        return s        
    def __repr__ (self):
        return self.tostr()    

class Polynome:
    """Polynome is defined as a list of monomes.

    """
    def __init__ (self, data=[]):
        self.mons = [Monome(nm[0], nm[1]) for nm in data]
    def evaluate (self, vals):
        t = 0
        for i in range(len(self.mons)):
            t += self.mons[i].evaluate(vals)
        return t
    def tostr (self):
        s = ""
        for i in range(len(self.mons)):
            s += self.mons[i].tostr(s != "")
        return s
    def __repr__ (self):
        return self.tostr()    
    def toMonomes (self):
        return [elem for elem in self.mons]

if __name__=='__main__':
    raw = (
        (3,(2,0)),
        (2,(4,1)),
        (5,(0,2)),
        (-17,(0,7)),
        (1,(0,3)),
        (21,(1,1)))
    vals = (3,5)
    poly = Polynome(raw)
    monomes = poly.toMonomes()
    tests = [
        [poly.tostr() ==
         "3 x^2 + 2 x^4 y + 5 y^2 - 17 y^7 + y^3 + 21 x y",
         "Polynome.tostr"],
        [poly.evaluate(vals) == -1326723, "Polynome.evaluate"]]
    Utils.doTests(tests)