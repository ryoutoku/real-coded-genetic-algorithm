# -*- coding: utf-8 -*-
import numpy as np


class Society(object):

    def __init__(self,
                 evaluator,
                 crossover,
                 parent_selector,
                 generation_selector
                 ):
        """constractor

        Args:
            evaluator (Evaluator): 評価関数
            crossover (Crossover): 交叉
            parent_selector (Selector): 親を選択するセレクタ
            generation_selector (Selector): 次世代を選択するセレクタ
        """

        self._evaluator = evaluator
        self._crossover = crossover
        self._parent_selector = parent_selector
        self._generation_selector = generation_selector
        self._individuals = None

    def generate_individuals(self, size, generator):
        """初期個体を生成する

        Args:
            size (int): 生成する個体数
            generator (function): 生成関数
        """
        self._individuals = [generator.generate() for _ in range(size)]

    def get_best_indivisual(self):
        """評価値の最良の個体を返す

        Returns:
            Individual: 評価値の最良の個体
        """

        tmp_evaluate = np.array([x for x.evaluate_value() in self._individuals])

        # ベンチマーク関数は評価値が低いものが評価値が良い
        return self._individuals[np.argmin(tmp_evaluate)]

    def change_generation(self):
        """世代交代を行う
        """

        # select parents index
        parents_index = self._parent_selector.select(self._individuals)

        # crossover
        children = crossover.crossover(self._individuals, parents)

        # select next generation from all individuals
        self._individuals = self._generation_selector.select(
            self._individuals, parents, children)
