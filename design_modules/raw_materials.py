class Raw_Material:
    def __init__(
            self,
            basic_price:float,
            recyclabe_cost_factor:float,
            recycling_price:float,
            recycling_loss:float
        ):
        
        self.basic_price = basic_price
        self.recyclabe_cost_factor = recyclabe_cost_factor
        self.recycling_price = recycling_price
        self.recycling_loss = recycling_loss

class Raw_Materials:
    
    def __init__(self):
        self.steel = Raw_Material(
            basic_price=3,
            recyclabe_cost_factor=12,
            recycling_price=2.4,
            recycling_loss=.02
        )
        self.rubber = Raw_Material(
            basic_price=.4,
            recyclabe_cost_factor=1.5,
            recycling_price=.32,
            recycling_loss=.3
        )
        self.plastic = Raw_Material(
            basic_price=1.5,
            recyclabe_cost_factor=3,
            recycling_price=1.2,
            recycling_loss=.5
        )
        self.cardboard = Raw_Material(
            basic_price=4,
            recyclabe_cost_factor=20,
            recycling_price=3.2,
            recycling_loss=.1
        )
        self.aluminium = Raw_Material(
            basic_price=2,
            recyclabe_cost_factor=50,
            recycling_price=1.6,
            recycling_loss=.01
        )
        self.leather = Raw_Material(
            basic_price=6,
            recyclabe_cost_factor=5,
            recycling_price=4.8,
            recycling_loss=.18
        )
        self.battery_acid = Raw_Material(
            basic_price=0,
            recyclabe_cost_factor=50,
            recycling_price=0,
            recycling_loss=1
        )