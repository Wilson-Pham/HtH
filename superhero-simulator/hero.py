# Lab 6 - Wilson Pham

import random
from ability import Ability
from armor import Armor

class Hero:
    def __init__(self, name, starting_health=100):
        '''Initialize Hero with a name and health values'''
        self.name = name
        self.starting_health = starting_health
        self.current_health = starting_health
        self.armors = []
        self.abilities = []
    
    def battle(self, opponent):
        '''Fight another hero and randomly choose a winner'''
        winner = random.choice([self.name, opponent.name])
        print(f"The winner of this battle is {winner}!")

    def add_ability(self, ability):
        '''Add an ability to the hero's abilities list'''
        self.abilities.append(ability)
        print(f"{ability.name} has been added to the list of abilities")

    def sum_of_attacks(self):
        '''Iterates through entire list of abilities and returns the sum of their attack values'''
        total_damage = 0
        for ability in self.abilities:
            total_damage += ability.attack()
        return total_damage
    
    def add_armor(self, armor):
        '''Add an armor to the hero's armors list'''
        self.armors.append(armor)
        print(f"{armor.name} has been added to the list of armors")

    def defend(self):
        '''Iterates through entire list of armors and returns the sum of their block values'''
        total_block = 0
        for armor in self.armors:
            total_block += armor.block()
        return total_block



if __name__ == "__main__":
    my_hero1 = Hero("Grace Hopper", 200)
    my_hero2 = Hero("Spider-Man", 150)
    print(my_hero1.name)            # Grace Hopper
    print(my_hero1.current_health)  # 200
    my_hero1.battle(my_hero1)
    ability1 = Ability("Explosion", 300)
    ability2 = Ability("Electrocution", 150)
    ability3 = Ability("Web Shooter", 50)
    ability4 = Ability("Punch", 15)
    my_hero1.add_ability(ability1)
    my_hero1.add_ability(ability4)
    my_hero2.add_ability(ability3)
    my_hero2.add_ability(ability2)
    print(my_hero1.abilities)
    print(my_hero2.abilities)

    

