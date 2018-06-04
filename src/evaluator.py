# -*- coding: utf-8 -*-
from abc import ABCMeta, abstractmethod
import math

from individual import Individual


class Evaluator(metaclass=ABCMeta):

    def __init__(self):
        Individual.set_evaluator(self)

    def evaluate(self, individual):
        """個体を評価する

        Args:
            individual (individual): 評価する個体

        Returns:
            float: 評価値
        """
        return self._evaluate_function(individual.gene)

    @abstractmethod
    def _evaluate_function(self, gene):
        """実際に個体を評価する実態

        Args:
            gene (np.array): 評価する遺伝子
        """
        pass


class Sphere(Evaluator):

    def _evaluate_function(self, gene):
        """Sphere関数として評価する
        f(x_1...x_n) = x_1**2 + x_2**2 + ... x_n**2

        Args:
            gene (np.array): 評価する遺伝子

        Returns:
            float: 評価値
        """
        return (gene**2).sum()


class Rosenbrock(Evaluator):

    def _evaluate_function(self, gene):
        """Rosenbrock関数として評価する
        f(x_1...x_n = 100(x_2 - x_1**2)**2 + (x_1 - 1)**2 + ...
        Args:
            gene (np.array): 評価する遺伝子

        Returns:
            float: 評価値
        """

        result = 0.0
        for gene_1, gene_2 in zip(gene, gene[1:]):
            result += 100.0 * (gene_2 - gene_1**2) ** 2 + (gene_1 - 1)**2
        return result
