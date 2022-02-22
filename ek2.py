import re
import typing
import math


def parse_eq(eq: str) -> tuple[float, float, float]:
    """parse a quadratic equation and return the parameters
    Parameters
    ----------
        eq: string
            the quadratic equation to parse

    Returns
    -------
        triple of integer
            the parameters in descending order of power of x
            missing parameters are substituted with 0
    """

    # strip all whitespaces and remove = and 0(bcs they are not needed)
    eq = ''.join(char for char in eq if char != ' ')
    eq = eq.replace("=", "")
    eq = eq.replace("0", "")

    # match the parameters
    square = re.findall(r'([+-]*\d*)x\^', eq)
    linear = re.findall(r'([+-]*\d*)x(?!\^)', eq)
    offset = re.findall(r'[^\^]([+-]*\d+)(?![x}])', eq)
    new_offset = offset[::-3]



    # parse the parameters
    a = parse_param(square)
    b = parse_param(linear)
    c = parse_param(new_offset)

    return a, b, c


def parse_param(repr: typing.Union[list, list[str]]) -> int:
    """helper function to parse a single parameter
    Parameters
    ----------
        repr: optional list of string
            the regex match from the parent function

    Returns
    -------
        integer
            the parsed parameter
    """

    if not repr:
        return 0
    elif not repr[0]:  # i.e. just a blank ''
        return 1
    elif repr[0] == '-':
        return -1
    else:
        return int(repr[0])



# Finding the roots using the Function
def roots_of_equation(a, b, c):
    print(a)
    print(b)
    print(c)
    # Finding the value of Discriminant
    D = b**2 - 4*a*c
    # print(D)

    sqrt_D = math.sqrt(abs(D))

    # checking Discriminant condition
    if D > 0:
        x1=(-b + sqrt_D) / (2 * a)
        x2=(-b - sqrt_D) / (2 * a)
        return f"x1={x1} x2={x2}"
        # print("Roots are Real and Different ")
        # print((-b + sqrt_D) / (2 * a))
        # print((-b - sqrt_D) / (2 * a))


    elif D == 0:
        x=-b / (2 * a)
        return f"x={x}"
        # print(" real and same roots")
        # print(-b / (2 * a))

        # Discriminant < 0 follows else block

    else:
        x1=- b / (2 * a), " + i", sqrt_D
        x2=- b / (2 * a), " - i", sqrt_D
        return f"Complex x1={x1} x2={x2}"
        # print("Complex Roots")
        # print(- b / (2 * a), " + i", sqrt_D)
        # print(- b / (2 * a), " - i", sqrt_D)


# equation = input("Jepni funksionin: ")
# a = parse_eq(equation)[0]
# b = parse_eq(equation)[1]
# c = parse_eq(equation)[2]
#
# roots_of_equation(a,b,c)

