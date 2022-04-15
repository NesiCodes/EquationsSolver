import unittest
import ekuacione_fuqi2
import grafiket_fuqi2


class TestEk2(unittest.TestCase):

    def test_1(self):
        equation = "2x^2-3x+1=0"
        a = ek2.parse_eq(equation)[0]
        b = ek2.parse_eq(equation)[1]
        c = ek2.parse_eq(equation)[2]
        result = ek2.roots_of_equation(a, b, c)
        self.assertEqual(result, "D=1 x1=1.0 x2=0.5")

        equation = "-3x+1+2x^2=0"
        a = ek2.parse_eq(equation)[0]
        b = ek2.parse_eq(equation)[1]
        c = ek2.parse_eq(equation)[2]
        result = ek2.roots_of_equation(a, b, c)
        self.assertEqual(result, "D=1 x1=1.0 x2=0.5")

        equation = "1+2x^2-3x=0"
        a = ek2.parse_eq(equation)[0]
        b = ek2.parse_eq(equation)[1]
        c = ek2.parse_eq(equation)[2]
        result = ek2.roots_of_equation(a, b, c)
        self.assertEqual(result, "D=1 x1=1.0 x2=0.5")

    def test_2(self):
        equation = "2x^2-4x+2=0"
        a = ek2.parse_eq(equation)[0]
        b = ek2.parse_eq(equation)[1]
        c = ek2.parse_eq(equation)[2]
        result = ek2.roots_of_equation(a, b, c)
        self.assertEqual(result, "D=0 x=1.0")

        equation = "-4x+2+2x^2=0"
        a = ek2.parse_eq(equation)[0]
        b = ek2.parse_eq(equation)[1]
        c = ek2.parse_eq(equation)[2]
        result = ek2.roots_of_equation(a, b, c)
        self.assertEqual(result, "D=0 x=1.0")

        equation = "+2-4x+2x^2=0"
        a = ek2.parse_eq(equation)[0]
        b = ek2.parse_eq(equation)[1]
        c = ek2.parse_eq(equation)[2]
        result = ek2.roots_of_equation(a, b, c)
        self.assertEqual(result, "D=0 x=1.0")

    def test_3(self):
        equation = "2x^2-3x+5=0"
        a = ek2.parse_eq(equation)[0]
        b = ek2.parse_eq(equation)[1]
        c = ek2.parse_eq(equation)[2]
        result = ek2.roots_of_equation(a, b, c)
        self.assertEqual(result, "D<0 Nuk ka rrenje reale")

        equation = "-3x+5+2x^2=0"
        a = ek2.parse_eq(equation)[0]
        b = ek2.parse_eq(equation)[1]
        c = ek2.parse_eq(equation)[2]
        result = ek2.roots_of_equation(a, b, c)
        self.assertEqual(result, "D<0 Nuk ka rrenje reale")

        equation = "+5-3x+2x^2=0"
        a = ek2.parse_eq(equation)[0]
        b = ek2.parse_eq(equation)[1]
        c = ek2.parse_eq(equation)[2]
        result = ek2.roots_of_equation(a, b, c)
        self.assertEqual(result, "D<0 Nuk ka rrenje reale")

    def test_4(self):
        equation = "5x^2+6x+1=0"
        a = ek2.parse_eq(equation)[0]
        b = ek2.parse_eq(equation)[1]
        c = ek2.parse_eq(equation)[2]
        result = ek2.roots_of_equation(a, b, c)
        self.assertEqual(result, "D=16 x1=-0.2 x2=-1.0")

        equation = "6x+5x^2+1=0"
        a = ek2.parse_eq(equation)[0]
        b = ek2.parse_eq(equation)[1]
        c = ek2.parse_eq(equation)[2]
        result = ek2.roots_of_equation(a, b, c)
        self.assertEqual(result, "D=16 x1=-0.2 x2=-1.0")

        equation = "1+6x+5x^2=0"
        a = ek2.parse_eq(equation)[0]
        b = ek2.parse_eq(equation)[1]
        c = ek2.parse_eq(equation)[2]
        result = ek2.roots_of_equation(a, b, c)
        self.assertEqual(result, "D=16 x1=-0.2 x2=-1.0")

    def test_5(self):
        equation = "5x^2+2x+1=0"
        a = ek2.parse_eq(equation)[0]
        b = ek2.parse_eq(equation)[1]
        c = ek2.parse_eq(equation)[2]
        result = ek2.roots_of_equation(a, b, c)
        self.assertEqual(result, "D<0 Nuk ka rrenje reale")

        equation = "2x+1+5x^2=0"
        a = ek2.parse_eq(equation)[0]
        b = ek2.parse_eq(equation)[1]
        c = ek2.parse_eq(equation)[2]
        result = ek2.roots_of_equation(a, b, c)
        self.assertEqual(result, "D<0 Nuk ka rrenje reale")

        equation = "1+5x^2+2x=0"
        a = ek2.parse_eq(equation)[0]
        b = ek2.parse_eq(equation)[1]
        c = ek2.parse_eq(equation)[2]
        result = ek2.roots_of_equation(a, b, c)
        self.assertEqual(result, "D<0 Nuk ka rrenje reale")

    def test_6(self):
        equation = "x^2-4x+6.25=0"
        a = ek2.parse_eq(equation)[0]
        b = ek2.parse_eq(equation)[1]
        c = ek2.parse_eq(equation)[2]
        result = ek2.roots_of_equation(a, b, c)
        self.assertEqual(result, "D<0 Nuk ka rrenje reale")

        equation = "6.25+x^2-4x=0"
        a = ek2.parse_eq(equation)[0]
        b = ek2.parse_eq(equation)[1]
        c = ek2.parse_eq(equation)[2]
        result = ek2.roots_of_equation(a, b, c)
        self.assertEqual(result, "D<0 Nuk ka rrenje reale")

        equation = "-4x+6.25+x^2=0"
        a = ek2.parse_eq(equation)[0]
        b = ek2.parse_eq(equation)[1]
        c = ek2.parse_eq(equation)[2]
        result = ek2.roots_of_equation(a, b, c)
        self.assertEqual(result, "D<0 Nuk ka rrenje reale")

    def test_7(self):
        equation = "x^2+15x+50=0"
        a = ek2.parse_eq(equation)[0]
        b = ek2.parse_eq(equation)[1]
        c = ek2.parse_eq(equation)[2]
        result = ek2.roots_of_equation(a, b, c)
        self.assertEqual(result, "D=25 x1=-5.0 x2=-10.0")

        equation = "15x+50+x^2=0"
        a = ek2.parse_eq(equation)[0]
        b = ek2.parse_eq(equation)[1]
        c = ek2.parse_eq(equation)[2]
        result = ek2.roots_of_equation(a, b, c)
        self.assertEqual(result, "D=25 x1=-5.0 x2=-10.0")

        equation = "50+x^2+15x=0"
        a = ek2.parse_eq(equation)[0]
        b = ek2.parse_eq(equation)[1]
        c = ek2.parse_eq(equation)[2]
        result = ek2.roots_of_equation(a, b, c)
        self.assertEqual(result, "D=25 x1=-5.0 x2=-10.0")

    def test_8(self):
        equation = "2x^2-11x+14=0"
        a = ek2.parse_eq(equation)[0]
        b = ek2.parse_eq(equation)[1]
        c = ek2.parse_eq(equation)[2]
        result = ek2.roots_of_equation(a, b, c)
        self.assertEqual(result, "D=9 x1=3.5 x2=2.0")

        equation = "-11x+14+2x^2=0"
        a = ek2.parse_eq(equation)[0]
        b = ek2.parse_eq(equation)[1]
        c = ek2.parse_eq(equation)[2]
        result = ek2.roots_of_equation(a, b, c)
        self.assertEqual(result, "D=9 x1=3.5 x2=2.0")

        equation = "14+2x^2-11x=0"
        a = ek2.parse_eq(equation)[0]
        b = ek2.parse_eq(equation)[1]
        c = ek2.parse_eq(equation)[2]
        result = ek2.roots_of_equation(a, b, c)
        self.assertEqual(result, "D=9 x1=3.5 x2=2.0")

    def test_9(self):
        equation = "x^2+4x-96=0"
        a = ek2.parse_eq(equation)[0]
        b = ek2.parse_eq(equation)[1]
        c = ek2.parse_eq(equation)[2]
        result = ek2.roots_of_equation(a, b, c)
        self.assertEqual(result, "D=400 x1=8.0 x2=-12.0")

        equation = "4x-96+x^2=0"
        a = ek2.parse_eq(equation)[0]
        b = ek2.parse_eq(equation)[1]
        c = ek2.parse_eq(equation)[2]
        result = ek2.roots_of_equation(a, b, c)
        self.assertEqual(result, "D=400 x1=8.0 x2=-12.0")

        equation = "-96+4x+x^2=0"
        a = ek2.parse_eq(equation)[0]
        b = ek2.parse_eq(equation)[1]
        c = ek2.parse_eq(equation)[2]
        result = ek2.roots_of_equation(a, b, c)
        self.assertEqual(result, "D=400 x1=8.0 x2=-12.0")

    def test_10(self):
        equation = "2x^2+9x=0"
        a = ek2.parse_eq(equation)[0]
        b = ek2.parse_eq(equation)[1]
        c = ek2.parse_eq(equation)[2]
        result = ek2.roots_of_equation(a, b, c)
        self.assertEqual(result, "D=81 x1=0.0 x2=-4.5")

        equation = "9x+2x^2=0"
        a = ek2.parse_eq(equation)[0]
        b = ek2.parse_eq(equation)[1]
        c = ek2.parse_eq(equation)[2]
        result = ek2.roots_of_equation(a, b, c)
        self.assertEqual(result, "D=81 x1=0.0 x2=-4.5")

    def test_11(self):
        equation = "-3x^2+243=0"
        a = ek2.parse_eq(equation)[0]
        b = ek2.parse_eq(equation)[1]
        c = ek2.parse_eq(equation)[2]
        result = ek2.roots_of_equation(a, b, c)
        self.assertEqual(result, "D=2916 x1=-9.0 x2=9.0")

        equation = "243-3x^2=0"
        a = ek2.parse_eq(equation)[0]
        b = ek2.parse_eq(equation)[1]
        c = ek2.parse_eq(equation)[2]
        result = ek2.roots_of_equation(a, b, c)
        self.assertEqual(result, "D=2916 x1=-9.0 x2=9.0")

    def test_12(self):
        equation = "-x^2"
        a = ek2.parse_eq(equation)[0]
        b = ek2.parse_eq(equation)[1]
        c = ek2.parse_eq(equation)[2]
        result = ek2.roots_of_equation(a, b, c)
        self.assertEqual(result, "D=0 x=-0.0")


if __name__ == '__main__':
    unittest.main()