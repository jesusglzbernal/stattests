"""
Author: Jesus A. Gonzalez
Description: Test class
Created: 10/09/2020
Last Modified: 10/09/2020
Description: Base class for statistical tests
"""

# Imports
from abc import ABC, abstractmethod
from print_statistic_behavior import PrintStatisticBehavior
import matplotlib.pyplot as plt
import seaborn as sns
import scipy.stats as stats


class AbstractTest(ABC, PrintStatisticBehavior):

    def __init__(self, print_behavior):
        super().__init__(print_behavior)

    @abstractmethod
    def evaluate_statistic(self, data):
        pass

    def plot_distribution(self, data, xlabel=""):
        plt.rcParams["figure.figsize"] = [10, 6]
        sns.set_style("darkgrid")
        sns.set_context("paper", font_scale=1.5, rc={"font.size":16, "axes.titlesize":16, "axes.labelsize":16})
        sns.distplot(data, fit=stats.norm, kde=False)
        plt.title('Histogram distribution')
        plt.xlabel(xlabel)
        plt.show()


