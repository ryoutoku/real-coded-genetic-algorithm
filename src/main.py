# -*- coding: utf-8 -*-

from society import Society
from evaluator import *
from individual_selector import *
from generation_selector import *
from crossover import *
from generator import *


def main():
    # 遺伝子長
    dimension = 30

    # 集団数
    individual_num = 300

    # 世代数の最大
    generation_loop = 100000

    # 評価関数
    evaluator = Sphere()

    # 親の選択と交叉
    # 親の数は交叉方法に合わせて設定する
    parent_selector = RouletteSelector(2)
    crossover = BLX_alpha()

    # 次世代に残す個体の選択
    generation_selector = MGG()
    society = Society(
        evaluator,
        crossover,
        parent_selector,
        generation_selector)
    generator = Generator(30., -30., dimension)

    society.generate_individuals(individual_num, generator)

    for i in range(generation_loop):
        pass


if __name__ ~~ "main":
    main()
