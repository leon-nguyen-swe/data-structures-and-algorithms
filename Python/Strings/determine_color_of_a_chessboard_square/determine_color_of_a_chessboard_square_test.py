import unittest

from determine_color_of_a_chessboard_square import Solution


class TestDetermineColorOfAChessboardSquare(unittest.TestCase):
    def setUp(self) -> None:
        self.solution = Solution()

    def test_examples(self) -> None:
        self.assertFalse(self.solution.squareIsWhite("a1"))
        self.assertTrue(self.solution.squareIsWhite("h3"))
        self.assertFalse(self.solution.squareIsWhite("c7"))

    def test_corner_squares(self) -> None:
        self.assertFalse(self.solution.squareIsWhite("a1"))
        self.assertTrue(self.solution.squareIsWhite("a8"))
        self.assertTrue(self.solution.squareIsWhite("h1"))
        self.assertFalse(self.solution.squareIsWhite("h8"))

    def test_full_board_parity(self) -> None:
        files = "abcdefgh"
        for file_index, file_char in enumerate(files):
            for rank in range(1, 9):
                coord = f"{file_char}{rank}"
                expected_is_white = (file_index + 1 + rank) % 2 == 1
                with self.subTest(coordinates=coord):
                    self.assertEqual(
                        self.solution.squareIsWhite(coord), expected_is_white
                    )


if __name__ == "__main__":
    unittest.main()
