import itertools

def range_(s, e):
    l = []
    for i in range(e-s+1):
        l.extend([s+i])
    return l

print range_(4,9)