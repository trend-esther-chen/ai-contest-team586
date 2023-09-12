import unittest 


# Fake, just for pass IDE
def solution(equation: str) -> str:
    pass


class M002(unittest.TestCase):
    def test_simple1(self):
        self.assertEqual(solution("4Al+3O2=2Al2O3"), "yes")

    def test_simple2(self):
        self.assertEqual(solution("2Na+2H2O=2NaOH+H2"), "yes")

    def test_simple3(self):
        self.assertEqual(solution("C2H5OH+3O2=2CO2+2H2O"), "no")

    def test_simple4(self):
        self.assertEqual(solution("6CO2+12H2O=C6H12O6+6H2O+6O2"), "yes")

    def test_simple5(self):
        self.assertEqual(solution("ABCDE+BCDEF=ABCDE"), "no")

