"""
Author: Jesus A. Gonzalez
Description: Test class
Created: 10/09/2020
Last Modified: 10/09/2020
Description: Base class for statistical tests
"""

from AbstractTest import AbstractTest
from scipy.stats import kruskal


class KruskalWallisH(AbstractTest):

    def __init__(self):
        super().__init__("single")
        self.print_statistic.set_test_name("Kruskal-Wallis H")
        self.print_statistic.set_result_text("Equal")
        self.print_statistic.set_null_hypothesis("The distribution of all samples are equal")

    def evaluate_statistic(self, data):
        self.print_statistic.set_number_of_vectors(len(data))
        assert self.print_statistic.number_of_vectors >= 2, "This test if for two or more arrays of numbers"
        stat, p = kruskal(*data)
        self.print_statistic.set_statistic(stat)
        self.print_statistic.set_p_value(p)
        self.print_statistic.evaluate_hypothesis(self.print_statistic.p_value)
        self.print_statistic.print_result(self.print_statistic.decision)
