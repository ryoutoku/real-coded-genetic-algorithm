# -*- coding: utf-8 -*-

from abc import ABCMeta, abstractmethod
import numpy as np
import random
import individual import Individual


class Crossover(metaclass=ABCMeta):

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
            individuals (Indivisual): 個体群
            parent_list (list): 個体群の中から使用する親

        Returns:
            list: 生成した子個体(list[Indivisual])
        """
        pass


class BLX_alpha(Crossover):

    def __init__(self, generate_size, alpha=0.3):
        super(BLX_alpha, self).__init__(generate_size)
        self._alpha = alpha

    def crossover(self, individuals, parent_list):
        """2個体から子個体を生成する

        Args:
            indivisuals (list(Indivisual)): 個体のリスト
        """
        matrix = np.array([individuals[x].gene for x in parent_list[:2]])
        gene_max = matrix.max(axis=0)
        gene_min = matrix.min(axis=0)
        gene_mean = matrix.mean(axis=0)

        result = []
        for _ in range(self._generate_size):
            gene = [
                random.uniform(gene_min, gene_max) * self._alpha * gene_mean
                for gene_max, gene_min, gene_men in zip(gene_max, gene_min, gene_mean)]
            result.append(Individual(gene))

        return result


class Simplex(Crossover):

    def __init__(self, generate_size, epsilon=0.3):
        super(Simplex, self).__init__(generate_size)
        self._alpha = alpha

    def crossover(self, individuals, parent_list):
        """次元数+1個体から子個体を生成する

        Args:
            indivisuals (list(Indivisual)): 個体のリスト
        """

        matrix = np.array([individuals[x].gene for x in parent_list])

        result = []
        for _ in range(self._generate_size):
            gene = [random.uniform(x[1], x[0]) * self._alpha * x[2] for
                    x in gene_value]
            result.append(Individual(gene))

        return result
