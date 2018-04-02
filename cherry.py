import matplotlib.pyplot as plt
from matplotlib.collections import PatchCollection
from matplotlib.patches import Polygon


def var_6():
    x1 = [-2, 0, 1, 4, 7, 8]

    e1 = lambda x1: (33 - 2 * x1) / 11
    e2 = lambda x1: (7 - x1)
    e3 = lambda x1: (4 * x1 - 5) / 5
    e4 = lambda x1: 0

    f1 = lambda x1: (- 10 * x1 + 12.5)
    f2 = lambda x1: (- 10 * x1 + 40)
    f3 = lambda x1: (- 10 * x1 + 70)

    fig, ax = plt.subplots()

    ax.plot(x1, list(map(e1, x1)))
    ax.plot(x1, list(map(e2, x1)))
    ax.plot(x1, list(map(e3, x1)))
    ax.plot(x1, list(map(e4, x1)), color='black')
    ax.plot([0, 0], [-1, 6], color='black')

    ax.plot(x1, list(map(f1, x1)))
    ax.plot(x1, list(map(f2, x1)))
    ax.plot(x1, list(map(f3, x1)))

    ax.add_collection(PatchCollection([Polygon([(1.25, 0), (4.07, 2.26), (4.9, 2.1), (7, 0)], closed=True)], alpha=0.4))

    ax.set_xlabel('x1')
    ax.set_ylabel('x2')

    ax.set_xlim((-2, 8))
    ax.set_ylim((-1, 6))

    axis = plt.gca()
    axis.text(2, -0.2, 'x1 = 0', fontdict={'fontsize': 9})
    axis.text(-0.25, 0.75, 'x2 = 0', fontdict={'fontsize': 9}, rotation=90)
    axis.text(1.9, 5.1, 'x1 + x2 = 7', fontdict={'fontsize': 9}, rotation=-47)
    axis.text(5, 3.8, '4x1 - 5x2 = 5', fontdict={'fontsize': 9}, rotation=40)
    axis.text(1.3, 2.83, '2x1 + 11x2 = 5', fontdict={'fontsize': 9}, rotation=-12)

    axis.text(0.7, 5.2, 'x2 = -10x1 + f(A)', fontdict={'fontsize': 9}, rotation=-84.3)
    axis.text(3.5, 5.2, 'x2 = -10x1 + 40', fontdict={'fontsize': 9}, rotation=-84.3)
    axis.text(6.65, 3.75, 'x2 = -10x1 + f(D)', fontdict={'fontsize': 9}, rotation=-84.3)

    axis.text(0.9, 0.1, 'A')
    axis.text(3.9, 2.4, 'B')
    axis.text(5, 2.2, 'C')
    axis.text(7.05, 0.1, 'D')

    ax.plot([1.25, 7, 4.07, 4.9], [0, 0, 2.26, 2.1], 'ro')

    plt.savefig('pie.png')

    plt.show()


def var_8():
    x1 = [-2, 0, 1, 4]

    e1 = lambda x1: (4 - 4 * x1) / 3
    e2 = lambda x1: (7 - 7 * x1) / 2
    e3 = lambda x1: 0

    fig, ax = plt.subplots()

    ax.plot(x1, list(map(e1, x1)))
    ax.plot(x1, list(map(e2, x1)))
    ax.plot(x1, list(map(e3, x1)))
    ax.plot([0, 0], [-1, 4])

    ax.add_collection(PatchCollection([Polygon([(1, 0), (0, 1.333), (0, 3.5)], closed=True)], alpha=0.4))

    ax.set_xlabel('x1')
    ax.set_ylabel('x2')

    ax.set_xlim((-2, 3))
    ax.set_ylim((-1, 4))

    axis = plt.gca()
    axis.text(0.2, -0.2, 'x1 = 0')
    axis.text(-0.15, 0.75, 'x2 = 0', rotation=90)
    axis.text(0.42, 2, '14x1 + 4x2 = 14', rotation=-68)
    axis.text(-1.3, 3.1, '200x1 + 150x2 = 200', rotation=-43.8)

    axis.text(0.09, 3.5, 'A')
    axis.text(-0.13, 1.2, 'C')
    axis.text(1.07, 0.1, 'B')

    ax.plot([0, 0, 1], [3.5, 1.333, 0], 'ro')

    plt.savefig('pie.png')

    plt.show()


if __name__ == '__main__':
    var_6()
