import random
import unittest

class PrologLists(unittest.TestCase):
	def test_1_1(self):
		def last(li):
			return li[-1]

		self.assertEquals(5, last([1,2,3,4,5]))
		self.assertEquals(-5, last([-1,-2,-3,-4,-5]))

	def test_1_23(self):
		def rnd_select(li, cnt):
			res = []

			for i in range(cnt):
				rnd = random.choice(li)
				res.append(rnd)
				li.remove(rnd)
				#print rnd, li, res
			print "This is solution for 1_23 :",res

		rnd_select([1,2,3,4,5], 3)
	
	def test_1_24(self):
		pass #print "a"

		#self.assertEquals(, rnd_select([1,2,3,4,5], 3))

	
if __name__ == "__main__":
	unittest.main()		