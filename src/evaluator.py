# -*- coding: utf-8 -*-
from abc import ABCMeta, abstractmethod
import math


class Evaluator(ABCMeta):

    def evaluate(self, individual):
        """個体を評価する

        Args:
            individual (Indivisual): 評価する個体

        Returns:
            float: 評価値
        """
        return self._evaluate_function(individual.genome)

    def _evaluate_function(self, genome):
        """実際に個体を評価する実態

        Args:
            genome (np.array): 評価する遺伝子
        """
        pass


class Sphere(Evaluator):

    def _evaluate_function(self, genome):
        """Sphere関数として評価する
        f(x_1...x_n) = x_1**2 + x_2**2 + ... x_n**2

        Args:
            genome (np.array): 評価する遺伝子

        Returns:
            float: 評価値
        """
        return (genome**2).sum()


class Rosenbrock(Evaluator):

    def _evaluate_function(self, genome):
        """Rosenbrock関数として評価する
        f(x_1...x_n = 100(x_2 - x_1**2)**2 + (x_1 - 1)**2 + ...
        Args:
            genome (np.array): 評価する遺伝子

        Returns:
            float: 評価値
        """

        result = 0.0
        for gene_1, gene_2 in zip(genome, genome[1:]):
            result += 100.0 * (gene_2 - gene_1**2) ** 2 + (gene_1 - 1)**2
        return result
