######################################################################
## 
## Tnirps: Tuple-based multiindex implementation
## 
######################################################################
import tnirps_utils
utils = tnirps_utils

varnames = ('x', 'y', 'z', 'v', 'w', 's', 't', 'r', 'p', 'q', 'h')

def make (iter):
    return tuple(iter)

def zero ():
    return ()

def eval (midx, vals):
    prod = 1
    for i in range(len(vals)):
        prod *= vals[i] ** midx[i]
    return prod

def varToStr (i):
    if varnames != None:
        return varnames[i]
    else:
        return '<{0}>'.format(i)

def tostr (midx):
    return ' '.join([varToStr(i) + utils.ifelse(midx[i] != 1, '^{0}'.format(midx[i]), '') 
                     for i in range(len(midx)) if midx[i] != 0])

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
        [tostr((1,5,0,77,3)) == "x y^5 v^77 w^3", "tostr"],
        [eval((3,1,4,1,0,9,2),(2,7,1,8,2,8,1)) == 60129542144, "eval"],
        [min((3,1,4,1,5,9,2), (2,7,1,8,2,8,1)) == (2,1,1,1,2,8,1), "min"],
        [isZero((0,0,0)) and not isZero((0,1,0)), "isZero"],
        [sub((3,1,4,1,5,9,2), (2,7,1,8,2,8,1)) == (1,-6,3,-7,3,1,1), "sub"]
        ]
    utils.doTests(tests)
