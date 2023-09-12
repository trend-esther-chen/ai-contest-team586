import unittest 


# Fake, just for pass IDE
def solution(n:int) -> int:
    pass


class M008(unittest.TestCase):
    def test_simple1(self):
        self.assertEqual(solution(645), 4)

    def test_simple2(self):
        self.assertEqual(solution(7), 4)

    def test_simple3(self):
        self.assertEqual(solution(143), 4)

    def test_simple4(self):
        self.assertEqual(solution(999), 2)

    def test_simple5(self):
        self.assertEqual(solution(2), 2)

    def test_simple6(self):
        self.assertEqual(solution(888), 4)

    def test_simple7(self):
        self.assertEqual(solution(1000), 2)

    def test_simple8(self):
        self.assertEqual(solution(777), 4)

    def test_simple9(self):
        self.assertEqual(solution(14), 2)

    def test_simple10(self):
        self.assertEqual(solution(1), 1)

