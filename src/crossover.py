# -*- coding: utf-8 -*-

from abc import ABCMeta, abstractmethod
import random
import math
import numpy as np
from individual import Individual


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
            individuals (Individual): 個体群
            parent_list (list): 個体群の中から使用する親

        Returns:
            list: 生成した子個体(list[Individual])
        """
        pass


class BLX_alpha(Crossover):

    def __init__(self, generate_size, alpha=0.3):
        super(BLX_alpha, self).__init__(generate_size)
        self._alpha = alpha

    def crossover(self, individuals, parent_list):
        """2個体から子個体を生成する

        Args:
            individuals (list(Individual)): 個体のリスト
        """
        matrix = np.array([individuals[x].gene for x in parent_list[:2]])
        gene_max = matrix.max(axis=0)
        gene_min = matrix.min(axis=0)
        gene_abs = np.abs(gene_max - gene_min)

        gene_max = gene_max + self._alpha * gene_abs
        gene_min = gene_min - self._alpha * gene_abs

        result = []
        for _ in range(self._generate_size):
            gene = [
                random.uniform(g_min, g_max)
                for g_max, g_min in zip(gene_max, gene_min)]
            result.append(Individual(gene))

        return result


class Simplex(Crossover):

    def crossover(self, individuals, parent_list):
        """次元数+1個体から子個体を生成する

        Args:
            individuals (list(Individual)): 個体のリスト
        """

        # 重心として親の各変数の平均を取る
        matrix = np.array([individuals[x].gene for x in parent_list])
        center = matrix.mean(axis=0)

        dimension = len(center)
        epsilon = math.sqrt(dimension + 2)
        matrix = center + epsilon * (matrix - center)

        result = []
        for _ in range(self._generate_size):
            gene = np.zeros(dimension)
            for k, (vector1, vector2) in enumerate(zip(matrix, matrix[1:])):
                r_k = random.uniform(0., 1.) ** (1./(k+1))
                gene = r_k * (vector1 - vector2 + gene)
            gene += matrix[-1]
            result.append(Individual(gene))

        return result
