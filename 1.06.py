def palindrome(l):
	result = "false"

	head = l[:len(l)/2]
	tail = l[len(l)/2 + 1:]
	tail.reverse()

	if head == tail:
		result = "true"
	
	return result

print palindrome(['x','a','m','a','x'])
print palindrome(['x','a','m','a','g'])