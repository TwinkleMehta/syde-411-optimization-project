import random as r

class Router:
    def __init__(self):
        self.cost = self.calculate_cost()
        self.time = self.calculate_time()
        self.quality = self.calculate_quality()

    def calculate_cost(self): # Unit [cents] 
        # OR we can just generate range between calculated cents 
        # return round(r.uniform(0.04, 10.04), 2) # between 1.04 - 10.04 watts
        # choose wattage between 2 - 20 r
        wattage = r.randint(1,20) # between 2 - 20 watts
        # calculate costs
        return round(wattage*21.64*(24/float(1000)), 2)
        
    def calculate_time(self): # Unit [ms] 
        queue_delay = r.randint(0,10) # TEMP VALUES
        process_delay = r.randint(0,10) # TEMP VALUES
        return queue_delay + process_delay

    def calculate_quality(self): # Unit [standard. 1-10]
        return r.randint(0,10)
     
    def get_cost(self):
        return self.cost