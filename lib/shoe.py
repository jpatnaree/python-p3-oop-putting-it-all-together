#!/usr/bin/env python3

class Shoe:
    def __init__(self, brand, size):
        self.brand = brand
        self.size = size 

    @property
    def size(self):
        return self.size
    
    @size.setter
    def size(self, size):
        if isinstance(size, int):
            self.size = size
        else: 
            print('size must be an integer')

    @property
    def brand(self):
        return self.brand
    
    @brand.setter
    def brand(self, brand):
        self.brand = brand

    def cobble(self):
        self.condition = "New"
        print("Your shoe is as good as new!")