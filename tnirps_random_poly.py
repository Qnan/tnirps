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

print(str(',\n'.join([str(el) for el in makeRandPoly(3, 0.01, 0.7, 0.001)])))
