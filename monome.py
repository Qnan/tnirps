def evaluateMonome (monome, vals):
    prod = 1
    for var in monome.keys():
        prod *= vals[var] ** monome[var]
    return prod

def evaluatePolynome (poly, vals):
    sum = 0
    for monome in poly:
        sum += evaluateMonome(monome, vals)
    return sum

degs = [{'x':2},{'x':1,'y':1},{'y':2}]
vals = {'x':3,'y':5}
print str(evaluatePolynome(degs, vals))