from component import BasicComponent

class Saddles:
    def __init__(self):
        self.cost_per_shipment = 100
        self.transport_cost_per_palet = 20
        self.transport_cost_per_full_truck = 500
        self.period_order_to_buyer_wharehouse = 3

        self.alternatives = [
            BasicComponent(
                name='Saddle pro health',
                remanufacturability=.5,
                remanufacturing_cost=35,
                recyclability=.45,
                durability=0.1,
                weight_in_kg=1,
                repair_time_discount=0,
                price_per_piece=75,
                steel=0,
                rubber=0.5,
                plastic=0,
                cardboard=0,
                aluminium=0.5,
                battery_acid=0
            ),
            BasicComponent(
                name='Saddle freedom',
                remanufacturability=.4,
                remanufacturing_cost=40,
                recyclability=.5,
                durability=0.1,
                weight_in_kg=1,
                repair_time_discount=0,
                price_per_piece=85,
                steel=0,
                rubber=0.5,
                plastic=0,
                cardboard=0,
                aluminium=0.5,
                battery_acid=0
            ),
            BasicComponent(
                name='Saddle royal',
                remanufacturability=.75,
                remanufacturing_cost=30,
                recyclability=.55,
                durability=0,
                weight_in_kg=1,
                repair_time_discount=0,
                price_per_piece=95,
                steel=0,
                rubber=0.5,
                plastic=0,
                cardboard=0,
                aluminium=0.5,
                battery_acid=0
            ),
            BasicComponent(
                name='Saddle comfort',
                remanufacturability=.3,
                remanufacturing_cost=35,
                recyclability=.9,
                durability=0,
                weight_in_kg=1.1,
                repair_time_discount=0,
                price_per_piece=45,
                steel=0,
                rubber=0.5,
                plastic=0,
                cardboard=0,
                aluminium=0.6,
                battery_acid=0
            ),
            BasicComponent(
                name='Saddle tech',
                remanufacturability=.5,
                remanufacturing_cost=30,
                recyclability=.65,
                durability=0,
                weight_in_kg=.8,
                repair_time_discount=0,
                price_per_piece=100,
                steel=0,
                rubber=0.5,
                plastic=0,
                cardboard=0,
                aluminium=0.3,
                battery_acid=0
            ),
            BasicComponent(
                name='Saddle standard',
                remanufacturability=.5,
                remanufacturing_cost=40,
                recyclability=.4,
                durability=0,
                weight_in_kg=1,
                repair_time_discount=0,
                price_per_piece=50,
                steel=0,
                rubber=0.5,
                plastic=0,
                cardboard=0,
                aluminium=0.5,
                battery_acid=0
            ),
        ]