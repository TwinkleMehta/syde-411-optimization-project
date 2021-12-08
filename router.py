import random as r

class Router:
    def __init__(self):
        self.cost = self.calculate_cost()
        self.time = self.calculate_time()
        self.quality = self.calculate_quality()

    def calculate_cost(self): # Unit [cents] 
        return round(r.uniform(1.04, 10.04), 2) 

    def calculate_time(self): # Unit [s] 
        queue_delay = r.uniform(0.01,0.03)
        process_delay = r.uniform(7.42e-5,1.9588e-3)
        return round(queue_delay + process_delay, 4)

    def calculate_quality(self): # Unit [standard. 1-10]
        return r.randint(1,10)
     
    def get_cost(self):
        return self.cost
