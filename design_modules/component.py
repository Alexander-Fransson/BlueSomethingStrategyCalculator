import copy

class BasicComponent:
    def __init__(
        self,
        name:str,                               # remove
        remanufacturability:float,              # +
        remanufacturing_cost:float,             # -
        recyclability:float,                    # +
        durability:float, # acceptable warenty?   +
        weight_in_kg:float,                     # -
        repair_time_discount:float,             # +
        price_per_piece:float,                   # -
        
        steel:float,
        rubber:float,
        plastic:float,
        cardboard:float,
        aluminium:float,
        battery_acid:float,
    ):
        self.name = name
        self.remanufacturability = remanufacturability
        self.remanufacturing_cost = remanufacturing_cost
        self.recyclability = recyclability
        self.durability = durability
        self.weight = weight_in_kg
        self.repair_time_discount = repair_time_discount
        self.price = price_per_piece

        # materials
        self.steel=steel
        self.plastic=plastic
        self.cardboard=cardboard
        self.rubber=rubber,
        self.aluminium=aluminium,
        self.battery_acid=battery_acid

class ChooseByCriteria:
    def __init__(
        self,
        alternatives:list[BasicComponent],
    ):
        self.alternatives = alternatives

    def calculate_average_of_alternatives(self):
        print(self.alternatives[0].__dict__)
        print('')

        instances = self.alternatives
        sums = {}
        length = len(instances)

        for i in instances:
            for key, value in i.__dict__.items():
                if isinstance(value, (int,float)):
                    if(key not in sums):
                        sums[key] = 0.0
                    sums[key] += getattr(i, key)
                else:
                    # probably decreases preformance but i dont car right now
                    sums[key] = value

        averages = {}

        for key, value in sums.items():
            if isinstance(value, (int,float)):
                averages[key] = value/length
            else:
                sums[key] = value

        return averages
    
    def normalize_alternatives(self):
        # Creating dict of keys with empty maluable values
        averages = self.calculate_average_of_alternatives()
        instances = copy.deepcopy(self.alternatives)
        where_low_is_good = ['remanufacturing_cost', 'weight_in_kg', 'price_per_piece']

        for i in instances:
            for key, value in i.__dict__.items():
                if key in where_low_is_good:
                    # If value is larger then one the diference is removed from one
                    value = 1 - (value - 1)
                if isinstance(value, (int, float)):
                    if averages[key] == 0:
                        setattr(i, key, 0)
                    else:
                        setattr(i, key, value/averages[key])

        print(self.alternatives[0].__dict__)
        print('')
                        
        return instances


    def sort_normalized_alternatives(
        self,
        remanufacturability_priority:int,
        remanufacturing_cost_priority:int,
        recyclability_priority:int,
        durability_priority:int,
        weight_in_kg_priority:int,
        repair_time_discount_priority:int,
        price_per_piece_priority:int     
    ):  
        normalized_instances = self.normalize_alternatives()
        prioritized_alternetives = []

        for i in normalized_instances:
            prioritized_instance = {
                'name':i.name,
                'value':(
                    remanufacturability_priority * i.remanufacturability +
                    remanufacturing_cost_priority * i.remanufacturing_cost +
                    recyclability_priority * i.recyclability +
                    durability_priority * i.durability +
                    weight_in_kg_priority * i.weight +
                    repair_time_discount_priority * i.repair_time_discount +
                    price_per_piece_priority * i.price
                )
            }
            prioritized_alternetives.append(prioritized_instance)

        sorted_prioritized_alternatives = sorted(prioritized_alternetives, key=lambda x:x['value'])

        return {
            'best':[i for i in self.alternatives if i.name == sorted_prioritized_alternatives[-1]['name']][0].__dict__,
            'worst':[i for i in self.alternatives if i.name == sorted_prioritized_alternatives[0]['name']][0].__dict__
        }