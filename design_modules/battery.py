from component import BasicComponent

class Batteries:
    def __init__(self):
        self.cost_per_shipment = 100
        self.transport_cost_per_palet = 80
        self.transport_cost_per_full_truck = 2000
        self.period_order_to_buyer_wharehouse = 14

        self.alternatives = [
            BasicComponent(
                name='Powerpack performance',
                remanufacturability=.5,
                remanufacturing_cost=50,
                recyclability=.35,
                durability=0.2,
                weight_in_kg=3.5,
                repair_time_discount=0,
                price_per_piece=200,
                steel=1,
                rubber=0,
                plastic=1,
                cardboard=0,
                aluminium=0,
                battery_acid=1.5
            ),
            BasicComponent(
                name='Battery robust',
                remanufacturability=.4,
                remanufacturing_cost=50,
                recyclability=.4,
                durability=0.3,
                weight_in_kg=3.6,
                repair_time_discount=0,
                price_per_piece=200,
                steel=1.1,
                rubber=0,
                plastic=1,
                cardboard=0,
                aluminium=0,
                battery_acid=1.5
            ),
            BasicComponent(
                name='Battery light',
                remanufacturability=.5,
                remanufacturing_cost=45,
                recyclability=.65,
                durability=0,
                weight_in_kg=3,
                repair_time_discount=0,
                price_per_piece=220,
                steel=.5,
                rubber=0,
                plastic=1,
                cardboard=0,
                aluminium=0,
                battery_acid=1.5
            ),
            BasicComponent(
                name='Battery classic',
                remanufacturability=.25,
                remanufacturing_cost=120,
                recyclability=.3,
                durability=0,
                weight_in_kg=3.5,
                repair_time_discount=0,
                price_per_piece=185,
                steel=1,
                rubber=0,
                plastic=1,
                cardboard=0,
                aluminium=0,
                battery_acid=1.5
            ),
            BasicComponent(
                name='Battery blue',
                remanufacturability=.65,
                remanufacturing_cost=35,
                recyclability=.45,
                durability=0,
                weight_in_kg=3.5,
                repair_time_discount=0,
                price_per_piece=210,
                steel=1,
                rubber=0,
                plastic=1,
                cardboard=0,
                aluminium=0,
                battery_acid=1.5
            ),
            BasicComponent(
                name='Battery smart',
                remanufacturability=.3,
                remanufacturing_cost=35,
                recyclability=.75,
                durability=-.1,
                weight_in_kg=3.5,
                repair_time_discount=0,
                price_per_piece=170,
                steel=1,
                rubber=0,
                plastic=1,
                cardboard=0,
                aluminium=0,
                battery_acid=1.5
            ),
        ]