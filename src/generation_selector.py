# -*- coding: utf-8 -*-
from abc import ABCMeta, abstractmethod
import random
from individual_selector import *


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


class MGG(GenerationSelector):
    """Minimam Generation Gap による世代交代
    """

    def select(self, individuals, parents_list, children):
        """次世代に残す個体のリスト(集団)を返す
        親個体+子個体からエリート1個体、ルーレット1個体を選択し、親個体と入れ替える

        Args:
            individuals (list): 個体のリスト
            parents_list (list): 親個体のindexのリスト
            children (list): 生成した子個体
        """

        # 親となった個体を取得
        target = [individuals[x] for x in parents_list]

        # 次世代に加える候補を作成
        target.extend(children)

        remain = []
        # エリート選択とルーレット選択で次世代を追加
        elite = EliteSelector(1).select(target)
        remain.extend([target.pop(x) for x in elite])
        roulette = RouletteSelector(1).select(target)
        remain.extend([target.pop(x) for x in roulette])

        # 個体入れ替え
        for i, r in zip(index, remain):
            individuals[i] = r

        return individuals


class JGG(GenerationSelector):
    """Just Generation Gap による世代交代
    """

    def select(self, individuals, parents_list, children):
        """次世代に残す個体のリストを返す
        子個体からエリート個体を選択肢、親個体と入れ替える

        Args:
            individuals (list): 個体のリスト
            parents_list (list): 親個体のindexのリスト
            children (list): 生成した子個体
        """

        elite = EliteSelector(len(parents_list)).select(children)

        for p, e in zip(parents_list, elite):
            individuals[p] = children[e]

        return individuals
