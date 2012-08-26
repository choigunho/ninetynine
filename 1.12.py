import itertools
def decode(l):
	result = []

	for k, g in itertools.groupby(l):
		result.extend(k[1]*k[0])
	return result

print decode([[4, 'a'], [1, 'b'], [2, 'c'], [2, 'a'], [1, 'd'], [4, 'e']])