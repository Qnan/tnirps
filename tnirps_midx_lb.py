######################################################################
## 
## Tnirps: Tuple-based multiindex implementation
## 
######################################################################
import tnirps_utils
utils = tnirps_utils

def make (iter):
    return tuple(iter)

def zero ():
    return ()

def eval (midx, vals):
    """ Multiindex is represented by a list of integers.
    
    """
    prod = 1
    for i in range(len(vals)):
        prod *= vals[i] ** midx[i]
    return prod

def tostr (midx):
    """ Multiindex is represented by a list of integers.
    
    """
    s = ''
    for i in range(len(midx)):
        if (midx[i] != 0):
            if s != '':
                s += ' '
            s += '<%i>' % i
            if (midx[i] != 1):
                s += '^' + str(midx[i])
    return s

def min (a, b):
    if not hasattr(a,'terms') and hasattr(b,'terms'):
        raise TypeError("Arguments should be of type Midx!")
    if len(a) != len(b):
        raise ValueError("Multiindices should have the same length!")
    return tuple((utils.min2(a[i],b[i]) for i in range(len(a))))
    
def isZero (m):
    for a in m:
        if a != 0:
            return False
    return True

def sub (m, d):
    if not hasattr(m,'terms') and hasattr(d,'terms'):
        raise TypeError("Arguments should be of type Midx!")
    if len(m) != len(d):
        raise ValueError("Multiindices should have the same length!")
    return tuple((m[i] - d[i] for i in range(len(d))))

if __name__=='__main__':
    tests = [
        [tostr((1,5,0,77,3)) == "<0> <1>^5 <3>^77 <4>^3", "tostr"],
        [eval((3,1,4,1,0,9,2),(2,7,1,8,2,8,1)) == 60129542144, "eval"],
        [min((3,1,4,1,5,9,2), (2,7,1,8,2,8,1)) == (2,1,1,1,2,8,1), "min"],
        [isZero((0,0,0)) and not isZero((0,1,0)), "isZero"],
        [sub((3,1,4,1,5,9,2), (2,7,1,8,2,8,1)) == (1,-6,3,-7,3,1,1), "sub"]
        ]
    utils.doTests(tests)