import itertools
def encode(l):
	#for k, g in itertools.groupby(l):
	#	print [len(list(g)), k]
	return [[len(list(g)), k] for k, g in itertools.groupby(l)] 

print encode(['a','a','a','a','b','c','c','a','a','d','e','e','e','e'])