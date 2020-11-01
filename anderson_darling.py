"""
Author: Jesus A. Gonzalez
Description: Test class
Created: 10/09/2020
Last Modified: 10/09/2020
Description: Base class for statistical tests
"""
from AbstractTest import AbstractTest
from scipy.stats import anderson


class Anderson_Darling(AbstractTest):

    def __init__(self):
        super().__init__("multiple")
        self.print_statistic.set_test_name("Anderson Darling")
        self.print_statistic.set_result_text("Gaussian")
        self.print_statistic.set_null_hypothesis("The sample has a Gaussian distribution")

    def evaluate_statistic(self, data):
        self.print_statistic.set_number_of_vectors(1)
        assert self.print_statistic.number_of_vectors == 1, "This test if for a single array of numbers"
        result = anderson(data[0])
        statistic = result.statistic
        critical_values = result.critical_values
        significance_level = result.significance_level
        self.print_statistic.set_statistic(statistic)
        self.print_statistic.print_result_header()
        print("")
        for i in range(len(critical_values)):
            self.print_statistic.critical_value = critical_values[i]
            self.print_statistic.significance_level = significance_level[i]
            self.print_statistic.evaluate_hypothesis_critical(self.print_statistic.statistic, critical_values[i])
            self.print_statistic.print_result(self.print_statistic.decision)
