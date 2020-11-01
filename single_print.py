
class SinglePrint:

    def __init__(self):
        self.p_value = 0
        self.statistic = 0
        self.result_text = ""
        self.decision = ""
        self.h0 = ""
        self.name = ""
        self.number_of_vectors = 1

    def print_result(self, decision):
        print("")
        print("Hypothesis Testing")
        print("Test:", self.name)
        self.decision = decision
        self.print_null_hypothesis()
        self.print_statistic()
        self.print_p_value()
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

    def set_p_value(self, p_value):
        self.p_value = p_value

    def set_test_name(self, name):
        self.name = name

    def evaluate_hypothesis(self, p):
        if p > 0.05:
            self.decision = "Accept"
        else:
            self.decision = "Reject"

    def print_statistic(self):
        print("Statistic:", self.statistic)

    def print_p_value(self):
        print("p-value:", self.p_value)

    def print_null_hypothesis(self):
        print("H0: ", self.h0)

    def print_test_result(self):
        if self.decision == "Accept":
            print("Probably", self.result_text)
        else:
            print("Probably not", self.result_text)
