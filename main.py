import numpy as np
from scipy.optimize import fsolve
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon
from matplotlib.collections import PatchCollection


def lr1_variant_1_2():
    a1 = 1
    a2 = 2

    limit_x1_x2 = lambda x1: a2/2 - a2/a1 * (x1 - a1)
    limit_x2 = lambda x1: a2

    f1 = lambda x1, x2: x1**3 + 2 * x2 ** 2
    f2 = lambda x1, x2: 6 * x1 + x2 ** 3

    A = (0, 0)
    B = (0, a2)
    C = (fsolve(lambda x1: limit_x2(x1) - limit_x1_x2(x1), 0)[0], a2)
    D = (a1, limit_x1_x2(a1))
    E = (a1, 0)

    points = np.array([A,  B, C, D,  E,])
    values = np.array([(f1(*p), f2(*p)) for p in points])

    fig, Dplot = plt.subplots()

    Dplot.add_collection(PatchCollection([Polygon(points, closed=True)], alpha=0.4))
    Dplot.set_title('D')
    Dplot.set_xlim((0, 5))
    Dplot.set_ylim((0, 5))
    Dplot.set_xlabel('x1')
    Dplot.set_ylabel('x2')

    Daxis = plt.gca()
    Daxis.text(-0.06, -0.1, 'A')
    Daxis.text(-0.1, 2.1, 'B')
    Daxis.text(0.5, 2.1, 'C')
    Daxis.text(1.1, 1.1, 'D')
    Daxis.text(1.1, 0.1, 'E')

    Dplot.plot([0.0, 0, 0.5, 1, 1], [0.0, 2, 2, 1, 0], 'bx')

    plt.savefig('lr2-2_1.png')
    plt.show()

    fig, Fplot = plt.subplots()

    Fplot.add_collection(PatchCollection([Polygon(values, closed=True)], alpha=0.4))
    Fplot.set_title('F')
    Fplot.set_xlim((0, 14))
    Fplot.set_ylim((0, 14))
    Fplot.set_xlabel('f1')
    Fplot.set_ylabel('f2')

    Faxis = plt.gca()
    Faxis.text(-0.2, -0.11, 'f(A)')
    Faxis.text(1, 6.1, 'f(E)')
    Faxis.text(3.7, 7.1, 'f(D)')
    Faxis.text(8.2, 11.1, 'f(C)')
    Faxis.text(8.1, 7.8, 'f(B)')

    Fplot.plot([0.0, 1, 3, 8.125, 8], [0.0, 6, 7, 11, 8], 'bx')

    plt.savefig('lr2-2_2.png')
    plt.show()


def lr1_variant_1_8():
    a1 = 1
    a2 = 3

    limit_x1_x2 = lambda x1: a2/2 - a2/a1 * (x1 - a1)
    limit_x2 = lambda x1: a2

    f1 = lambda x1, x2: x1**3 + x2 ** 2
    f2 = lambda x1, x2: x1 + x2 ** (1/2)

    line = lambda f1: 0.196 / 0.804 * f1
    solves = lambda f2: 2.23

    A = (0, 0)
    B = (0, a2)
    C = (fsolve(lambda x1: limit_x2(x1) - limit_x1_x2(x1), 0)[0], a2)
    D = (a1, limit_x1_x2(a1))
    E = (a1, 0)
    points = np.array([A, B, C, D, E])
    values = np.array([(f1(*p), f2(*p)) for p in points])

    fig, Dplot = plt.subplots()

    Dplot.add_collection(PatchCollection([Polygon(points, closed=True)], alpha=0.4))
    Dplot.set_title('D')
    Dplot.set_xlim((0, 3))
    Dplot.set_ylim((0, 4))
    Dplot.set_xlabel('x1')
    Dplot.set_ylabel('x2')

    Daxis = plt.gca()
    Daxis.text(-0.06, -0.1, 'A')
    Daxis.text(-0.1, 3.1, 'B')
    Daxis.text(0.5, 3.1, 'C')
    Daxis.text(1.1, 1.7, 'D')
    Daxis.text(1.1, 0.1, 'E')

    Dplot.plot([0.0, 0, 0.5, 1, 1], [0.0, 3, 3, 1.55, 0], 'bx')

    plt.savefig('lr1-8_1.png')
    #plt.show()

    fig, Fplot = plt.subplots()

    Fplot.add_collection(PatchCollection([Polygon(values, closed=True)], alpha=0.4))
    Fplot.set_title('F')
    Fplot.set_xlim((0, 10))
    Fplot.set_ylim((0, 3))
    Fplot.set_xlabel('f1')
    Fplot.set_ylabel('f2')

    Fplot.plot([-1, 10], list(map(line, [-1, 10])))
    Fplot.plot([3.25, 9.125], list(map(solves, [3.25, 9.125])))

    Faxis = plt.gca()
    Faxis.text(-0.2, -0.11, 'f(A)')
    Faxis.text(8.9, 1.5, 'f(B)')
    Faxis.text(9.125, 2.3, 'f(C)')
    Faxis.text(3.15, 2.3, 'f(D)')
    Faxis.text(0.9, 1.1, 'f(E)')

    Fplot.plot([0.0, 9, 9.125, 3.25, 1], [0.0, 1.75, 2.22, 2.22, 1], 'bx')

    plt.savefig('lr1-8_2.png')
    plt.show()


