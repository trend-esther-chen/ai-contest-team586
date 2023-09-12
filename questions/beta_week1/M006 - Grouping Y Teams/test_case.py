import unittest 


# Fake, just for pass IDE
def solution(teams: list[int], g: int) -> list[int]:
    pass


class M006(unittest.TestCase):
    def test_simple1(self):
        self.assertEqual(solution([7, 49, 47, 27, 39, 41, 79, 49, 17, 16, 16, 9, 44], 5), [88, 88, 88, 88, 88])

    def test_simple2(self):
        self.assertEqual(solution([125, 162, 185, 132, 34, 32, 151, 67, 14, 3, 13, 142, 35, 11, 44, 37, 7], 6), [199, 199, 199, 199, 199, 199])

    def test_simple3(self):
        self.assertEqual(solution([126, 162, 185, 132, 34, 32, 150, 67, 14, 3, 13, 141, 35, 11, 44, 37, 8], 6), [200, 199, 199, 199, 199, 198])

    def test_simple4(self):
        self.assertEqual(solution([71, 11, 130, 14, 153, 58, 162, 55, 117, 35, 99, 89, 177, 35, 26, 118, 154], 8), [189, 188, 188, 188, 188, 188, 188, 187])

    def test_simple5(self):
        self.assertEqual(solution([325, 845, 648, 802, 329, 251, 257, 53, 113, 35, 529, 7, 55, 203, 245, 491, 205, 846, 55], 7), [900, 899, 899, 899, 899, 899, 899])

    def test_simple6(self):
        self.assertEqual(solution([125, 162, 185, 132, 34, 32, 150, 67, 14, 3, 13, 143, 35, 11, 44, 37, 7], 7), [185, 169, 169, 169, 168, 167, 167])

