import unittest 


# Fake, just for pass IDE
def solution(a: list[int]) -> int:
    pass


class M014(unittest.TestCase):
    def test_simple1(self):
        self.assertEqual(solution([0]), 0)

    def test_simple2(self):
        self.assertEqual(solution([1]), 0)

    def test_simple3(self):
        self.assertEqual(solution([0, 0]), 0)

    def test_simple4(self):
        self.assertEqual(solution([1, 1]), 0)

    def test_simple5(self):
        self.assertEqual(solution([0, 1]), 1)

    def test_simple6(self):
        self.assertEqual(solution([1, 0]), 0)

    def test_simple7(self):
        self.assertEqual(solution([0, 0, 0]), 0)

    def test_simple8(self):
        self.assertEqual(solution([0, 0, 1]), 2)

    def test_simple9(self):
        self.assertEqual(solution([0, 1, 0]), 1)

    def test_simple10(self):
        self.assertEqual(solution([0, 1, 1]), 2)

    def test_simple11(self):
        self.assertEqual(solution([1, 0, 0]), 0)

    def test_simple12(self):
        self.assertEqual(solution([1, 0, 1]), 1)

    def test_simple13(self):
        self.assertEqual(solution([1, 1, 0]), 0)

    def test_simple14(self):
        self.assertEqual(solution([1, 1, 1]), 0)

    def test_simple15(self):
        self.assertEqual(solution([0, 0, 0, 0]), 0)

    def test_simple16(self):
        self.assertEqual(solution([0, 0, 0, 1]), 3)

    def test_simple17(self):
        self.assertEqual(solution([0, 0, 1, 1]), 4)

    def test_simple18(self):
        self.assertEqual(solution([0, 1, 0, 0]), 1)

    def test_simple19(self):
        self.assertEqual(solution([0, 1, 0, 1]), 3)

    def test_simple20(self):
        self.assertEqual(solution([0, 1, 1, 1]), 3)

    def test_simple21(self):
        self.assertEqual(solution([1, 0, 0, 0]), 0)

    def test_simple22(self):
        self.assertEqual(solution([1, 0, 0, 1]), 2)

    def test_simple23(self):
        self.assertEqual(solution([1, 0, 1, 0]), 1)

    def test_simple24(self):
        self.assertEqual(solution([1, 0, 1, 1]), 2)

    def test_simple25(self):
        self.assertEqual(solution([1, 1, 0, 0]), 0)

    def test_simple26(self):
        self.assertEqual(solution([1, 1, 0, 1]), 1)

    def test_simple27(self):
        self.assertEqual(solution([1, 1, 1, 0]), 0)

    def test_simple28(self):
        self.assertEqual(solution([1, 1, 1, 1]), 0)

