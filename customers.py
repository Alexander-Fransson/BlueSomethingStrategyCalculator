class Customer:
    def __init__(
        self,
        country:str,
        credit_rating:str,
        number_of_stores:float,
        cost_per_shipment:float,
        distribution_cost_per_pallet:float,
        distribution_cost_per_full_truck:float,
        average_yearly_usage_km:float,
        month_between_unlimited_subscription_contracts:float,
        average_unlimited_subscription_duration:float,
    ):
        self.country = country
        self.credit_rating = credit_rating
        self.number_of_stores = number_of_stores
        self.cost_per_shipment = cost_per_shipment
        self.istribution_cost_per_pallet = distribution_cost_per_pallet
        self.distribution_cost_per_full_truck = distribution_cost_per_full_truck
        self.average_yearly_usage_km = average_yearly_usage_km
        self.month_between_unlimited_subscription_contracts = month_between_unlimited_subscription_contracts
        self.average_unlimited_subscription_duration = average_unlimited_subscription_duration

class Customers:
    def __init__(self):
        self.Cheetah = Customer(
            country= 'france',
            credit_rating='CC',
            number_of_stores=100,
            cost_per_shipment= 70,
            distribution_cost_per_pallet=20,
            distribution_cost_per_full_truck=500,
            average_yearly_usage_km=1000,
            month_between_unlimited_subscription_contracts=2,
            average_unlimited_subscription_duration=6
        )
        self.Gearshift = Customer(
            country= 'UK',
            credit_rating='AA',
            number_of_stores=15,
            cost_per_shipment= 70,
            distribution_cost_per_pallet=20,
            distribution_cost_per_full_truck=500,
            average_yearly_usage_km=1000,
            month_between_unlimited_subscription_contracts=1,
            average_unlimited_subscription_duration=9
        )
        self.HBS = self.Cheetah = Customer(
            country= 'netherlands',
            credit_rating='BB',
            number_of_stores=10,
            cost_per_shipment= 70,
            distribution_cost_per_pallet=15,
            distribution_cost_per_full_truck=350,
            average_yearly_usage_km=1000,
            month_between_unlimited_subscription_contracts=2,
            average_unlimited_subscription_duration=12
        )