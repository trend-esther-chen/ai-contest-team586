import unittest 


# Fake, just for pass IDE
def solution(number: int) -> int:
    pass


class E001(unittest.TestCase):
    def test_simple1(self):
        self.assertEqual(solution(11), 7)

    def test_simple2(self):
        self.assertEqual(solution(10), 10)

    def test_simple3(self):
        self.assertEqual(solution(20), 6)

    def test_simple4(self):
        self.assertEqual(solution(500), 311)

    def test_simple5(self):
        self.assertEqual(solution(50), 40)

    def test_simple6(self):
        self.assertEqual(solution(100), 66)

