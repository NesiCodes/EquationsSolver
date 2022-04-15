import re
import typing
import math

def parse_eq(eq: str) -> tuple[float, float]:
    """mer nje ekuacion nga perdoruesi dhe rikthen vlerat a,b
    Parameters
    ----------
        eq: string
            ekuacioni nga perdoruesi
    Returns
    -------
        vlerat a,b ne float
        vlerat boshe zevendesohen me 0
    """

    # strip all whitespaces and = 0 (not necessary)
    eq = ''.join(char for char in eq if char != ' ')
    eq = eq.replace("=0", "")

    # match the parameters
    linear = re.findall(r'([+-]*\d*)x(?!\^)', eq)
    # parse the parameters

    a = parse_param(linear)

    # offset = re.findall(r'[^\^]([+-]*\d+)(?![x}])', eq)
    # new_offset = offset[::-3]
    #find c
    eq = eq.replace("x", "")
    if(str(a) == "1"):
        print()
    elif(str(a) == "-1"):
        print()
        eq = eq.replace("-", "", 1)
    else:
        eq = eq.replace(str(a), "", 1)

    # eq = eq.replace("-", "")
    eq = eq.replace("+", "")
    if(isfloat(eq)):
        offset = eq
    else:
        offset = list(eq.split(" "))
        if(offset[0] == "" or offset[0] == " "):
            offset = ""

    #parse c
    b = parse_param(offset)

    return a, b


def parse_param(repr: typing.Union[list, list[str]]) -> int:
    """funksion ndihmes per te kontrolluar secilen nga vlera a,b,c
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


if __name__ == "__main__":
    while(True):
        equation = input("Jepni funksionin: ")
        a = parse_eq(equation)[0]
        b = parse_eq(equation)[1]
        
        print(a)
        print(b)