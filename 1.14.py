def dupli(l):
	a = []
	
	for k in l:
		a.extend(k)
		a.extend(k)

	return a

#testcase
print dupli(['a','b','c','c','d'])