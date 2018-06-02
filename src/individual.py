# -*- coding: utf-8 -*-

import numpy as np


class Individual(object):

    _evaluator = None

    def __init__(self, genome):
        self._genome = np.array(genome)
        self._evaluate_value = cls._evaluator.evaluate(evaluate_value)

    @classmethod
    def set_evaluator(cls, evaluator):
        cls._evaluator = evaluator

    @property
    def genome(self):
        """遺伝子
        """
        return self._genome

    @property
    def evaluate_value(self):
        """評価値
        """
        return self._evaluate_value
