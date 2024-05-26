# Maybe separate the product specific stuff into its own inheritable class
# I bet I miss sime dynamism, lets check out how the rate of return is effected by warenty changes

class Customer:
    def __init__(
        self,
        location:str,
        rate_of_return:list,
        last_warrenty_period:int,
        warrenty:int, # aka buy back price
        virgin_product_value:float=2000,
        raw_material_value:float=30.6,
        average_product_lifespan:float=5.3,
        max_refurbishment_age:float=4.7
    ):
        self.location = location
        self.average_product_lifespan = average_product_lifespan
        self.max_refurbishment_age = max_refurbishment_age
        self.buyback_price = warrenty
        self.last_warrenty_period = last_warrenty_period
        # figure out how much extra the customer pays for warrenty

        #Depreciation, repurchase and warenty
        self.virgin_product_value = virgin_product_value
        self.raw_material_value= raw_material_value
        self.rate_of_return = rate_of_return
        self.depreciation_rate = map(divideBy2000,[
            2000, 1462.8, 1015.2, 567.6, 344, 114.6, 0,0,0,0,0
        ])
        self.second_hand_value_percent = map(divideBy2000[
            1624, 1310.6, 997.3, 840.8, 680.2, 519.6, 359.1, 198.5, 37.9, 0
        ])

    def second_hand_value_by_period(self, period):
        return self.virgin_product_value * self.second_hand_value_percent[period]
    
    def depreciated_value_by_period(self, period):
        return self.virgin_product_value * self.depreciation_rate[period]
    
    def fraction_returned_by_period(self,period):
        percentage_returned = 0

        for i in range(period+1):
            percentage_returned += self.rate_of_return[i]

        return percentage_returned

def divideBy2000(x):
    return x/2000

# High, quality and long lasting
# bad credit rating maybe expect 20% less
class Cheetah(Customer):
    def __init__(self):
        super().__init__(
            location='France',
            rate_of_return=[0,.01,.029,.069,.222,.114,.166,.096,.056,.023,.003]
        )

# Convinience
class Gearshift(Customer):
    def __init__(self):
        super().__init__(
            location='UK',
            rate_of_return=[0,.01,.029,.069,.222,.055,.122,.071,.041,.017,.002]
        )

# Sustainability niche
class HBS(Customer):
    def __init__(self):
        super().__init__(
            location='Netherlands',
            rate_of_return=[0,.01,.029,.069,.222,.192,.168,.097,.056,.023,.003]
        )

#Do the depreciation graph and maybe have one customer class and just 
# make instances of the three customers here, maybe they can inherit stuff?