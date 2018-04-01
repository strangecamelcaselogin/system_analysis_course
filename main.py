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
    points = np.array([A, B, C, D, E])
    values = np.array([(f1(*p), f2(*p)) for p in points])

    fig, Dplot = plt.subplots()

    Dplot.add_collection(PatchCollection([Polygon(points, closed=True)], alpha=0.4))
    Dplot.set_title('D')
    Dplot.set_xlim((0, 5))
    Dplot.set_ylim((0, 5))
    Dplot.set_xlabel('x1')
    Dplot.set_ylabel('x2')

    plt.savefig('lr1_5.png')
    plt.show()

    fig, Fplot = plt.subplots()

    Fplot.add_collection(PatchCollection([Polygon(values, closed=True)], alpha=0.4))
    Fplot.set_title('F')
    Fplot.set_xlim((0, 14))
    Fplot.set_ylim((0, 14))
    Fplot.set_xlabel('f1')
    Fplot.set_ylabel('f2')

    plt.savefig('lr1_6.png')
    plt.show()


def lr1_variant_1_8():
    a1 = 1
    a2 = 3

    limit_x1_x2 = lambda x1: a2/2 - a2/a1 * (x1 - a1)
    limit_x2 = lambda x1: a2

    f1 = lambda x1, x2: x1**3 + x2 ** 2
    f2 = lambda x1, x2: x1 + x2 ** (1/2)

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

    plt.savefig('lr1_3.png')
    plt.show()

    fig, Fplot = plt.subplots()

    Fplot.add_collection(PatchCollection([Polygon(values, closed=True)], alpha=0.4))
    Fplot.set_title('F')
    Fplot.set_xlim((0, 18))
    Fplot.set_ylim((0, 5))
    Fplot.set_xlabel('f1')
    Fplot.set_ylabel('f2')

    plt.savefig('lr1_4.png')
    plt.show()


def lr1():
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

    plt.savefig('lr1_1.png')
    plt.show()

    fig, Fplot = plt.subplots()

    Fplot.add_collection(PatchCollection([Polygon(values, closed=True)], alpha=0.4))
    Fplot.set_title('F')
    Fplot.set_xlim((0, 8))
    Fplot.set_ylim((0, 8))
    Fplot.set_xlabel('f1')
    Fplot.set_ylabel('f2')

    plt.savefig('lr1_2.png')
    plt.show()


if __name__ == '__main__':
    lr1()

    lr1_variant_1_8()
    lr1_variant_1_2()
