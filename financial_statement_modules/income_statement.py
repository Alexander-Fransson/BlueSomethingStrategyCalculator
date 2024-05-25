class IncomeStatement:

    def __init__(
            self, 
            gross_sales:float, 
            sales_bonus_or_penalty:float,
            material_purchases:float,
            permanent_labor_cost:float,
            manufactoring_overhead_cost:float,
            maintanence_cost:float,
            energy_cost:float,
            water_cost:float,
            equipment_depreciation:float,
            real_estate_depreciation:float,
            risk_cost:float, # bad debt loss
            outbound_storage_cost:float, # cost of maintaining warehouses
            inbound_storage_cost:float,  # cost of maintaining material warehouses
            order_lines_outbound_cost:float, # administaration variable costs related to number of order lines (book keeping)
            orders_outbound_cost:float, # variable administatetion cost regarding the order itself
            contract_manangement_outbound_cost:float,
            other_sales_personnel_cost:float,
            distribution_costs:float,
            order_lines_inbound_costs:float,
            orders_inbound_costs:float,
            contract_management_inbound_costs:float,
            other_personnel_costs:float,
            rnd_project_costs:float,
            real_estate_loan_interest_expense:float,
            machine_loan_interest_expense:float,
            overdraft_interest_expense:float, # short term loan to fund working capital
            emergency_loan_interest_expense:float, # loan from shareholder to provide liquidity in crisis
            credit_risk_and_insurance_expenses:float,
            direct_debit:float,
            electronic_bank_transfer:float,
            credit_limit_cost:float,
            coorporate_tax:float
        ):
        
        # Revenue

        self.sales_revenue = gross_sales + sales_bonus_or_penalty

        # COGS

        self.cost_of_goods_manufactured = (
            material_purchases +
            permanent_labor_cost +
            manufactoring_overhead_cost +
            maintanence_cost +
            energy_cost +
            water_cost +
            equipment_depreciation +
            real_estate_depreciation +
            risk_cost + 
            outbound_storage_cost + 
            inbound_storage_cost
        )

        # Selling and Distribution expenses

        self.sales_expenses = (
            order_lines_outbound_cost +
            orders_outbound_cost +
            contract_manangement_outbound_cost +
            other_sales_personnel_cost
        )

        self.distribution_costs = distribution_costs

        self.general_and_administrative_expenses = (
            order_lines_inbound_costs +
            orders_inbound_costs +
            contract_management_inbound_costs +
            other_personnel_costs
        )
        
        # R&D expenses

        self.rnd_expenses = rnd_project_costs

        # Financial costs

        self.interest_expenses = (
            real_estate_loan_interest_expense +
            machine_loan_interest_expense +
            overdraft_interest_expense +
            emergency_loan_interest_expense
        )

        self.credit_risk_cost = credit_risk_and_insurance_expenses

        self.transaction_costs = direct_debit + electronic_bank_transfer

        self.financing_project_costs = credit_limit_cost

        # Tax Expenses

        self.tax_expenses = coorporate_tax

    def cogs(self):  # maybe add cost of recycled inventory later?
        return self.cost_of_goods_manufactured()
    
    def gross_profit(self):
        return self.sales_revenue() - self.cogs()
    
    def result_operating_activities(self):
        return (
            self.gross_profit() - 
            self.sales_expenses - 
            self.distribution_costs - 
            self.general_and_administrative_expenses - 
            self.rnd_expenses
        )
    
    def profit_before_tax(self): # no financial revenues?
        return (
            self.result_operating_activities() -
            self.interest_expenses -
            self.credit_risk_cost -
            self.transaction_costs -
            self.financing_project_costs
        )
    
    def profit_after_tax(self):
        return self.profit_before_tax - self.tax_expenses


        
