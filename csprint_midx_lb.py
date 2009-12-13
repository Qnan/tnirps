######################################################################
## 
## CSprint: List-based multiindex implementation
## 
######################################################################
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
        s = str(self.coeff)
        for i in range(len(self.terms)):
            if (self.terms[i] != 0):
                s += ' <%i>' % i
                if (self.terms[i] != 1):
                    s += '^' + str(self.terms[i])
        return s

def midxMin (a, b):
    return [min2(a[i],b[i]) for i in range(len(a))]

def midxIsZero (m):
    for a in m:
        if a != 0:
            return False
    return True

def midxSub (m, d):
    return [m[i] - d[i] for i in range(len(d))]

if __name__=='__main__':
    print('Here should be some tests')