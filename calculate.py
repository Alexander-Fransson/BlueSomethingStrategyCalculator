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


