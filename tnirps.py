from tnirps_utils import cmpLex
import tnirps_recursive_split
import tnirps_utils; Utils = tnirps_utils
import tnirps_midx_lb; Midx = tnirps_midx_lb
from tnirps_monopoly import Polynome
from tnirps_monopoly import Monome
import math
import random
import samples_poly

poly = Polynome(samples_poly.lng1)
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
#tnirps_recursive_split.printTree(tree)
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