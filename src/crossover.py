# -*- coding: utf-8 -*-

from abc import ABCMeta, abstractmethod
import numpy as np
import .individuals import Individual


class Crossover(ABCMeta):

    def __init__(self, generate_size):
        """constractor

        Args:
            generate_size (int): 交叉によって生成する個体数
        """
        self._generate_size = generate_size

    @abstractmethod
    def crossover(self, individuals, parent_list):
        """交叉を実行する

        Args:
            individuals (Indivisuals): 交叉で使う個体

        Returns:
            list: 生成した子個体(list[Indivisual])
        """
        pass


class BLX_alpha(Crossover):

    def __init__(self, generate_size, alpha=0.3):
        super(BLX_alpha, self).__init__(generate_size)
        self._alpha = alpha

    def crossover(self, genome_list):
        """2個体(遺伝子)から子個体を生成する

        Args:
            indivisuals (list(Indivisual)): 個体のリスト
        """

        upper = []
        downer = []
        for gene_1, gene_2 in zip(genome_list[0], genome_list[1]):
            upper.append(max(gene_1, gene_2))
            downer.append(min(gene_1, gene_2))

        result = []
        for _ in range(self._generate_size):
