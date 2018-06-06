# -*- coding: utf-8 -*-

from society import Society
from evaluator import *
from individual_selector import *
from generation_selector import *
from crossover import *
from generator import *

import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


def main():
    # 遺伝子長
    dimension = 30

    # 集団数
    individual_num = 300

    # 世代数の最大
    generation_loop = 1000

    # 評価関数
    evaluator = Sphere()
    evaluator = Rosenbrock()

    # 親の選択と交叉
    # 親の数は交叉方法に合わせて設定する
    roulette = RouletteSelector(2)
    blx = BLX_alpha(dimension * 10)

    # 次世代に残す個体の選択
    society = Society(
        evaluator,
        blx,
        roulette,
        JGG())
    generator = Generator(10., -10., dimension)

    society.generate_individuals(individual_num, generator)
    plot(society.individuals)

    for i in range(generation_loop):
        society.change_generation()
        ind = society.get_best_individual()
        print(i, ind.evaluate_value)

    plot(society.individuals)


def plot(Individuals):
    x = [x.gene[0] for x in Individuals]
    y = [x.gene[1] for x in Individuals]
    plt.scatter(x, y, s=5)
    plt.show()


if __name__ == "__main__":
    main()
