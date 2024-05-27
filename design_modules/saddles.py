from component import BasicComponent

class Saddles:
    def __init__(self):
        
        self.alternatives = [
            BasicComponent(
                name='Saddle pro health',
                remanufacturability=.5,
                remanufacturing_cost=35,
                recyclability=.45,
                durability=0.1+1,
                weight_in_kg=1,
                repair_time_discount=0,
                price_per_piece=75
            ),
            BasicComponent(
                name='Saddle freedom',
                remanufacturability=.4,
                remanufacturing_cost=40,
                recyclability=.5,
                durability=0.1+1,
                weight_in_kg=1,
                repair_time_discount=0,
                price_per_piece=85
            ),
            BasicComponent(
                name='Saddle royal',
                remanufacturability=.75,
                remanufacturing_cost=30,
                recyclability=.55,
                durability=0+1,
                weight_in_kg=1,
                repair_time_discount=0,
                price_per_piece=95
            ),
            BasicComponent(
                name='Saddle comfort',
                remanufacturability=.3,
                remanufacturing_cost=35,
                recyclability=.9,
                durability=0+1,
                weight_in_kg=1.1,
                repair_time_discount=0,
                price_per_piece=45
            ),
            BasicComponent(
                name='Saddle tech',
                remanufacturability=.5,
                remanufacturing_cost=30,
                recyclability=.65,
                durability=0+1,
                weight_in_kg=.8,
                repair_time_discount=0,
                price_per_piece=100
            ),
            BasicComponent(
                name='Saddle standard',
                remanufacturability=.5,
                remanufacturing_cost=40,
                recyclability=.4,
                durability=0+1,
                weight_in_kg=1,
                repair_time_discount=0,
                price_per_piece=50
            ),
        ]