class MultiplePrint:

    def __init__(self):
        self.critical_value = 0
        self.significance_level = 0
        self.statistic = 0
        self.result_text = ""
        self.decision = ""
        self.h0 = ""
        self.name = ""
        self.number_of_vectors = 1
        self.p_value = 0

    def print_result_header(self):
        print("")
        print("Hypothesis Testing")
        print("Test:", self.name)
        self.print_null_hypothesis()
        self.print_statistic()

    def print_result(self, decision):
        self.decision = decision
        self.print_critical_value()
        self.print_significance_level()
        self.print_test_result()
        print("")

    def set_number_of_vectors(self, number_of_vectors):
        self.number_of_vectors = number_of_vectors

    def set_null_hypothesis(self, h0):
        self.h0 = h0

    def set_statistic(self, statistic):
        self.statistic = statistic

    def set_result_text(self, result_text):
        self.result_text = result_text

    def set_critical_value(self, critical_value):
        self.critical_value = critical_value

    def set_significance_level(self, significance_level):
        self.significance_level = significance_level

    def set_test_name(self, name):
        self.name = name

    def set_p_value(self, p):
        self.p_value = p

    def evaluate_hypothesis_critical(self, statistic, critical_value):
        if statistic < critical_value:
            self.decision = "Accept"
        else:
            self.decision = "Reject"

    def print_statistic(self):
        print("Statistic:", self.statistic)

    def print_p_value(self):
        print("p-value:", self.p_value)

    def print_critical_value(self):
        print("    critical value:", self.critical_value)

    def print_significance_level(self):
        print("    significance level:", self.significance_level)

    def print_null_hypothesis(self):
        print("H0: ", self.h0)

    def print_test_result(self):
        if self.decision == "Accept":
            print("    Probably", self.result_text)
        else:
            print("    Probably not", self.result_text)
