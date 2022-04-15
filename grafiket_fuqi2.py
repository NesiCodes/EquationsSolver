import ekuacione_fuqi2


def shfaq_grafikun(a, b, c):
    try:
        import matplotlib.pyplot as plt
        import math
        import numpy as np
        plt.style.use('seaborn-darkgrid')
        fig, ax = plt.subplots()
        d = b ** 2 - 4 * a * c
        convex_point = -b / (2 * a)
        x = np.linspace(-10, 11, 1000)
        # x = np.arange(-15.0, 15.0, 0.05)
        y = [(a * i ** 2 + b * i + c) for i in x]
        ax.plot(x, y)
        if (d == 0):
            convex_point = -b / (2 * a)  # it is the x-interceptor when det is 0
            convex_point2 = (-d) / (4 * a)
            ax.plot(convex_point, convex_point2, 'k-o')
            plt.text(convex_point, convex_point2, f"({convex_point};{convex_point2})")
            print('the convex point is at', convex_point, 'on the x-axis | the parabola intersect the y-axis at', c,
                  '| the determinant is 0')
        elif (d < 0):
            print('Determinant is', d, 'and if determinant is smaller than zero, there is no real solution')
        else:
            print("got here")
            convex_point2 = (-d)/(4*a)
            x_positive = (-b + math.sqrt(d)) / (2 * a) # y = 0
            x_negative = (-b - math.sqrt(d)) / (2 * a)  # y = 0
            print(convex_point)
            print(convex_point2)
            ax.plot(convex_point, convex_point2, 'k-o')
            ax.plot(x_positive, 0, 'k-o')
            ax.plot(x_negative, 0, 'k-o')
            plt.text(convex_point, convex_point2, f"({convex_point};{convex_point2})")
            plt.text(x_positive, 0, f"({x_positive};{0})")
            plt.text(x_negative, 0, f"({x_negative};{0})")
            print('the convex points is at', convex_point, 'on the x-axis |x_positive', x_positive, ' |x_negative',
                  x_negative, '| the parabola intersect the y-axis at', c)
        plt.show()
    except:
        print('try: import math')

if __name__ == "__main__":
    equation = "2x^2-3x+1=0"
    a = ek2.parse_eq(equation)[0]
    b = ek2.parse_eq(equation)[1]
    c = ek2.parse_eq(equation)[2]
    print(f"a:{a} b:{b} c:{c}")
    shfaq_grafikun(a,b,c)