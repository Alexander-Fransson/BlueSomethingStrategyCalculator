from component import BasicComponent

class Packages:
    def __init__(self):
        self.cost_per_shipment = 130
        self.transport_cost_per_palet = 20
        self.transport_cost_per_full_truck = 500
        self.period_order_to_buyer_wharehouse = 5

        self.alternatives = [
            BasicComponent(
                name='Luxury box green',
                remanufacturability=.0,
                remanufacturing_cost=0,
                recyclability=1,
                durability=0,
                weight_in_kg=.05,
                repair_time_discount=0,
                price_per_piece=15,
                steel=0,
                rubber=0,
                plastic=0.01,
                cardboard=0.04,
                aluminium=0,
                battery_acid=0
            ),
            BasicComponent(
                name='Luxury box basic',
                remanufacturability=.0,
                remanufacturing_cost=0,
                recyclability=.0,
                durability=0, # check if acurate
                weight_in_kg=.05,
                repair_time_discount=0,
                price_per_piece=10,
                steel=0,
                rubber=0,
                plastic=0.01,
                cardboard=0.04,
                aluminium=0,
                battery_acid=0
            ),
        ]