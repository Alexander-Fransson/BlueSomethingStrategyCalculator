from component import BasicComponent

# mAKE A PARRENT WITH A SORT alternatices FUNCTION
# use normalize prioritize

class Frames:
    def __init__(self):
        
        self.alternatives = [
            BasicComponent(
                name='Frame_forever',
                remanufacturability=.4,
                remanufacturing_cost=110,
                recyclability=.45,
                durability=0.5,
                weight_in_kg=4,
                repair_time_discount=0,
                price_per_piece=310
            ),
            BasicComponent(
                name='Frame_28',
                remanufacturability=.5,
                remanufacturing_cost=130,
                recyclability=.5,
                durability=0.3,
                weight_in_kg=3.6,
                repair_time_discount=0,
                price_per_piece=300
            ),
            BasicComponent(
                name='Frame_robust',
                remanufacturability=.3,
                remanufacturing_cost=50,
                recyclability=.95,
                durability=0.1,
                weight_in_kg=5,
                repair_time_discount=0,
                price_per_piece=210
            ),
            BasicComponent(
                name='Frame_light',
                remanufacturability=.5,
                remanufacturing_cost=90,
                recyclability=.75,
                durability=-.1,
                weight_in_kg=3.2,
                repair_time_discount=0,
                price_per_piece=300
            ),
            BasicComponent(
                name='Frame_standard',
                remanufacturability=.4,
                remanufacturing_cost=70,
                recyclability=.4,
                durability=0,
                weight_in_kg=4,
                repair_time_discount=0,
                price_per_piece=250
            ),
            BasicComponent(
                name='Frame_de_luxe',
                remanufacturability=.9,
                remanufacturing_cost=55,
                recyclability=.6,
                durability=0,
                weight_in_kg=4,
                repair_time_discount=0,
                price_per_piece=325
            ),
            BasicComponent(
                name='Framed',
                remanufacturability=.85,
                remanufacturing_cost=55,
                recyclability=.6,
                durability=0,
                weight_in_kg=4,
                repair_time_discount=0,
                price_per_piece=310
            )
        ]