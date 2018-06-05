from crossover import BLX_alpha, Simplex
from evaluator import Sphere
from individual import Individual

import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# 個体生成前に宣言する必要あり
evaluator = Sphere()

l = [Individual([0, 0, 0]), Individual([3, 3, 3]),
     Individual([-3, 3, -3]), Individual([3, 3, -3])]


def plot_blx_alpha():
    cx = BLX_alpha(600)
    tmp = cx.crossover(l, [0, 1])

    x = [x.gene[0] for x in tmp]
    y = [x.gene[1] for x in tmp]
    z = [x.gene[2] for x in tmp]
    p_x = [x.gene[0] for x in l[:2]]
    p_y = [x.gene[0] for x in l[:2]]
    p_z = [x.gene[0] for x in l[:2]]
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.scatter3D(x, y, z, s=5, c='blue')
    ax.scatter3D(p_x, p_y, p_z, s=20, c='red')
    plt.show()


def plot_simplex():
    cx = Simplex(600)
    tmp = cx.crossover(l, [0, 1, 2, 3])

    x = [x.gene[0] for x in tmp]
    y = [x.gene[1] for x in tmp]
    z = [x.gene[2] for x in tmp]
    p_x = [x.gene[0] for x in l]
    p_y = [x.gene[1] for x in l]
    p_z = [x.gene[2] for x in l]

    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.scatter3D(x, y, z, s=5, c='blue')
    ax.scatter3D(p_x, p_y, p_z, s=20, c='red')
    plt.show()


plot_simplex()
