from tnirps_utils import cmpLex
import tnirps_recursive_split
import tnirps_utils; Utils = tnirps_utils
import tnirps_midx_lb; Midx = tnirps_midx_lb
from tnirps_monopoly import Polynome
from tnirps_monopoly import Monome
import math
import random

print(str([random.randint(0,1) for i in range(10)]))

def unique (list, func):
    ul = []
    lookup = []
    for el in list:
        f = func(el)
        if not (f in lookup):
            lookup.append(f)
            ul.append(el)
    return ul

#print(str(unique([8,1,2,5,1,4,5,6,2,3,4,5,1,3,4,5,1,5,3,2,4,7], lambda x: x)))        

#3, 0.05, 0.5, 0.001
def makeRandPoly(v, lengthFactor, presenceFactor, degreeFactor):
    n = math.ceil(random.expovariate(lengthFactor))
    data = [(1, [Utils.ifelse(random.random() < presenceFactor, math.ceil(random.expovariate(degreeFactor)), 0) for j in range(v)]) for i in range(n)]
    return unique(data, lambda el: el[1])    

#print(str(',\n'.join([str(el) for el in makeRandPoly(3, 0.05, 0.5, 0.001)])))

randraw = [(1, [0, 0, 943]),
            (1, [0, 0, 0]),
            (1, [498, 1292, 0]),
            (1, [302, 84, 103]),
            (1, [0, 222, 3899]),
            (1, [765, 890, 417]),
            (1, [582, 0, 2039]),
            (1, [0, 533, 0]),
            (1, [0, 0, 316]),
            (1, [0, 694, 0]),
            (1, [489, 0, 787]),
            (1, [0, 0, 979]),
            (1, [0, 0, 784]),
            (1, [3034, 0, 302]),
            (1, [0, 491, 1670]),
            (1, [666, 524, 0]),
            (1, [1790, 496, 0]),
            (1, [1635, 0, 0]),
            (1, [407, 593, 216]),
            (1, [0, 2132, 105]),
            (1, [0, 0, 2313]),
            (1, [411, 142, 0]),
            (1, [1330, 221, 0]),
            (1, [0, 263, 980])]

raw = (
    (3,(2,0)),
    (2,(4,1)),
    (5,(0,2)),
    (-17,(0,7)),
    (1,(0,3)),
    (21,(1,1)))

poly = Polynome(randraw)

print(poly)

mc = 0
for monome in poly.mons:
    for i in range(len(monome.midx)):
        if monome.midx[i] > 0:
            mc += math.ceil(math.log(monome.midx[i], 2))       
print('naive: {0}'.format(mc))


def monCmp (a,b):
    return cmpLex(a.midx, b.midx)
monomes = poly.toMonomes()
monomes.sort(key=Utils.cmpToKey(monCmp),reverse=True)
print(monomes)
tree = tnirps_recursive_split.monomesToTree(monomes)
tnirps_recursive_split.printTree(tree)
def nodeMultCount (data, subres):
#    print(str(data) + ' --- ' + str(type(data)))
    if isinstance(data, str):
        return sum(subres) + Utils.ifelse(data=='*', 1, 0)
    else:
        return sum([el and math.ceil(math.log(el, 2)) for el in data.midx])    
rcnt = tree.traverse(nodeMultCount)
print('tree: {0}'.format(rcnt))

vals = (1, 2)
def nodeEval (data, subres):
    if data == '+':
        return subres[0] + subres[1]
    elif data == '*':
        return subres[0] * subres[1]
    else:
        return data.evaluate(vals)
treeEval = tree.traverse(nodeEval)
print('tree  res: {0}'.format(treeEval))
print('naive res: {0}'.format(poly.evaluate(vals)))

print('Done')