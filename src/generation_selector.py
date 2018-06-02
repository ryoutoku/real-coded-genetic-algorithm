# -*- coding: utf-8 -*-
from abc import ABCMeta, abstractmethod
from .indivisual_selector import *


class GenerationSelector(ABCMeta):
    """次世代に残す個体の選択方法のベース
    """

    @abstractmethod
    def select(self, indivisuals, parents_list, children):
        """次世代に残す個体のリストを返す

        Args:
            indivisuals (list): 個体のリスト
            parents_list (list): 親個体のindexのリスト
            children (list): 生成した子個体
        """
        pass


class MMG(GenerationalSelector):
    """Minimam Generation Gap による世代交代
    """

    def select(self, indivisuals, parents_list, children):
        """次世代に残す個体のリストを返す

        Args:
            indivisuals (list): 個体のリスト
            parents_list (list): 親個体のindexのリスト
            children (list): 生成した子個体
        """

        # 集団から親を抽出
        parents = [indivisuals.pop(x) in x in parents_list]

        # 親の数分変更
        selection_num = len(parents)
