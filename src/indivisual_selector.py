# -*- coding: utf-8 -*-
from abc import ABCMeta, abstractmethod
import numpy as np
import random


class IndivisualSelector(metaclass=ABCMeta):
    """個体の選択方法のベース
    """

    def __init__(self, selection_num):
        self._selection_num = selection_num

    @abstractmethod
    def select(self, indivisuals):
        """選択した個体のリストを返す

        Args:
            indivisuals (list): 個体のリスト
        """
        pass


class EliteSelector(GenerationalSelector):
    """エリート選択による個体選択
    """

    def select(self, indivisuals):
        """選択した個体のリストを返す

        Args:
            indivisuals (list): 個体のリスト
        """

        evaluate_list = np.array([
            x.evaluate_value for x in indivisuals
        ])
        # 評価値の小さいものから選択する
        return np.argsort(evaluate_list)[:self._selection_num]


class RouletteSelector(GenerationalSelector):
    """ルーレット選択による個体選択
    """

    def select(self, indivisuals):
        """選択した個体のリストを返す

        Args:
            indivisuals (list): 個体のリスト
        """

        evaluate_list = np.array([
            x.evaluate_value for x in indivisuals
        ])

        # 評価値が小さいものを選択しやすくする必要がある
        evaluate_list = evaluate_list - np.max(evaluate_list)
        total = np.sum(evaluate_list)

        selected_index = []
        for _ in self._selection_num:
            threshold = random.uniform(0.0, total)

            sum = 0.0
            for index, value in enumerate(evaluate_list):
                sum += value
                if sum >= threshold:
                    # 選択されたindexは次の選択から除く
                    selected_index.append(index)
                    np.delete(evaluate_list, index)
                    total -= value
