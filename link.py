import random as r

class Link:
    def __init__(self, link_length):
        self.cost = self.calculate_cost()
        self.time = self.calculate_time(link_length)
        self.quality = self.calculate_quality()

    def calculate_cost(self): # Unit [cents] 
        return round(r.uniform(1.34, 1.42), 2)

    def calculate_time(self, d): # Unit [s] 
        R = r.randint(50,300) # link_transmission_rate [mbps]
        C = r.uniform(2e8, 3e10) # propagation_speed [m/s]
        propagation_delay = d / float(C) # where d is in [m]
        transmission_delay = 150 / float(R) # where 150Mb = filesize
        return propagation_delay + transmission_delay

    def calculate_quality(self): # Unit [standard. 1-10]
        return r.randint(1,10)