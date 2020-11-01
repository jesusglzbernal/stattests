"""
Author: Jesus A. Gonzalez
Description: Test class
Created: 10/09/2020
Last Modified: 10/09/2020
Description: Base class for statistical tests
"""

from AbstractTest import AbstractTest
from statsmodels.tsa.stattools import adfuller


class DickeyFuller(AbstractTest):

    def __init__(self):
        super().__init__("multiple")
        self.print_statistic.set_test_name("Dickey Fuller")
        self.print_statistic.set_result_text("Stationary")
        self.print_statistic.set_null_hypothesis("A unit root is present - (Series is non-stationary")

    def evaluate_statistic(self, data):
        self.print_statistic.set_number_of_vectors(1)
        assert self.print_statistic.number_of_vectors == 1, "This test if for a single array of numbers"
        statistic, p_value, lags, nobs, critical_values, icbest = adfuller(data[0])
        self.print_statistic.set_statistic(statistic)
        self.print_statistic.print_result_header()
        print("")
        for key, val in critical_values.items():
            self.print_statistic.critical_value = val
            self.print_statistic.significance_level = key
            self.print_statistic.evaluate_hypothesis_critical(self.print_statistic.statistic,
                                                              self.print_statistic.critical_value)
            self.print_statistic.print_result(self.print_statistic.decision)
