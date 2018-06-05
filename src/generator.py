# -*- coding: utf-8 -*-

import random
import numpy as np

from individual import Individual


class Generator(object):

    def __init__(self, maximum, minimum, dimension):
        """constractor

        Args:
            maximum (float): 遺伝子の値の上限
            minimum (float): 遺伝子の値の下限
            dimension (int): 遺伝子長
        """

        self._maximum = maximum
        self._minimum = minimum
        self._dimension = dimension

    def generate(self):
        """初期遺伝子を作成する

        Returns:
            np.array: 生成した遺伝子
        """
        value_range = self._maximum - self._minimum
        return Individual([value_range * np.random.rand() + self._minimum
                           for _ in range(self._dimension)])
