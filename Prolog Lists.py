import random
import unittest

class PrologLists(unittest.TestCase):
	def test_1_1(self):
		def last(li):
			return li[-1]

		self.assertEquals(5, last([1,2,3,4,5]))
		self.assertEquals(-5, last([-1,-2,-3,-4,-5]))

	def test_1_2(self):
		def butlast(li):
			return li[-2]

		self.assertEquals(4, butlast([1,2,3,4,5]))
		self.assertEquals(2, butlast([1,2,3]))

	def test_1_3(self):
		def elemAt(li, i):
			return li[i-1]

		self.assertEquals(1, elemAt([1,2,3,4,5], 1))
		self.assertEquals(3, elemAt([1,2,3,4,5], 3))
		self.assertEquals(5, elemAt([1,2,3,4,5], 5))

	def test_1_4(self):
		def findLen(li):
			return len(li)

		self.assertEquals(3, findLen([1,2,3]))
		self.assertEquals(5, findLen([1,2,3,4,5]))

	def test_1_5(self):
		def reverseList(li):
			li.reverse()
			return li

		self.assertEquals([5,4,3,2,1], reverseList([1,2,3,4,5]))
		self.assertEquals([10,5,4,3,1], reverseList([1,3,4,5,10]))

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