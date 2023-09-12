import unittest 


# Fake, just for pass IDE
def solution(cards: list[int]) -> int:
    pass


class E004(unittest.TestCase):
    def test_simple1(self):
        self.assertEqual(solution([8, 15, 3, 7]), 22)

    def test_simple2(self):
        self.assertEqual(solution([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]), 50)

    def test_simple3(self):
        self.assertEqual(solution([100000000, 700000000, 300000000, 400000000, 50000000, 60000000]), 1160000000)

    def test_simple4(self):
        self.assertEqual(solution([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), 0)

    def test_simple5(self):
        self.assertEqual(solution([8, 15, 3, 7, 8, 15, 3, 7, 8, 15, 3, 7, 8, 15, 3, 7, 8, 15, 3, 7, 8, 15, 3, 7, 8, 15, 3, 7, 8, 15, 3, 7, 8, 15, 3, 7, 8, 15, 3, 7, 8, 15, 3, 7, 8, 15, 3, 7, 8, 15, 3, 7, 8, 15, 3, 7, 8, 15, 3, 7, 8, 15, 3, 7, 8, 15, 3, 7, 8, 15, 3, 7, 8, 15, 3, 7, 8, 15, 3, 7, 8, 15, 3, 7, 8, 15, 3, 7, 8, 15, 3, 7, 8, 15, 3, 7, 8, 15, 3, 7, 8, 15, 3, 7, 8, 15, 3, 7, 8, 15, 3, 7, 8, 15, 3, 7, 8, 15, 3, 7, 8, 15, 3, 7, 8, 15, 3, 7, 8, 15, 3, 7, 8, 15, 3, 7, 8, 15, 3, 7, 8, 15, 3, 7, 8, 15, 3, 7, 8, 15, 3, 7, 8, 15, 3, 7, 8, 15, 3, 7, 8, 15, 3, 7, 8, 15, 3, 7, 8, 15, 3, 7, 8, 15, 3, 7, 8, 15, 3, 7, 8, 15, 3, 7, 8, 15, 3, 7, 8, 15, 3, 7, 8, 15, 3, 7, 8, 15, 3, 7, 8, 15, 3, 7, 8, 15, 3, 7, 8, 15, 3, 7, 8, 15, 3, 7, 8, 15, 3, 7, 8, 15, 3, 7, 8, 15, 3, 7, 8, 15, 3, 7, 8, 15, 3, 7, 8, 15, 3, 7, 8, 15, 3, 7, 8, 15, 3, 7, 8, 15, 3, 7, 8, 15, 3, 7, 8, 15, 3, 7, 8, 15, 3, 7, 8, 15, 3, 7, 8, 15, 3, 7, 8, 15, 3, 7, 8, 15, 3, 7, 8, 15, 3, 7, 8, 15, 3, 7, 8, 15, 3, 7, 8, 15, 3, 7, 8, 15, 3, 7, 8, 15, 3, 7, 8, 15, 3, 7, 8, 15, 3, 7, 8, 15, 3, 7, 8, 15, 3, 7, 8, 15, 3, 7, 8, 15, 3, 7, 8, 15, 3, 7, 8, 15, 3, 7, 8, 15, 3, 10]), 1873)

    def test_simple6(self):
        self.assertEqual(solution([1, 1]), 1)

    def test_simple7(self):
        self.assertEqual(solution([0, 1, 0, 1, 100, 50, 3, 9, 9, 2, 3, 5, 2, 2, 6, 1000, 33333, 6, 77777777, 9]), 77811233)
