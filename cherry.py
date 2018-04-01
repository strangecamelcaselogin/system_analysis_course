import matplotlib.pyplot as plt
from matplotlib.collections import PatchCollection
from matplotlib.patches import Polygon


if __name__ == '__main__':
    e1 = lambda x1: (4 - 4 * x1) / 3
    e2 = lambda x1: (7 - 7 * x1) / 2
    e3 = lambda x1: 0

    x1 = [-2, 0, 1, 4]

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

    plt.savefig('pie.png')

    plt.show()
