# Lab 6 - Wilson Pham

import random

class Armor:
    def __init__(self, name, max_block):
        self.name = name
        self.max_block = max_block

    def block(self):
        '''Return a random value between 0 and max_block'''
        return random.randint(0, self.max_block)
    
if __name__ == "__main__":
    Shield = Armor("Shield", 20)
    print(Shield.block())
