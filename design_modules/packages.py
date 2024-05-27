from component import BasicComponent

class Packages:
    def __init__(self):
        
        self.alternatives = [
            BasicComponent(
                name='Luxury box green',
                remanufacturability=.0,
                remanufacturing_cost=0,
                recyclability=1,
                durability=0+1,
                weight_in_kg=.05,
                repair_time_discount=0,
                price_per_piece=15
            ),
            BasicComponent(
                name='Luxury box basic',
                remanufacturability=.0,
                remanufacturing_cost=0,
                recyclability=.0,
                durability=0+1, # check if acurate
                weight_in_kg=.05,
                repair_time_discount=0,
                price_per_piece=10
            ),
        ]