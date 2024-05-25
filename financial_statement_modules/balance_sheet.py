class BalanceSheet:
    def __init__(
        self,
        plant_assets:float,
        production_assets:float,
        assembly_assets:float,
        intangible_assets_and_goodwill:float,
        cash_and_cash_equivalents:float,
        component_inventory:float,
        product_inventory:float,
        retained_products:float, # value of products delivered but still owned
        recievables:float,
        allowance_for_doubtful_accounts:float, # refcievables which might not be payed
        prepayments:float,
        long_term_loans:float,
        other_non_current_payables:float,
        deferred_income:float,
        short_term_loans:float,
        emergency_loans:float,
        payables:float,
        receipt_in_advance:float,
        other_current_liabilities:float,
        share_capital:float,
        share_premium:float,
        reserves:float,
        retained_earnings:float
    ):
        # assets
        self.total_assets__OLD = 86647399

        # non-current assets
        self.non_current_assets__OLD = 55800000

        self.property_plant_and_equipment = (
            plant_assets + 
            production_assets + 
            assembly_assets
        )
        self.property_plant_and_equipment__OLD = 55800000

        self.intangible_assets_and_goodwill = intangible_assets_and_goodwill
        self.intangible_assets_and_goodwill__OLD = 0

        # current assets
        self.current_assets__OLD = 30847399

        self.cash_and_cash_equivalents = cash_and_cash_equivalents
        self.cash_and_cash_equivalents__OLD = 455709

        self.inventories = (
            component_inventory +
            product_inventory +
            retained_products
        )
        self.inventories__OLD = 14708868

        self.recievables = recievables
        self.recievables__OLD = 15,682,822

        self.allowance_for_doubtful_accounts = allowance_for_doubtful_accounts
        self.allowance_for_doubtful_accounts__OLD = 0

        self.prepayments = prepayments
        self.prepayments__OLD = 0

        # total equity and liabilities
        self.total_equity_and_liabilities__OLD = 86,647,399

        # liabilities
        self.total_liabilities__OLD = 74422953

        # non_current_liabiliteis
        self.non_current_liabilities = (
            long_term_loans +
            other_non_current_payables +
            deferred_income
        )
        self.non_current_liabilities__OLD = 55800000

        # current_liabilites
        self.current_liabilities = (
            short_term_loans +
            emergency_loans +
            payables +
            receipt_in_advance +
            other_current_liabilities
        )
        self.current_liabilities__OLD = 18622953

        # equity
        self.total_equity__OLD = 12224446
        self.total_equity = (
            share_capital +
            share_premium +
            reserves +
            retained_earnings
        )


    def non_current_assets(self):
        return self.property_plant_and_equipment + self.intangible_assets_and_goodwill

    def current_assets(self):
        return (
            self.cash_and_cash_equivalents +
            self.inventories +
            self.recievables +
            self.allowance_for_doubtful_accounts +
            self.prepayments
        )
    
    def total_assets(self):
        return self.current_assets() + self.non_current_assets()
    
    def total_liabilities(self):
        return self.current_liabilities + self.non_current_liabilities
    
    def total_equity_and_liabilities(self):
        return self.total_liabilities() + self.total_equity
    
    def balance(self):
        return self.total_assets() - self.total_equity_and_liabilities()