import math
import numpy as np
import re
import typing


def parse_eq(eq: str) -> tuple[float, float, float, float]:
    """mer nje ekuacion nga perdoruesi dhe rikthen vlerat a,b,c,d
    Parameters
    ----------
        eq: string
            ekuacioni nga perdoruesi
    Returns
    -------
        vlerat a,b,c,d ne float
        vlerat boshe zevendesohen me 0
    """

    eq = ''.join(char for char in eq if char != ' ')
    eq = eq.replace("=0", "")

    cubic = re.findall(r'([+-]*\d*)x\^3', eq) #^3
    square = re.findall(r'([+-]*\d*)x\^2', eq) #^2
    linear = re.findall(r'([+-]*\d*)x(?!\^)', eq) #^1(x)

    a = parse_param(cubic)
    b = parse_param(square)
    c = parse_param(linear)

    # c
    eq = eq.replace("^3", "")
    eq = eq.replace("^2", "")
    eq = eq.replace("^", "")
    eq = eq.replace("x", "")
    if(str(a) == "1"):
        print()
    elif(str(a) == "-1"):
        print()
        eq = eq.replace("-", "", 1)
    else:
        eq = eq.replace(str(a), "", 1)


    if (str(b) == "1"):
        print()
    elif (str(b) == "-1"):
        print()
        eq = eq.replace("-", "", 1)
    else:
        eq = eq.replace(str(b), "", 1)

    if (str(c) == "1"):
        print()
    elif (str(c) == "-1"):
        print()
        eq = eq.replace("-", "", 1)
    else:
        eq = eq.replace(str(c), "", 1)


    # eq = eq.replace("-", "")
    eq = eq.replace("+", "")
    if(isfloat(eq)):
        offset = eq
    else:
        offset = list(eq.split(" "))
        if(offset[0] == "" or offset[0] == " "):
            offset = ""

    #parse d
    d = parse_param(offset)

    return a, b, c, d


def parse_param(repr: typing.Union[list, list[str]]) -> int:
    """funksion ndihmes per te kontrolluar secilen nga vlera a,b,c,d
    Parameters
    ----------
        repr: list of string vlera e  kthyer nga regex

    Returns
    -------
        integer
            vlera e dhene e rikthyer mbas kontrollit
    """
    if not repr:
        return 0
    elif not repr[0]:  # i.e. just a blank ''
        return 1
    elif repr[0] == '-':
        return -1
    elif repr[0] == '+':
        return 1
    else:
        try:
            if (isfloat(repr)):
                number_to_return = float(repr)
                return number_to_return
        except:
            number_returning = float(repr[0])
            return int(number_returning)


def isfloat(num):
    if num.isdigit():
        return False
    elif num.replace('.', '', 1).isdigit() and num.count('.') < 2:
        return True
    else:
        return False


def solve(a, b, c, d):
    if (a == 0 and b == 0):  # Case for handling Liner Equation
        return np.array([f"x={(-d * 1.0) / c}"])  # Returning linear root as numpy array.

    elif (a == 0):  # Case for handling Quadratic Equations

        D = c * c - 4.0 * b * d  # Helper Temporary Variable
        if D >= 0:
            D = math.sqrt(D)
            x1 = (-c + D) / (2.0 * b)
            x2 = (-c - D) / (2.0 * b)
        else:
            D = math.sqrt(-D)
            x1 = (-c + D * 1j) / (2.0 * b)
            x2 = (-c - D * 1j) / (2.0 * b)

        return np.array([f"x1={x1}", f"x2={x2}"])  # Returning Quadratic Roots as numpy array.

    f = findF(a, b, c)  # Helper Temporary Variable
    g = findG(a, b, c, d)  # Helper Temporary Variable
    h = findH(g, f)  # Helper Temporary Variable

    if f == 0 and g == 0 and h == 0:  # All 3 Roots are Real and Equal
        if (d / a) >= 0:
            x = (d / (1.0 * a)) ** (1 / 3.0) * -1
        else:
            x = (-d / (1.0 * a)) ** (1 / 3.0)
        return (f"x={round(x)} x={round(x)} x={round(x)}")
        # return np.array([x, x, x])  # Returning Equal Roots as numpy array.

    elif h <= 0:  # All 3 roots are Real

        i = math.sqrt(((g ** 2.0) / 4.0) - h)  # Helper Temporary Variable
        j = i ** (1 / 3.0)  # Helper Temporary Variable
        k = math.acos(-(g / (2 * i)))  # Helper Temporary Variable
        L = j * -1  # Helper Temporary Variable
        M = math.cos(k / 3.0)  # Helper Temporary Variable
        N = math.sqrt(3) * math.sin(k / 3.0)  # Helper Temporary Variable
        P = (b / (3.0 * a)) * -1  # Helper Temporary Variable

        x1 = 2 * j * math.cos(k / 3.0) - (b / (3.0 * a))
        x2 = L * (M + N) + P
        x3 = L * (M - N) + P

        # return np.array([x1,x2,x3])  # Returning Real Roots as numpy array.
        return (f"x1={round(x1)} x2={round(x2)} x3={round(x3)}")

    elif h > 0:  # One Real Root and two Complex Roots
        R = -(g / 2.0) + math.sqrt(h)  # Helper Temporary Variable
        if R >= 0:
            S = R ** (1 / 3.0)  # Helper Temporary Variable
        else:
            S = (-R) ** (1 / 3.0) * -1  # Helper Temporary Variable
        T = -(g / 2.0) - math.sqrt(h)
        if T >= 0:
            U = (T ** (1 / 3.0))  # Helper Temporary Variable
        else:
            U = ((-T) ** (1 / 3.0)) * -1  # Helper Temporary Variable

        x1 = (S + U) - (b / (3.0 * a))
        x2 = -(S + U) / 2 - (b / (3.0 * a)) + (S - U) * math.sqrt(3) * 0.5j
        x3 = -(S + U) / 2 - (b / (3.0 * a)) - (S - U) * math.sqrt(3) * 0.5j

        return (f"x1={round(x1)} x2={round(x2)} x3={round(x3)}")

# Helper function to return float value of f.
def findF(a, b, c):
    return ((3.0 * c / a) - ((b ** 2.0) / (a ** 2.0))) / 3.0


# Helper function to return float value of g.
def findG(a, b, c, d):
    return (((2.0 * (b ** 3.0)) / (a ** 3.0)) - ((9.0 * b * c) / (a ** 2.0)) + (27.0 * d / a)) / 27.0


# Helper function to return float value of h.
def findH(g, f):
    return ((g ** 2.0) / 4.0 + (f ** 3.0) / 27.0)


if __name__ == "__main__":
    while(True):
        equation = input("Jepni funksionin: ")
        a = parse_eq(equation)[0]
        b = parse_eq(equation)[1]
        c = parse_eq(equation)[2]
        d = parse_eq(equation)[3]

        print(a,b,c,d)

        print(solve(a,b,c,d))


