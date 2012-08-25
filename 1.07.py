def my_fllatten(l):
	result = []
	
	for item in l:
		if isinstance(item, list):
			result += my_fllatten(item)
		else:
			result.append(item)
	return result

print my_fllatten([1,[2,[3,4],5]])