######################################################################
## 
## CSprint: List-based multiindex implementation
## 
######################################################################
from csprint_utils import *

class Midx:
    """ Multiindex is represented by a list of integers.

    """
    def __init__ (self, terms=[]):
        self.terms = terms
    def evaluate (self, vals):
        prod = 1
        for i in range(len(vals)):
            prod *= vals[i] ** self.terms[i]
        return prod
    def tostr (self):
        s = ''
        for i in range(len(self.terms)):
            if (self.terms[i] != 0):
                if s != '':
                    s += ' '
                s += '<%i>' % i
                if (self.terms[i] != 1):
                    s += '^' + str(self.terms[i])
        return s

def midxMin (a, b):
    if not hasattr(a,'terms') and hasattr(b,'terms'):
        raise TypeError("Arguments should be of type Midx!")
    if len(a.terms) != len(b.terms):
        raise ValueError("Multiindexes should have the same length!")
    return Midx([min2(a.terms[i],b.terms[i]) for i in range(len(a.terms))])

def midxIsZero (m):
    if not hasattr(m,'terms'):
        raise TypeError("Argument should be of type Midx!")
    for a in m.terms:
        if a != 0:
            return False
    return True

def midxSub (m, d):
    if not hasattr(m,'terms') and hasattr(d,'terms'):
        raise TypeError("Arguments should be of type Midx!")
    if len(m.terms) != len(d.terms):
        raise ValueError("Multiindexes should have the same length!")
    return Midx([m.terms[i] - d.terms[i] for i in range(len(d.terms))])

if __name__=='__main__':
    tests = [
        [len(Midx([2,4,8,16,32]).terms) == 5, "Midx.init"],
        [Midx([1,5,0,77,3]).tostr() == "<0> <1>^5 <3>^77 <4>^3", "Midx.tostr"],
        [Midx([3,1,4,1,0,9,2]).evaluate([2,7,1,8,2,8,1]) == 60129542144, "Midx.evaluate"],
        [midxMin(Midx([3,1,4,1,5,9,2]), Midx([2,7,1,8,2,8,1])).terms == [2,1,1,1,2,8,1], "midxMin"],
        [midxIsZero(Midx([0,0,0])) and not midxIsZero(Midx([0,1,0])), "midxIsZero"],
        [midxSub(Midx([3,1,4,1,5,9,2]), Midx([2,7,1,8,2,8,1])).terms == [1,-6,3,-7,3,1,1], "midxSub"]]
    doTests(tests)