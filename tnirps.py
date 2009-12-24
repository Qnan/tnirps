#import tnirps_recursive_split
import tnirps_utils; Utils = tnirps_utils
import tnirps_midx_lb; Midx = tnirps_midx_lb
from tnirps_monopoly import Polynome
#import math
import samples_poly

poly = Polynome(samples_poly.med1)
print(poly)
mons = [el.midx for el in poly.toMonomes()]
vals = (3,2,-1)
mod = 373587883
print("mons: " + str(mons))

# build graph
def buildGrapg (mons):
    rmons = range(len(mons))
    edges = []
    for i in rmons:
        for j in rmons:        
            if i != j and Midx.cmp(mons[i], mons[j]) == 1:
                edges.append((i, j, max(Midx.sub(mons[i], mons[j]))))            
    return edges 

edges = buildGrapg(mons)
print("edges: " + str(edges))                
edges.sort(key=lambda x: x[2])
print("edges sorted: " + str(edges))

def minSpanTree (mons, edges):
    rmons = range(len(mons))
    vsets = [i for i in rmons]
    tree = []
    for edge in edges:
        if vsets[edge[0]] != vsets[edge[1]]:
            v = vsets[edge[0]]
            tree.append(edge)
            for i in rmons:
                if vsets[i] == v:
                    vsets[i] = vsets[edge[1]]
#            print(vsets)
#    print((len(mons), len(tree), len(edges)))
    return tree 

tree = minSpanTree(mons,edges)
print("tree: " + str(tree))
                  
# sort vertices topologically
rmons = range(len(mons))
refcnt = [0 for i in rmons]
order = []
for edge in tree:
    refcnt[edge[0]] = refcnt[edge[0]] + 1 
for i in rmons:
    j0 = -1
    for j in rmons:
        if refcnt[j] == 0:            
            j0 = j
            break
    for edge in tree:
        if edge[1] == j0:
            refcnt[edge[0]] = refcnt[edge[0]] - 1
    order.append(j0)
    refcnt[j0] = -1
    
print(order)


#values = [0 for el in mons]
#front = [i for i in rmons if nodes[i] == 0]
#for i in front:
#    values[i] = Midx.eval(mons[i], vals)
#while front:
#    newFront = []
#    for i in front:
#        val = 0
#        for j in redges[i]:
#            val
#            

print('Done')