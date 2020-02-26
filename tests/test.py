import unittest
import code

class TestCases(unittest.TestCase):

	def test_sanity(self):
		self.assertEqual(1, 1)

	def test_sanity(self):
		self.assertEqual("abc", code.id("abc"))

if __name__ == "__main__":
	unittest.main()
