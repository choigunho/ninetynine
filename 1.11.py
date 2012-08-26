import itertools
def encode_modified(l):
	result = []

	for k, g in itertools.groupby(l):
		o = [len(list(g)), k]

		if o[0] == 1:
			result.append(k)
		else:
			result.extend([[o[0], k]])

	return result

print encode_modified(['a','a','a','a','b','c','c','a','a','d','e','e','e','e'])