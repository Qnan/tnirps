######################################################################
## 
## Tnirps: Simple recursive split procedure for tree building
## 
######################################################################
from tnirps_utils import TreeNode
from tnirps_utils import doTests
import tnirps_midx_lb; Midx = tnirps_midx_lb
from tnirps_monopoly import Monome

def subList (mons, m):
    for monome in mons:
        monome.midx = Midx.sub(monome.midx, m)
    return mons
    

def split (mons):
    """Find the maximum prefix of the sequence having nontrivial common divisor
        and return this divisor along with the first part of the list divided by it
        and the second part as is.
        
    """
    mcm=mons[0].midx
    for i in range(len(mons)):
        m = Midx.min(mcm, mons[i].midx)
        if Midx.isZero(m):
            return mcm, subList(mons[:i], mcm), mons[i:]
        mcm = m
    return mcm, subList(mons, mcm), []

def monomesToTree (monomes):
    """Create a tree by recursively splitting the list of monomes.
        The resulting tree is binary.
    
    """
    if len(monomes) == 1:
        return TreeNode(monomes[0])
    else:
        mcm, ml1, ml2 = split(monomes)
        if len(ml1) > 1:
            lnode = TreeNode('*', [TreeNode(mcm), monomesToTree(ml1)])
        else:
            lnode = TreeNode(mcm)
        if len(ml2) > 0:
            rnode = monomesToTree(ml2)
            return TreeNode('+', [lnode, rnode])
        else:
            return lnode

def printTree (tree, offset = 0):
    print('  ' * offset + str(tree.data))
    [printTree(child, offset + 1) for child in tree.children]

if __name__=='__main__':
    lst = ((1, (2,3)), (2, (2,1)), (3, (1,0)), (5, (0,3)), (7, (0,2)))
    mons = [Monome(el[0], el[1]) for el in lst]
    r = split(mons)
    print(str(r))
    tests = [
        [split(mons), "TreeNode init"]
        ]
    doTests(tests)