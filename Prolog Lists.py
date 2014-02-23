import random, itertools
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

	def test_1_6(self):
		def palindrome(li):
			return li == li[::-1]

		self.assertEquals(False, palindrome([1,2,3,4,5]))
		self.assertEquals(True, palindrome([1,2,3,2,1]))

	def test_1_7(self):
		def my_flatten(li):
			rst = []

			for item in li:
				if isinstance(item, list):
					rst += my_flatten(item)
				else:
					rst.append(item)
			return rst

		self.assertEquals([1,2,3], my_flatten([1,[2,3]]))
		self.assertEquals([1,2,3,4,5], my_flatten([1,[2,[3,4],5]]))

	def test_1_8(self):
		def compress(li):
			return [k for k, i in itertools.groupby(li)]

		self.assertEquals([1,2,3,4,5], compress([1,1,1,1,2,2,2,3,3,3,3,3,3,3,4,4,5]))

	def test_1_9(self):
		def pack(li):
			return [list(i) for k, i in itertools.groupby(li)]

		self.assertEquals([[1,1,1,1],[2,2,2],[3],[4,4,4],[5]], pack([1,1,1,1,2,2,2,3,4,4,4,5]))

	def test_1_10(self):
		def encode(li):
			return [[len(list(i)), k] for k, i in itertools.groupby(li)]

		self.assertEquals([[3,1],[2,2],[5,3],[2,1],[3,5]], encode([1,1,1,2,2,3,3,3,3,3,1,1,5,5,5]))

	def test_1_11(self):
		def encode_modified(li):
			rst = []

			for k, i in itertools.groupby(li):
				v = list(i)
				rst.append(v[0] if len(v) == 1 else [len(v), k])
			return rst

		self.assertEquals([[3, 1], [2, 2], 3, [2, 4], [3, 5]], encode_modified([1,1,1,2,2,3,4,4,5,5,5]))

	def test_1_12(self):
		def decode(li):
			rst = []

			for i in li:
				rst.extend(i[1]*i[0] if isinstance(i, list) else i) 
			return rst

		self.assertEquals(['a', 'a', 'a', 'a', 'b', 'c', 'c', 'a', 'a', 'd', 'e', 'e', 'e', 'e'], decode([[4, 'a'], 'b', [2, 'c'], [2, 'a'], 'd', [4, 'e']]))

	def test_1_14(self):
		def dupli(li):
			rst = []

			for i in li:
				rst.extend(i+i)
			return rst

		self.assertEquals(['a', 'a', 'b', 'b', 'c', 'c', 'c', 'c', 'd', 'd'], dupli(['a','b','c','c','d']))

	def test_1_15(self):
		def dupli2(li, cnt):
			return [i for i in li for _ in range(cnt)]

		self.assertEquals(['a', 'a', 'a', 'c', 'c', 'c', 'b', 'b', 'b'], dupli2(['a','c','b'], 3))

	def test_1_16(self):
		def drop(li, n):
			del li[2::n]
			return li

		self.assertEquals(['a', 'b', 'd', 'e', 'g', 'h', 'k'], drop(['a','b','c','d','e','f','g','h','i','k'],3))

	def test_1_17(self):
		def split(l, i):
			return l[:i], l[i:]

		self.assertEqual((['a','b','c'],['d','e','f','g','h','i','k']), split(['a','b','c','d','e','f','g','h','i','k'],3))


	def test_1_18(self):
		def slice(l, i, j):
			return l[i-1:j]

		self.assertEqual((['c','d','e','f','g']), slice(['a','b','c','d','e','f','g','h','i','k'],3,7))

	def test_1_19(self):
		def rotate(l, i):
			return l[i:]+l[:i]

		self.assertEquals(['d', 'e', 'f', 'g', 'h', 'a', 'b', 'c'], rotate(['a','b','c','d','e','f','g','h'],3))
		self.assertEquals(['g', 'h', 'a', 'b', 'c', 'd', 'e', 'f'], rotate(['a','b','c','d','e','f','g','h'],-2))

	def test_1_20(self):
		def remove_at(l, n):
			del l[n-1]

	def test_1_21(self):
		def insert_at(d, li, p):
			li.insert(p-1, d)
			return li

		self.assertEquals(['a', 'alfa', 'b', 'c', 'd'], insert_at('alfa',['a','b','c','d'],2))

	def test_1_22(self):
		def _range(s, e):
			return [i for i in range(s, e+1)]
		
		self.assertEquals([4, 5, 6, 7, 8, 9], _range(4,9))

	def test_1_23(self):
		def rnd_select(li, cnt):
			res = []

			for i in range(cnt):
				rnd = random.choice(li)
				res.append(rnd)
				li.remove(rnd)
			#print "This is solution for 1_23 :",res

		rnd_select([1,2,3,4,5], 3)
	
	def test_1_24(self):
		def rnd_select2(cnt, rng):
			lotto = [i for i in range(1, rng+1)]
			rst = []

			for i in range(cnt):
				rnd = random.choice(lotto)
				rst.append(rnd)
				lotto.remove(rnd)
			return rst

		# print "This is solution for 1_24 :", rnd_select2(6, 49)

	'''
	1.25 (*) Generate a random permutation of the elements of a list.
		Example:
		?- rnd_permu([a,b,c,d,e,f],L).
		L = [b,a,d,c,e,f]

		Hint: Use the solution of problem 1.23.
	'''
	def test_1_25(self):
		def rnd_select(li):
			res = []

			for i in range(len(li)):
				rnd = random.choice(li)
				res.append(rnd)
				li.remove(rnd)
		
			# print "This is solution for 1_25 :", res

		rnd_select([1,2,3,4,5])
		
	
	
if __name__ == "__main__":
	suite = unittest.TestLoader().loadTestsFromTestCase(PrologLists)
	unittest.TextTestRunner(verbosity=2).run(suite)