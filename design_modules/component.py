class BasicComponent:
    def __init__(
        self,
        name:str,
        remanufacturability:float,
        remanufacturing_cost:int,
        recyclability:float,
        durability:float, # acceptable warenty?
        weight_in_kg:float,
        repair_time_discount:float,
        price_per_piece:float 
    ):
        self.name = name
        self.remanufacturability = remanufacturability
        self.remanufacturing_cost = remanufacturing_cost
        self.remanufacturability = recyclability
        self.durability = durability
        self.weight = weight_in_kg
        self.repair_time_discount = repair_time_discount
        self.price = price_per_piece