def lr1_3():
    a1 = 1.4
    a2 = 2.2

    limit_x1_x2 = lambda x1: a2/2 - a2/a1 * (x1 - a1)
    limit_x2 = lambda x1: a2

    f1 = lambda x1, x2: 2 * x1**2 + x1 * x2
    f2 = lambda x1, x2: x1 + x2

    A = (0, 0)
    B = (0, a2)
    C = (fsolve(lambda x1: limit_x2(x1) - limit_x1_x2(x1), 0)[0], a2)
    D = (a1, limit_x1_x2(a1))
    E = (a1, 0)
    points = np.array([A, B, C, D, E])
    values = np.array([(f1(*p), f2(*p)) for p in points])

    fig, Dplot = plt.subplots()

    Dplot.add_collection(PatchCollection([Polygon(points, closed=True)], alpha=0.4))
    Dplot.set_title('D')
    Dplot.set_xlim((0, 5))
    Dplot.set_ylim((0, 5))
    Dplot.set_xlabel('x1')
    Dplot.set_ylabel('x2')


    Daxis = plt.gca()
    Daxis.text(-0.06, -0.1, 'A')
    Daxis.text(-0.1, 2.3, 'B')
    Daxis.text(0.7, 2.3, 'C')
    Daxis.text(1.5, 1.3, 'D')
    Daxis.text(1.4, 0.1, 'E')

    Dplot.plot([0.0, 0, 0.7, 1.4, 1.4], [0.0, 2.2, 2.2, 1.2, 0], 'bx')

    plt.savefig('lr2-3_1.png')
    #plt.show()

    fig, Fplot = plt.subplots()

    Fplot.add_collection(PatchCollection([Polygon(values, closed=True)], alpha=0.4))
    Fplot.set_title('F')
    Fplot.set_xlim((0, 8))
    Fplot.set_ylim((0, 8))
    Fplot.set_xlabel('f1')
    Fplot.set_ylabel('f2')

    Faxis = plt.gca()
    Faxis.text(0.1, 0.07, 'f(A)')
    Faxis.text(-0.1, 2.3, 'f(B)')
    Faxis.text(2.7, 2.9, 'f(C)')
    Faxis.text(5.56, 2.4, 'f(D)')
    Faxis.text(4, 1, 'f(E)')

    Fplot.plot([0.0, 0.0, 2.55, 5.46, 3.92], [0.0, 2.2, 2.9, 2.5, 1.4], 'bx')

    plt.savefig('lr2-3_2.png')
    #plt.show()


def lr1_6():
    a1 = 2
    a2 = 1.4

    limit_x1_x2 = lambda x1: a2/2 - a2/a1 * (x1 - a1)
    limit_x2 = lambda x1: a2

    f1 = lambda x1, x2: 0.5 * x1 * x2
    f2 = lambda x1, x2: x1 * x2**2

    line = lambda f1: 0.737/0.263 * f1

    A = (0, 0)
    B = (0, a2)
    C = (fsolve(lambda x1: limit_x2(x1) - limit_x1_x2(x1), 0)[0], a2)
    D = (a1, limit_x1_x2(a1))
    E = (a1, 0)
    points = np.array([A, B, C, D, E])
    values = np.array([(f1(*p), f2(*p)) for p in points])

    fig, Dplot = plt.subplots()

    Dplot.add_collection(PatchCollection([Polygon(points, closed=True)], alpha=0.4))
    Dplot.set_title('D')
    Dplot.set_xlim((0, 5))
    Dplot.set_ylim((0, 5))
    Dplot.set_xlabel('x1')
    Dplot.set_ylabel('x2')

    Daxis = plt.gca()
    Daxis.text(-0.06, -0.1, 'A')
    Daxis.text(-0.1, 1.5, 'B')
    Daxis.text(1, 1.5, 'C')
    Daxis.text(2.1, 0.7, 'D')
    Daxis.text(2.1, -0.1, 'E')

    Dplot.plot([0.0, 0, 1, 2, 2], [0.0, 1.4, 1.4, 0.7, 0], 'bx')

    plt.savefig('lr1-6_1.png')
    plt.show()

    fig, Fplot = plt.subplots()

    Fplot.add_collection(PatchCollection([Polygon(values, closed=True)], alpha=0.4))
    Fplot.set_title('F')
    Fplot.set_xlim((0, 3))
    Fplot.set_ylim((0, 3))
    Fplot.set_xlabel('f1')
    Fplot.set_ylabel('f2')

    Fplot.plot([-1, 5], list(map(line, [-1, 5])))
    Fplot.plot([0.7, 0.7], [0.98, 1.96], color='black')

    Faxis = plt.gca()
    Faxis.text(0.1, 0.07, 'f(A, B, E)')
    Faxis.text(0.75, 1.96, 'f(C)')
    Faxis.text(0.75, 0.98, 'f(D)')

    Fplot.plot([0.0, 0.7, 0.7], [0.0, 1.96, 0.98], 'bx')

    plt.savefig('lr1-6_2.png')
    plt.show()

if __name__ == '__main__':
    #lr1_6()
    lr1_3()

    #lr1_variant_1_8()
    #lr1_variant_1_2()
