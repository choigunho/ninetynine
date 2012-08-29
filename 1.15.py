import itertools
def flat(l):
	return list(itertools.chain.from_iterable(l))

def dupli(l,i):
	return flat([k*i for k in l])

#testcase
print dupli(['a','b','c'],3)