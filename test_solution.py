import unittest
from solution import Solution

class TestSolution(unittest.TestCase):

    def test_hammingWeight(self):
        sol = Solution()

        n = 0
        expected = 0
        self.assertEqual(sol.hammingWeight(n), expected)

        n = 1
        expected = 1
        self.assertEqual(sol.hammingWeight(n), expected)

        n = 11
        expected = 3
        self.assertEqual(sol.hammingWeight(n), expected)

        n = 128
        expected = 1
        self.assertEqual(sol.hammingWeight(n), expected)

        n = 255
        expected = 8
        self.assertEqual(sol.hammingWeight(n), expected)

        n = 4294967295
        expected = 32
        self.assertEqual(sol.hammingWeight(n), expected)

if __name__ == '__main__':
    unittest.main()
