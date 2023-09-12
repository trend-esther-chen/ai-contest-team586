import unittest 


# Fake, just for pass IDE
def solution(inorder: str, postorder: str) -> str:
    pass


class E002(unittest.TestCase):
    def test_simple1(self):
        self.assertEqual(solution("abdec", "adbce"), "ebadc")

    def test_simple2(self):
        self.assertEqual(solution("bdfcea", "dbeacf"), "fbdcae")

    def test_simple3(self):
        self.assertEqual(solution("edcba", "abcde"), "edcba")

    def test_simple4(self):
        self.assertEqual(solution("dbeafcg", "debfgca"), "abdecfg")

    def test_simple5(self):
        self.assertEqual(solution("bac", "bca"), "abc")

