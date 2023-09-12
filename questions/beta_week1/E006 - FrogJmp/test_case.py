import unittest 


# Fake, just for pass IDE
def solution(x:int, y:int, d:int) -> int:
    pass


class E006(unittest.TestCase):
    def test_simple1(self):
        self.assertEqual(solution(10, 85, 30), 3)

    def test_simple2(self):
        self.assertEqual(solution(0, 10, 1), 10)

    def test_simple3(self):
        self.assertEqual(solution(0, 10, 20), 1)

    def test_simple4(self):
        self.assertEqual(solution(10, 100, 10), 9)

    def test_simple5(self):
        self.assertEqual(solution(10, 10, 10), 0)

    def test_simple6(self):
        self.assertEqual(solution(9, 29, 10), 2)

