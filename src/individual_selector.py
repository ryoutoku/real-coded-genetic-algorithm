# -*- coding: utf-8 -*-
from abc import ABCMeta, abstractmethod
import numpy as np
import random


class Individualselector(metaclass=ABCMeta):
    """個体の選択方法のベース
    """

    def __init__(self, selection_num):
        self._selection_num = selection_num

    @abstractmethod
    def select(self, individuals):
        """選択した個体のリストを返す

        Args:
            individuals (list): 個体のリスト
        """
        pass


class EliteSelector(Individualselector):
    """エリート選択による個体選択
    """

    def select(self, individuals):
        """選択した個体のリストを返す

        Args:
            individuals (list): 個体のリスト
        """
        evaluate_list = np.array([
            x.evaluate_value for x in individuals
        ])
        # 評価値の小さいものから選択する
        return np.argsort(evaluate_list)[:self._selection_num]


class RouletteSelector(Individualselector):
    """ルーレット選択による個体選択
    """

    def select(self, individuals):
        """選択した個体のリストを返す

        Args:
            individuals (list): 個体のリスト
        """

        evaluate_list = np.array([
            x.evaluate_value for x in individuals
        ])

        # 評価値が小さいものを選択しやすくする必要がある
        evaluate_list = np.abs(evaluate_list - np.max(evaluate_list))
        total = np.sum(evaluate_list)

        selected_index = []
        for _ in range(self._selection_num):
            threshold = random.uniform(0.0, total)

            sum = 0.0
            for index, value in enumerate(evaluate_list):
                sum += value
                if sum >= threshold:
                    # 選択されたindexは次の選択から除く
                    selected_index.append(index)
                    evaluate_list[index] = 0.
                    total -= value
                    break
        return selected_index
