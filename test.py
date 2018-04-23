import numpy

class Test:
    r = 100
    g = 20
    b = 10
    change_color(r,g,b)
    def test_red(self,r):
        r = r * 20
    def test_blue(self,b):
        b += 10
    def change_color(self,r,g,b):
        test_red(r)
        test_blue(b)
