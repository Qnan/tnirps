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
    if len(a) != len(b):
        raise ValueError("Multiindices should have the same length!")
    return tuple((utils.min2(a[i],b[i]) for i in range(len(a))))
    
def isZero (m):
    for a in m:
        if a != 0:
            return False
    return True

def cmp (a, b):
    """ Check whether b divides a or vice versa.
    
    Returns
         1 if a >= b
        -1 if b > a
         0 otherwise
    """
    if len(a) != len(b):
        raise ValueError("Multiindices should have the same length!")
    mn, mx = 0, 0
    for i in range(len(a)):
        v = a[i] - b[i]
        if mn > v: mn = v
        if mx < v: mx = v
    if mn == 0:
        return 1
    if mx == 0:
        return -1
    return 0

def sub (m, d):
    if len(m) != len(d):
        raise ValueError("Multiindices should have the same length!")
    return tuple((m[i] - d[i] for i in range(len(d))))

if __name__=='__main__':
    tests = [
        [tostr((1,5,0,77,3)) == "x y^5 v^77 w^3", "tostr"],
        [eval((3,1,4,1,0,9,2),(2,7,1,8,2,8,1)) == 60129542144, "eval"],
        [min((3,1,4,1,5,9,2), (2,7,1,8,2,8,1)) == (2,1,1,1,2,8,1), "min"],
        [isZero((0,0,0)) and not isZero((0,1,0)), "isZero"],
        [sub((3,1,4,1,5,9,2), (2,7,1,8,2,8,1)) == (1,-6,3,-7,3,1,1), "sub"],
        [cmp((1,2,3), (1,3,4)) == -1, "cmp 1"],
        [cmp((1,2,3), (1,1,2)) ==  1, "cmp 2"],
        [cmp((1,2,3), (1,2,3)) ==  1, "cmp 3"],
        [cmp((1,2,3), (2,1,3)) ==  0, "cmp 1"],
        ]
    utils.doTests(tests)
