#test supersum
import unittest
from math_x.super_sum import super_sum
#relative import in python
class SuperSumTest(unittest.TestCase):
	def test_two_numbers(self):
		result = super_sum(20,20)
		self.assertEqual(result,40)

	def test_four_numbers(self):
		result = super_sum(10,20,30,40)
		self.assertEqual(result,100)

	def test_two_lists(self):
		a = [10,20,30,40]
		b = [100,20]
		result = super_sum(a,b)
		self.assertEqual(result,220)

	def test_list_and_number(self):
		a = []
		result = super_sum(a,50)
		self.assertEqual(result,140)

	def test_four_lists(self):
		a, b, c, d = [1,2],[2,3],[4],[4,10]
		result = super_sum(a,b,c,d)
		self.assertEqual(result,26)

	def test_large_input(self):
		#big_a = [i**3 for i in xrange(100)]
		pass
