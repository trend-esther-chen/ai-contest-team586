import unittest 


# Fake, just for pass IDE
def solution(source_url:str) -> list[str]:
    pass


class H002(unittest.TestCase):
    def test_simple1(self):
        self.assertEqual(solution("www.mymainsite.com/somepath/path2/path3/path4"), ['www.mymainsite.com', '80', '/somepath/path2/path3/path4'])

    def test_simple2(self):
        self.assertEqual(solution("http://www.mymainsite.com/somepath/path2/path3/path4"), ['www.mymainsite.com', '80', '/somepath/path2/path3/path4'])

    def test_simple3(self):
        self.assertEqual(solution("https://www.mymainsite.com/somepath/path2/path3/path4"), ['www.mymainsite.com', '443', '/somepath/path2/path3/path4'])

    def test_simple4(self):
        self.assertEqual(solution("http://www.mymainsite.com:8080/somepath/path2/path3/path4"), ['www.mymainsite.com', '8080', '/somepath/path2/path3/path4'])

    def test_simple5(self):
        self.assertEqual(solution("http://www.mymainsite.com:8080/somepath/path2/path3/path4?urlparam1=hello&urlparam2=world"), ['www.mymainsite.com', '8080', '/somepath/path2/path3/path4', 'urlparam1=hello&urlparam2=world'])

    def test_simple6(self):
        self.assertEqual(solution("114.114.114.114/somepath/path2/path3/path4"), ['114.114.114.114', '80', '/somepath/path2/path3/path4'])

    def test_simple7(self):
        self.assertEqual(solution("http://114.114.114.114/somepath/path2/path3/path4"), ['114.114.114.11480', '/somepath/path2/path3/path4'])

    def test_simple8(self):
        self.assertEqual(solution("https://114.114.114.114/somepath/path2/path3/path4"), ['114.114.114.114', '443', '/somepath/path2/path3/path4'])

    def test_simple9(self):
        self.assertEqual(solution("http://114.114.114.114:8080/somepath/path2/path3/path4"), ['114.114.114.114', '8080', '/somepath/path2/path3/path4'])

    def test_simple10(self):
        self.assertEqual(solution("http://114.114.114.114:8080/somepath/path2/path3/path4?urlparam1=hello&urlparam2=world"), ['114.114.114.114', '8080', '/somepath/path2/path3/path4', 'urlparam1=hello&urlparam2=world'])

