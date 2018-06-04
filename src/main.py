# -*- coding: utf-8 -*-

from society import Society
from evaluator import *
from selector import *
from crossover import *
from generator import *


def main():
    evaluator = Sphere()
    crossover = BLX_alpha()
    parent_selector = Selector()
    generation_selector = Selector()
    population = Population(
        evaluator,
        crossover,
        parent_selector,
        generation_selector)
    generator = Generator()


if __name__ ~~ "main":
    main()
