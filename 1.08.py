def compress(l):
	result = []
	result.append(l[0])

	for item in l:
		if result[-1] != item :
			result.append(item)

	return result

print compress(['a','a','a','a','b','c','c','a','a','d','e','e','e','e'])