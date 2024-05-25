from financial_statement_modules.income_statement import IncomeStatement

#my_income_statement = IncomeStatement()

print('hi world')

# Create a python script to optimise the blue eBike group work, 
# make a github repo and go through the videos and not down what effects the result, 
# then ccreate a script that prepares and compares all results. 
# If you miss some data ask it on monday or over the web.

#########
# KPI's #
#########

#maybe make this into a module?

def inflow_circularity(non_virgin_material, total_inflow):
    return non_virgin_material / total_inflow

def outflow_circularity(recoverable_outflow, total_outflow):
    return recoverable_outflow / total_outflow

# I am a bit uncertain on this one but it can probably be checked
def circularity(inflow_circularity, outflow_circularity):
    return (inflow_circularity + outflow_circularity)/2

def return_on_investments(profit_after_tax, total_assets):
    return profit_after_tax/total_assets

def return_on_materials(profit_after_tax, net_virgin_materials_used):
    return profit_after_tax / net_virgin_materials_used

# [kg]
def net_virgin_materials_used(virgin_material_purchased, recycled_materials_delivered):
    return virgin_material_purchased/recycled_materials_delivered

##############
# Financials #
##############

# not matching income statement?
starting_cash_position = 20800
starting_emergency_loans = 4896733

# old circularity was 0%
# this led to a bank contract index of 1.2136
# the base interest rate with no circularity is 6.07%

# if new circularity is 100%
# bank contract index is 0.9136
# the interest then becomes 4.57%

'''

Margin (Real Estate loan)
4.00%
Margin (Machines loan)
5.00%
Margin (Overdraft)
6.00%

'''

index_at_zero = 1.2136
index_at_hundered = 0.9136

# these fucntion assume a linear relationship between circularity and interest rates

def calculate_base_interest():
    interest_at_zero = .0607
    interest_at_hundered = .0457
    base_index = 1
    removed_interest_per_deciindex = (interest_at_zero - interest_at_hundered) / (index_at_zero - index_at_hundered)
    deciindex_from_zero_to_base = index_at_zero - base_index

    return interest_at_zero - (deciindex_from_zero_to_base * removed_interest_per_deciindex)

def bank_interest_rate_based_on_circularity(promised_circularity, base_interest):
    added_index_per_percent_circularity = (index_at_zero - index_at_hundered)/100

    return base_interest * (index_at_zero + promised_circularity * added_index_per_percent_circularity)

print(calculate_base_interest())