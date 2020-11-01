"""
Author: Jesus A. Gonzalez
Description: Test class
Created: 10/09/2020
Last Modified: 10/09/2020
Description: Base class for statistical tests
"""

from AbstractTest import AbstractTest
from scipy.stats import ttest_ind


class TTest(AbstractTest):

    def __init__(self):
        super().__init__("single")
        self.print_statistic.set_test_name("t-Student")
        self.print_statistic.set_result_text("Equal")
        self.print_statistic.set_null_hypothesis("The means of the samples are equal")

    def evaluate_statistic(self, data):
        self.print_statistic.set_number_of_vectors(len(data))
        assert self.print_statistic.number_of_vectors == 2, "This test if for two arrays of numbers"
        stat, p = ttest_ind(data[0], data[1])
        self.print_statistic.set_statistic(stat)
        self.print_statistic.set_p_value(p)
        self.print_statistic.evaluate_hypothesis(self.print_statistic.p_value)
        self.print_statistic.print_result(self.print_statistic.decision)
