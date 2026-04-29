import unittest
from ugly_number_ii import Solution


class TestUglyNumberII(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_n1(self):
        self.assertEqual(self.solution.nthUglyNumber(1), 1)

    def test_n7(self):
        self.assertEqual(self.solution.nthUglyNumber(7), 8)

    def test_n10(self):
        self.assertEqual(self.solution.nthUglyNumber(10), 12)

    def test_n11(self):
        self.assertEqual(self.solution.nthUglyNumber(11), 15)

    def test_first_ten_sequence(self):
        expected = [1, 2, 3, 4, 5, 6, 8, 9, 10, 12]
        result = [self.solution.nthUglyNumber(i) for i in range(1, 11)]
        self.assertEqual(result, expected)

    def test_zero_raises_index_error(self):
        with self.assertRaises(IndexError):
            self.solution.nthUglyNumber(0)


if __name__ == "__main__":
    unittest.main()
