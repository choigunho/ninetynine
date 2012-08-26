import itertools
def decode(l):
	result = []

	for k, g in itertools.groupby(l):
		
		if isinstance(k, list):
			result.extend(k[1]*k[0])
		else:
			result.extend(k)

	return result

#testcase
print decode([[4, 'a'], 'b', [2, 'c'], [2, 'a'], 'd', [4, 'e']])