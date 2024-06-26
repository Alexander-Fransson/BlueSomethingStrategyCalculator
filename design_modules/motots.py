from component import BasicComponent

class Motors:
    def __init__(self):
        self.cost_per_shipment = 90
        self.transport_cost_per_palet = 65
        self.transport_cost_per_full_truck = 1700
        self.period_order_to_buyer_wharehouse = 12

        self.alternatives = [
            BasicComponent(
                name='Power bike',
                remanufacturability=.3,
                remanufacturing_cost=35,
                recyclability=.9,
                durability=0,
                weight_in_kg=2,
                repair_time_discount=0,
                price_per_piece=125,
                steel=2,
                rubber=0,
                plastic=0,
                cardboard=0,
                aluminium=0,
                battery_acid=0
            ),
            BasicComponent(
                name='Motor feather',
                remanufacturability=.5,
                remanufacturing_cost=45,
                recyclability=.65,
                durability=0,
                weight_in_kg=1.8,
                repair_time_discount=0,
                price_per_piece=195,
                steel=1.8,
                rubber=0,
                plastic=0,
                cardboard=0,
                aluminium=0,
                battery_acid=0
            ),
            BasicComponent(
                name='Motor standard',
                remanufacturability=.5,
                remanufacturing_cost=60,
                recyclability=.4,
                durability=0,
                weight_in_kg=2,
                repair_time_discount=0,
                price_per_piece=150,
                steel=2,
                rubber=0,
                plastic=0,
                cardboard=0,
                aluminium=0,
                battery_acid=0
            ),
            BasicComponent(
                name='Motor easy',
                remanufacturability=.5,
                remanufacturing_cost=50,
                recyclability=.45,
                durability=0.2,
                weight_in_kg=1.9,
                repair_time_discount=.2,
                price_per_piece=190,
                steel=1.9,
                rubber=0,
                plastic=0,
                cardboard=0,
                aluminium=0,
                battery_acid=0
            ),
            BasicComponent(
                name='Motor endure',
                remanufacturability=.4,
                remanufacturing_cost=50,
                recyclability=.5,
                durability=0.2,
                weight_in_kg=2,
                repair_time_discount=.15,
                price_per_piece=190,
                steel=2,
                rubber=0,
                plastic=0,
                cardboard=0,
                aluminium=0,
                battery_acid=0
            ),
            BasicComponent(
                name='Green motor',
                remanufacturability=.75,
                remanufacturing_cost=35,
                recyclability=.55,
                durability=0,
                weight_in_kg=2,
                repair_time_discount=0,
                price_per_piece=180,
                steel=2,
                rubber=0,
                plastic=0,
                cardboard=0,
                aluminium=0,
                battery_acid=0
            ),
            BasicComponent(
                name='Blue motor',
                remanufacturability=.85,
                remanufacturing_cost=35,
                recyclability=.5,
                durability=0,
                weight_in_kg=2,
                repair_time_discount=.05,
                price_per_piece=220,
                steel=2,
                rubber=0,
                plastic=0,
                cardboard=0,
                aluminium=0,
                battery_acid=0
            )
        ]