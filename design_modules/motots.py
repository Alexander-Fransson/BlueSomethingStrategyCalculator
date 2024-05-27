from component import BasicComponent

class Motors:
    def __init__(self):
        
        self.alternatives = [
            BasicComponent(
                name='Power bike',
                remanufacturability=.3,
                remanufacturing_cost=35,
                recyclability=.9,
                durability=1+0,
                weight_in_kg=2,
                repair_time_discount=0,
                price_per_piece=125
            ),
            BasicComponent(
                name='Motor feather',
                remanufacturability=.5,
                remanufacturing_cost=45,
                recyclability=.65,
                durability=1+0,
                weight_in_kg=1.8,
                repair_time_discount=0,
                price_per_piece=195
            ),
            BasicComponent(
                name='Motor standard',
                remanufacturability=.5,
                remanufacturing_cost=60,
                recyclability=.4,
                durability=1+0,
                weight_in_kg=2,
                repair_time_discount=0,
                price_per_piece=150
            ),
            BasicComponent(
                name='Motor easy',
                remanufacturability=.5,
                remanufacturing_cost=50,
                recyclability=.45,
                durability=1+0.2,
                weight_in_kg=1.9,
                repair_time_discount=.2,
                price_per_piece=190
            ),
            BasicComponent(
                name='Motor endure',
                remanufacturability=.4,
                remanufacturing_cost=50,
                recyclability=.5,
                durability=1+0.2,
                weight_in_kg=2,
                repair_time_discount=.15,
                price_per_piece=190
            ),
            BasicComponent(
                name='Green motor',
                remanufacturability=.75,
                remanufacturing_cost=35,
                recyclability=.55,
                durability=1+0,
                weight_in_kg=2,
                repair_time_discount=0,
                price_per_piece=180
            ),
            BasicComponent(
                name='Blue motor',
                remanufacturability=.85,
                remanufacturing_cost=35,
                recyclability=.5,
                durability=1+0,
                weight_in_kg=2,
                repair_time_discount=.05,
                price_per_piece=220
            )
        ]