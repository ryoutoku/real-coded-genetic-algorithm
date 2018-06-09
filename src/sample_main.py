# -*- coding: utf-8 -*-

from society import Society
from evaluator import *
from individual_selector import *
from generation_selector import *
from crossover import *
from generator import *

import matplotlib.pyplot as plt
import matplotlib.animation as animation
from mpl_toolkits.mplot3d import Axes3D

import numpy as np


def get_generation_data(individual_list):
    x = [ind.gene[0] for ind in individual_list]
    y = [ind.gene[1] for ind in individual_list]
    return (x, y)


def plot_transition(x, y, generation_data):
    fig, (axL, _) = plt.subplots(ncols=2, figsize=(10, 4))

    # 左のプロット
    axL.plot(x, y, linewidth=2)
    axL.set_title('iterate - best value')
    axL.set_xlabel('iterate')
    axL.set_ylabel('evaluate value')
    axL.grid(True)

    # 右のプロット
    ims = []
    # for x, y in generation_list:
    for x, y in generation_data:
        im = plt.scatter(x, y, s=3, color='blue')
        ims.append([im])

    # なぜか代入する必要がある...
    _ = animation.ArtistAnimation(fig, ims, interval=50, repeat_delay=1000)
    plt.show()


def plot_evaluate_values(iterator_list, list_1, list_2):

    plt.plot(iterator_list, list_1)
    plt.plot(iterator_list, list_2)
    plt.show()


def demo_1():
    # 遺伝子長
    dimension = 30

    # 集団数
    individual_num = 300

    # 世代数の最大
    generation_loop = 1000

    # 評価関数
    evaluator = Sphere()

    # 次世代に残す個体の選択
    society = Society(
        evaluator,
        Simplex(dimension * 10),
        RouletteSelector(dimension + 1),
        JGG())
    generator = Generator(10., -10., dimension)

    # 初期個体の生成
    society.generate_individuals(individual_num, generator)

    # 画像データ表示用
    best_value = []
    iterate = []
    generation_data = []
    generation_data.append(get_generation_data(society.individuals))

    # 遺伝的操作を行う
    for i in range(generation_loop):
        society.change_generation()

        # 画像データ表示用処理
        best = society.get_best_individual()
        iterate.append(i)
        best_value.append(best.evaluate_value)
        generation_data.append(get_generation_data(society.individuals))

        best = society.get_best_individual()
        print(i, best.evaluate_value)

    # 最良評価値の推移を表示
    plot_transition(iterate, best_value, generation_data)


def demo_2():
    # 遺伝子長
    dimension = 30

    # 集団数
    individual_num = 300

    # 世代数の最大
    generation_loop = 1000

    # 評価関数
    evaluator = Rosenbrock()

    # 親の選択と交叉
    # 親の数は交叉方法に合わせて設定する

    # 次世代に残す個体の選択
    # Simplex, ルーレット選択
    society = Society(
        evaluator,
        Simplex(dimension * 10),
        RouletteSelector(dimension + 1),
        JGG())
    generator = Generator(10., -10., dimension)

    society.generate_individuals(individual_num, generator)

    # 初期個体の生成
    society.generate_individuals(individual_num, generator)

    # 画像データ表示用
    best_value = []
    iterate = []
    generation_data = []
    generation_data.append(get_generation_data(society.individuals))

    best = None
    for i in range(generation_loop):
        society.change_generation()

        # 画像データ表示用処理
        best = society.get_best_individual()
        iterate.append(i)
        best_value.append(best.evaluate_value)
        generation_data.append(get_generation_data(society.individuals))

        print(i, best.evaluate_value)

    # 最良評価値の推移を表示
    plot_transition(iterate, best_value, generation_data)


def demo_3():
    # 遺伝子長
    dimension = 30

    # 集団数
    individual_num = 300

    # 世代数の最大
    generation_loop = 1000

    # 評価関数
    evaluator = Rosenbrock()

    # 次世代に残す個体の選択
    society_simplex = Society(
        evaluator,
        Simplex(dimension * 10),
        RouletteSelector(dimension + 1),
        JGG())
    generator = Generator(10., -10., dimension)

    society_blx = Society(
        evaluator,
        BLX_alpha(dimension * 10),
        RouletteSelector(2),
        JGG())

    # 初期個体の生成
    society_simplex.generate_individuals(individual_num, generator)
    society_blx.generate_individuals(individual_num, generator)

    # 画像データ表示用
    simplex_data = []
    blx_data = []
    iterator_list = []

    # 初期個体のデータを保持
    best_simplex = society_simplex.get_best_individual()
    best_blx = society_blx.get_best_individual()
    simplex_data.append(best_simplex.evaluate_value)
    blx_data.append(best_blx.evaluate_value)
    iterator_list.append(0)

    for i in range(generation_loop):
        society_simplex.change_generation()
        society_blx.change_generation()

        # 画像データ表示用処理
        best_simplex = society_simplex.get_best_individual()
        best_blx = society_blx.get_best_individual()

        simplex_data.append(best_simplex.evaluate_value)
        blx_data.append(best_blx.evaluate_value)
        iterator_list.append(i+1)
        print(iterator_list[-1], simplex_data[-1], blx_data[-1])

    # 評価値の推移を表示
    plot_evaluate_values(iterator_list, simplex_data, blx_data)


if __name__ == "__main__":
    # demo_1()
    # demo_2()
    demo_3()
