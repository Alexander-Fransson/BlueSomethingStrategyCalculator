from design_modules.component import BasicComponent, ChooseByCriteria

# mAKE A PARRENT WITH A SORT alternatices FUNCTION
# use normalize prioritize

class Frames(ChooseByCriteria):
    def __init__(self):
        self.cost_per_shipment = 120
        self.transport_cost_per_palet = 40
        self.transport_cost_per_full_truck = 900
        self.period_order_to_buyer_wharehouse = 8

        self.alternatives = [
            BasicComponent(
                name='Frame_forever',
                remanufacturability=.4,
                remanufacturing_cost=110,
                recyclability=.45,
                durability=0.5,
                weight_in_kg=4,
                repair_time_discount=0,
                price_per_piece=310,
                steel=0,
                rubber=0,
                plastic=0,
                cardboard=0,
                aluminium=4,
                battery_acid=0
            ),
            BasicComponent(
                name='Frame_28',
                remanufacturability=.5,
                remanufacturing_cost=130,
                recyclability=.5,
                durability=0.3,
                weight_in_kg=3.6,
                repair_time_discount=0,
                price_per_piece=300,
                steel=0,
                rubber=0,
                plastic=0,
                cardboard=0,
                aluminium=3.6,
                battery_acid=0
            ),
            BasicComponent(
                name='Frame_robust',
                remanufacturability=.3,
                remanufacturing_cost=50,
                recyclability=.95,
                durability=0.1,
                weight_in_kg=5,
                repair_time_discount=0,
                price_per_piece=210,
                steel=5,
                rubber=0,
                plastic=0,
                cardboard=0,
                aluminium=0,
                battery_acid=0
            ),
            BasicComponent(
                name='Frame_light',
                remanufacturability=.5,
                remanufacturing_cost=90,
                recyclability=.75,
                durability=-.1,
                weight_in_kg=3.2,
                repair_time_discount=0,
                price_per_piece=300,
                steel=0,
                rubber=0,
                plastic=0,
                cardboard=0,
                aluminium=3.2,
                battery_acid=0
                
            ),
            BasicComponent(
                name='Frame_standard',
                remanufacturability=.4,
                remanufacturing_cost=70,
                recyclability=.4,
                durability=0,
                weight_in_kg=4,
                repair_time_discount=0,
                price_per_piece=250,
                steel=0,
                rubber=0,
                plastic=0,
                cardboard=0,
                aluminium=4,
                battery_acid=0
            ),
            BasicComponent(
                name='Frame_de_luxe',
                remanufacturability=.9,
                remanufacturing_cost=55,
                recyclability=.6,
                durability=0,
                weight_in_kg=4,
                repair_time_discount=0,
                price_per_piece=325,
                steel=0,
                rubber=0,
                plastic=0,
                cardboard=0,
                aluminium=4,
                battery_acid=0
            ),
            BasicComponent(
                name='Framed',
                remanufacturability=.85,
                remanufacturing_cost=55,
                recyclability=.6,
                durability=0,
                weight_in_kg=4,
                repair_time_discount=0,
                price_per_piece=310,
                steel=0,
                rubber=0,
                plastic=0,
                cardboard=0,
                aluminium=4,
                battery_acid=0
            )
        ]

        super().__init__(
            self.alternatives
        )