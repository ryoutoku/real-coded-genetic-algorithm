# -*- coding: utf-8 -*-

import random
import numpy as np

from individual import Individual


def generate(maximum, minimum, dimension):
    """初期遺伝子を作成する

    Args:
        maximum (float): 遺伝子の値の上限
        minimum (float): 遺伝子の値の下限
        dimension (int): 遺伝子長

    Returns:
        np.array: 生成した遺伝子
    """
    value_range = maximum - minimum
    return Individual([value_range * np.random.rand() + minimum
                       for _ in range(dimension)])
