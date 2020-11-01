from multiple_print import MultiplePrint
from single_print import SinglePrint


class PrintStatisticBehavior:

    def __init__(self, print_behavior):
        if print_behavior == "multiple":
            self.print_statistic = MultiplePrint()
        else:
            self.print_statistic = SinglePrint()
