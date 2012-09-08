def rotate(l, i):
    return l[i:]+l[:i]

print rotate(['a','b','c','d','e','f','g','h'],3)
print rotate(['a','b','c','d','e','f','g','h'],-2)