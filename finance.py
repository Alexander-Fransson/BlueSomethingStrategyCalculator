class BankInterestNegotiations:
    def __init__(
        self,
        promised_circularity
    ):
        self.circularity = promised_circularity

        #ICA Bancas interests dependant on circularity
        self.index_at_zero = 1.2136
        self.index_at_hundered = 0.9136
        self.interest_at_zero = .0607
        self.interest_at_hundered = .0457

        #Past interest rates on loans I belive
        self.real_estate_loan_margin = .04
        self.machine_loan_margin = .05
        self.overdraft_loan_margin = .06 #emergency loan?

        #vendor lease I dont have access to information about yet

    # assumes linear relationship based on circularity
    def bank_interest_rate_based_on_circularity(self, margin):

        decreased_index_per_percent_circularity = (
            self.index_at_zero - self.index_at_hundered
        )/100
        
        decreased_interest_per_percent_circularity = (
            self.interest_at_zero - self.interest_at_hundered
        )/100

        current_index = self.index_at_zero - decreased_index_per_percent_circularity
        current_base_interest = self.interest_at_zero - decreased_interest_per_percent_circularity

        return current_index * (current_base_interest + margin)

# not matching income statement?
starting_cash_position = 20800
starting_emergency_loans = 4896733
