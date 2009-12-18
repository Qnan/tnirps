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
        if inExpr:
            return ' {0} {1} {2}'.format(self.coeff < 0 and '-' or '+', abs(self.coeff), Midx.tostr(self.midx))
        else:
            return '{0} {1}'.format(self.coeff, Midx.tostr(self.midx))
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

print(Polynome(((1, (2,0)), (-2, (1,1)), (1, (0,2)))))

if __name__=='__main__':
    raw = (
        (3,(2,0)),
        (2,(4,1)),
        (5,(0,2)),
        (17,(0,7)),
        (1,(0,3)),
        (21,(1,1)))
    vals = (3,5)
    poly = Polynome(raw)
    monomes = poly.toMonomes()
    tests = [
        [poly.tostr() ==
         "3 <0>^2 + 2 <0>^4 <1> + 5 <1>^2 + 17 <1>^7 + 1 <1>^3 + 21 <0> <1>",
         "Polynome.tostr"],
        [poly.evaluate(vals) == 1329527, "Polynome.evaluate"]]
    Utils.doTests(tests)
