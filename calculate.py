from financial_statement_modules.income_statement import IncomeStatement
from design_modules.frames import Frames

#my_income_statement = IncomeStatement()

#############
# Todo list
'''
* Look at supply chain report and create modules for each component
* Look at sales roals and sales reports and make modules for everything


*Look att all decision videos and the hiering calculationformula
*See what inputs you have and try to calculate all costs and benefits
*draw the cashflow
'''

###############
# Findings


#*You can see demand on the past sales report thing
# you cannot have warenty and lease at the same time
# have the teammates note down everything they can do and how it effects the price


print('hi world')

frames = Frames()
# print(frames.calculate_average_of_alternatives())

# normlized_frames = frames.normalize_alternatives()

# for i in normlized_frames:
#     print(i.__dict__.items())

prioritized = frames.sort_normalized_alternatives(
    remanufacturability_priority=0,
    remanufacturing_cost_priority=1,
    recyclability_priority=0,
    durability_priority=0,
    weight_in_kg_priority=0,
    repair_time_discount_priority=0,
    price_per_piece_priority=0
)

print(prioritized)

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


######################
# Supply chain stuff #
######################

max_refurbishment_age:int # products older then this will not be refurbished
# you will have to chack out what the worth of the products are at what age
# refurbished items are sold at second hand value

shifts:int
# each shift has 16 full time employees
# 7 man hours to refurbish a bicicle
# can be discounted by repair time discounted componeients
# 70% of returned items will be refurbished, the rest are fildeted and dont take labor
# if labor is lacking the diference will be made up by 60€/h workers

full_time_employee:dict
# works 40 hours a week and costs 40000€ a year
# every maintanence service takes 60h
# you can decide how many to hire

