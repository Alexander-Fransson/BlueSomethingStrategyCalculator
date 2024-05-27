from component import BasicComponent

class Mechanisms:
    def __init__(self):
        
        self.alternatives = [
            BasicComponent(
                name='Bike gear plus',
                remanufacturability=.5,
                remanufacturing_cost=100,
                recyclability=.45,
                durability=1+0.2,
                weight_in_kg=0.7,
                repair_time_discount=.2,
                price_per_piece=385
            ),
            BasicComponent(
                name=' Gear and more',
                remanufacturability=.4,
                remanufacturing_cost=110,
                recyclability=.5,
                durability=1+0.5,
                weight_in_kg=.7,
                repair_time_discount=.25,
                price_per_piece=400
            ),
            BasicComponent(
                name='Speedy',
                remanufacturability=.82,
                remanufacturing_cost=55,
                recyclability=.55,
                durability=1+0,
                weight_in_kg=.7,
                repair_time_discount=0,
                price_per_piece=415
            ),
            BasicComponent(
                name='Mechanism standard',
                remanufacturability=.5,
                remanufacturing_cost=100,
                recyclability=.4,
                durability=1+0,
                weight_in_kg=.7,
                repair_time_discount=0,
                price_per_piece=320
            ),
            BasicComponent(
                name='Mechanism basic',
                remanufacturability=.3,
                remanufacturing_cost=50,
                recyclability=.9,
                durability=1+0.1,
                weight_in_kg=1,
                repair_time_discount=-.05,
                price_per_piece=270
            ),
            BasicComponent(
                name='Mechanism light',
                remanufacturability=.5,
                remanufacturing_cost=80,
                recyclability=.65,
                durability=1-0.2,
                weight_in_kg=.6,
                repair_time_discount=0,
                price_per_piece=390
            ),
            BasicComponent(
                name='Mechtech',
                remanufacturability=.8,
                remanufacturing_cost=55,
                recyclability=.55,
                durability=1+0,
                weight_in_kg=.7,
                repair_time_discount=.05,
                price_per_piece=420
            )
        ]