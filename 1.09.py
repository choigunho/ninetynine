def pack(l):
	result = []
	temp = []
	temp.append(l.pop(0))

	for item in l:
		if item == temp[0]:
			temp.extend(item)	
		else:
			result.append(temp)
			temp = []
			temp.extend(item)

	result.append(temp)

	return result

print pack(['a','a','a','b','c','c','a','a','d','e','e','e'])