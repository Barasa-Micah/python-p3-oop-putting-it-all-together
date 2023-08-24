#!/usr/bin/env python3

class Shoe:
    def __init__(self, brand, size):
        self.brand=brand
        self.size= size
        self.condition= 'used'  #default condition


    def int_size(self):
        if  not isinstance(self.size, int):
            print('size must be an integer')



    def can_cobble(self):
        self.condition = 'New'
        print('Your shoe is as good as new! \n')            




    condition = ('Nike', 10)
    condition.cobble = 'New'    