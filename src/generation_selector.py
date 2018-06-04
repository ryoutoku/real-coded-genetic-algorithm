# -*- coding: utf-8 -*-
from abc import ABCMeta, abstractmethod
import random
import indivisual_selector import *


class GenerationSelector(metaclass=ABCMeta):
    """次世代に残す個体の選択方法のベース
    """

    @abstractmethod
    def select(self, individuals, parents_list, children):
        """次世代に残す個体のリストを返す

        Args:
            individuals (list): 個体のリスト
            parents_list (list): 親個体のindexのリスト
            children (list): 生成した子個体
        """
        pass

        parents = [individuals.pop(x) in x in parents_list]


class MMG(GenerationalSelector):
    """Minimam Generation Gap による世代交代
    """

    def select(self, individuals, parents_list, children):
        """次世代に残す個体のリストを返す

        Args:
            individuals (list): 個体のリスト
            parents_list (list): 親個体のindexのリスト
            children (list): 生成した子個体
        """

        # 集団から除かれる候補の親を選出し、除く
        index = random.sample(parents_list, 2)
        [individuals.pop(x) for x in index]

        # 次世代に残る候補
        target = [parents_list[x] for x in index] + children

        # エリート選択とルーレット選択で次世代を追加
        elite = EliteSelector(1).select(target)
        individuals.append(target.pop(elite))
        roulette = RouletteSelector(1).select(target)
        individuals.append(target.pop(roulette))
