# -*- coding: utf-8 -*-

import numpy as np


class Individual(object):

    _evaluator = None

    def __init__(self, gene):
        self._gene = np.array(gene)
        self._evaluate_value = Individual._evaluator.evaluate(self)

    @classmethod
    def set_evaluator(cls, evaluator):
        Individual._evaluator = evaluator

    @property
    def gene(self):
        """遺伝子
        """
        return self._gene

    @property
    def evaluate_value(self):
        """評価値
        """
        return self._evaluate_value
