"""
Author: Jesus A. Gonzalez
Description: Test class
Created: 10/09/2020
Last Modified: 10/09/2020
Description: Base class for statistical tests
"""

from AbstractTest import AbstractTest
from scipy.stats import chi2_contingency


class ChiSquared(AbstractTest):

    def __init__(self):
        super().__init__("single")
        self.print_statistic.set_test_name("Chi^2")
        self.print_statistic.set_result_text("Independent")
        self.print_statistic.set_null_hypothesis("The two samples are independent")

    def evaluate_statistic(self, data):
        self.print_statistic.set_number_of_vectors(len(data))
        #assert self.print_statistic.number_of_vectors[[0]] > 1, "This test requires 2 arrays of numbers"
        print(data)
        stat, p, dof, expected = chi2_contingency(data)
        self.print_statistic.set_statistic(stat)
        self.print_statistic.set_p_value(p)
        self.print_statistic.evaluate_hypothesis(self.print_statistic.p_value)
        self.print_statistic.print_result(self.print_statistic.decision)


