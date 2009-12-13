######################################################################
## 
## CSprint: Simple recursive split procedure for tree building
## 
######################################################################
import csprint_util

def split (mons):
    """Find the maximum prefix of the sequence having nontrivial common divisor
        and return this devisor along with the first part of the list divided by it
        and the second part as is.
        
    """
    mcm=mons[0]
    for i in range(len(mons)):
        m = midxMin(mcm, mons[i])
        if midxIsZero(m):
            return mcm, [midxSub(el, mcm) for el in mons[:i]], mons[i:]
        mcm = m
    return mcm, [midxSub(el, mcm) for el in mons], []

def monomesToTree (monomes):
    """Create a tree by recursively splitting the list of monomes.
        The resulting tree is binary.
    
    """
    if len(monomes) == 1:
        return TreeNode(monomes[0])
    else:
        children = []
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

