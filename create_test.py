import numpy as np
from shapiro_wilk import ShapiroWilk
from dagostinok2 import DagostinoK2
from anderson_darling import Anderson_Darling
from pearson_correlation import PearsonCorrelation
from spearmans_rank_correlation import SpearmanRankCorrelation
from kendalls_rank_correlation import KendallRankCorrelation
from chi_squared import ChiSquared
from dickey_fuller import DickeyFuller
from kwiatkowski_phillips_schmidt_shin import KwiatkowskiPhillipsSchmidtShin
from t_test import TTest
from paired_t_test import PairedTTest
from anova import ANOVA
from mann_whitney_u import MannWhitneyU
from wilcoxon_signed_rank import WilcoxonSignedRank
from kruskal_wallis_h import KruskalWallisH
from friedman import Friedman

mu = 0
sigma = 0.001
data1 = np.random.normal(mu, sigma, 500)
data2 = data1*3
data3 = np.random.normal(3, 2, 500)
data4 = np.random.normal(7, 34, 500)
table = np.array([[10, 20, 30], [5, 9, 17]])
data_single = [data1]
data_multiple = [data1, data3]
data_multiple2 = [data1, data3, data4]

my_test = ShapiroWilk()
my_test.evaluate_statistic(data_single)

my_test2 = DagostinoK2()
my_test2.evaluate_statistic(data_single)

my_test3 = Anderson_Darling()
my_test3.evaluate_statistic(data_single)

my_test4 = PearsonCorrelation()
my_test4.evaluate_statistic(data_multiple)

my_test5 = SpearmanRankCorrelation()
my_test5.evaluate_statistic(data_multiple)

my_test6 = ChiSquared()
my_test6.evaluate_statistic(table)

my_test7 = KendallRankCorrelation()
my_test7.evaluate_statistic(data_multiple)

my_test9 = KwiatkowskiPhillipsSchmidtShin()
my_test9.evaluate_statistic(data_single)

my_test8 = DickeyFuller()
my_test8.evaluate_statistic(data_single)

my_test10 = TTest()
my_test10.evaluate_statistic(data_multiple)

my_test11 = PairedTTest()
my_test11.evaluate_statistic(data_multiple)

my_test12 = ANOVA()
my_test12.evaluate_statistic(data_multiple)

my_test13 = MannWhitneyU()
my_test13.evaluate_statistic(data_multiple)

my_test14 = WilcoxonSignedRank()
my_test14.evaluate_statistic(data_multiple)

my_test15 = KruskalWallisH()
my_test15.evaluate_statistic(data_multiple)

my_test16 = Friedman()
my_test16.evaluate_statistic(data_multiple2)
