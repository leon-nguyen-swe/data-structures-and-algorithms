import unittest
from hash_divided_string import Solution


class TestStringHash(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        """Test basic example: s="abcd", k=2"""
        result = self.solution.stringHash("abcd", 2)
        # 'ab': (0+1) % 26 = 1 -> 'b'
        # 'cd': (2+3) % 26 = 5 -> 'f'
        self.assertEqual(result, "bf")

    def test_example_2(self):
        """Test another example: s="mxz", k=3"""
        result = self.solution.stringHash("mxz", 3)
        # 'mxz': (12+23+25) % 26 = 60 % 26 = 8 -> 'i'
        self.assertEqual(result, "i")

    def test_single_char_k_one(self):
        """Test single character with k=1"""
        result = self.solution.stringHash("a", 1)
        # 'a': 0 % 26 = 0 -> 'a'
        self.assertEqual(result, "a")

    def test_single_char_k_higher(self):
        """Test single character with k higher than string"""
        result = self.solution.stringHash("z", 1)
        # 'z': 25 % 26 = 25 -> 'z'
        self.assertEqual(result, "z")

    def test_two_chars_sum_under_26(self):
        """Test two characters where sum < 26"""
        result = self.solution.stringHash("ab", 2)
        # 'ab': (0+1) % 26 = 1 -> 'b'
        self.assertEqual(result, "b")

    def test_two_chars_sum_over_26(self):
        """Test two characters where sum > 26"""
        result = self.solution.stringHash("zz", 2)
        # 'zz': (25+25) % 26 = 50 % 26 = 24 -> 'y'
        self.assertEqual(result, "y")

    def test_multiple_chunks(self):
        """Test multiple chunks"""
        result = self.solution.stringHash("abcdefgh", 2)
        # 'ab': 1 -> 'b'
        # 'cd': 5 -> 'f'
        # 'ef': 9 -> 'j'
        # 'gh': 13 -> 'n'
        self.assertEqual(result, "bfjn")

    def test_all_same_char(self):
        """Test string with all same characters"""
        result = self.solution.stringHash("aaaa", 2)
        # 'aa': 0 % 26 = 0 -> 'a'
        # 'aa': 0 % 26 = 0 -> 'a'
        self.assertEqual(result, "aa")

    def test_modulo_wrapping(self):
        """Test cases where sum wraps around via modulo"""
        result = self.solution.stringHash("zzz", 3)
        # 'zzz': (25+25+25) % 26 = 75 % 26 = 23 -> 'x'
        self.assertEqual(result, "x")

    def test_large_sum_modulo(self):
        """Test larger sum with modulo"""
        result = self.solution.stringHash("zzzzzz", 3)
        # 'zzz': 75 % 26 = 23 -> 'x'
        # 'zzz': 75 % 26 = 23 -> 'x'
        self.assertEqual(result, "xx")

    def test_mixed_chars(self):
        """Test mixed characters"""
        result = self.solution.stringHash("helloa", 2)
        self.assertEqual(result, "lwo")

    def test_long_chunk_short_string(self):
        """Test when k is equal to string length"""
        result = self.solution.stringHash("abc", 3)
        # 'abc': (0+1+2) % 26 = 3 -> 'd'
        self.assertEqual(result, "d")


if __name__ == "__main__":
    unittest.main()
