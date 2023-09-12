import unittest 


# Fake, just for pass IDE
def solution(s:str) -> int:
    pass


class M012(unittest.TestCase):
    def test_simple1(self):
        self.assertEqual(solution("{[()()]}"), 1)

    def test_simple2(self):
        self.assertEqual(solution("([)()]"), 0)

    def test_simple3(self):
        self.assertEqual(solution(""), 1)

    def test_simple4(self):
        self.assertEqual(solution("{[(V)(W)]}"), 1)

    def test_simple5(self):
        self.assertEqual(solution("[{V}[W]]"), 1)

    def test_simple6(self):
        self.assertEqual(solution("[{V(W)]"), 0)

    def test_simple7(self):
        self.assertEqual(solution(")"), 0)

