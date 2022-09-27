import random

class Insect: 
    def __init__(self,w,l):
        self.wings = w
        self.legs = l
        self.flight = 0

    def calc_flight(self):
        self.flight = random.randint(1,10)
    
    def get_flight(self): #accessor method, returns one attribute
        self.flight

    



    
