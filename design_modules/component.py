class BasicComponent:
    def __init__(
        self,
        name:str,
        remanufacturability:float,
        remanufacturing_cost:float,
        recyclability:float,
        durability:float, # acceptable warenty?
        weight_in_kg:float,
        repair_time_discount:float,
        price_per_piece:float 
    ):
        self.name = name
        self.remanufacturability = remanufacturability
        self.remanufacturing_cost = remanufacturing_cost
        self.recyclability = recyclability
        self.durability = durability
        self.weight = weight_in_kg
        self.repair_time_discount = repair_time_discount
        self.price = price_per_piece

class ChooseByCriteria:
    def __init__(
        self,
        alternatives:list[BasicComponent],
    ):
        self.alternatives = alternatives

    def calculate_average_of_alternatives(self):
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
        instances = self.alternatives

        # you need to account for durability being negative 

        for i in instances:
            for key, value in i.__dict__.items():
                if isinstance(value, (int, float)):
                    if averages[key] == 0:
                        setattr(i, key, 0)
                    else:
                        setattr(i, key, value/averages[key])

        # un negafy durability
                        
        return instances


    def normalize_prioritize_and_sort_alternatives(
        self,
        remanufacturability_priority:int,
        remanufacturing_cost_priority:int,
        recyclability_priority:int,
        durability_priority:int,
        weight_in_kg_priority:int,
        repair_time_discount_priority:int,
        price_per_piece_priority:int     
    ):  
        pass
        #normalize all the values to be relative to the average of that type
        
        # multiply the normalized values with their priority

        # reduce the value of the instance to one 

        # sort the array based on that value

        # deliver the top alternative
        

    #create normalize prioritize and a function that sorts 
    #them based on criteria and priority