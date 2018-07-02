#!/usr/bin/env python

# In this simple RPG game, the hero fights the goblin. He has the options to:

# 1. fight goblin
# 2. do nothing - in which case the goblin will attack him anyway
# 3. flee

import random

class Character:

    def __init__(self, health, power, charType, special):
        self.health = health
        self.power = power
        self.charType = charType
        self.special = special

    def attack(self, foe):
        foe.health -= self.power
        print("{} does {} damage to the {}.".format(self.charType, self.power, foe.charType))
        if foe.health <= 0:
            print("The {} is dead.".format(foe.charType))

    def alive(self):
        if self.health > 0:
            return True
        else:
            return False

    def print_status(self):
        print("{} has {} health, {} power, and {} special.".format(self.charType, self.health, self.power, self.special))

    
class Hero(Character):

    def __init__(self):
        super().__init__(15, 4, "Hero", "5")

    def special_ability(self, foe):


        

class Goblin(Character):
    
    def __init__(self):
        super().__init__(10, 2, "Goblin")


class Zombie(Character):
    def __init__(self):
        super().__init__(30, 1, "Zombie")


def chooseProtagonist():
    inputCheck = True

    while inputCheck:
        myHero = input("""
                Enter the number of your protagonist:
                1. Hero
                2. Medic
                3. Wizard
                4. Samurai
                5. Eager Beaver 
                """)

        if myHero == "1":
            myHero = Hero()
            inputCheck = False
        elif myHero == "2":
            myHero = Medic()
            inputCheck = False
        elif myHero == "3":
            myHero = Wizard()
            inputCheck = False
        elif myHero == "4":
            myHero = Samurai()
            inputCheck = False
        elif myHero == "5":
            myHero = eagerBeaver()
            inputCheck = False
        else:
            print("Invalid choice, please try again. ")

    return myHero

def chooseFoe():
    inputCheck = True

    while inputCheck:
        myFoe = input("""
                Who would you like to fight? 
                1. Goblin
                2. Zombie
                3. Shadow
                4. Sewer Montrosity
                5. Angry Sports Fan 
                """)

        if myFoe == "1":
            myFoe = Goblin()
            inputCheck = False
        elif myFoe == "2":
            myFoe = Zombie()
            inputCheck = False
        elif myFoe == "3":
            myFoe = Shadow()
            inputCheck = False
        elif myFoe == "4":
            myFoe = sewerMonstrosity()
            inputCheck = False
        elif myFoe == "5":
            myFoe = angrySportsFan()
            inputCheck = False
        else:
            print("Invalid choice, please try again. ")

    return myFoe


def main():

    # Initialize variables
    myHero = chooseProtagonist()
    myFoe = chooseFoe()

    while myHero.alive() and myFoe.alive():
        myHero.print_status()
        myFoe.print_status()       
        print()

        print("What do you want to do? ")
        print("1. Basic Attack ")
        print("2. Special Ability (Cost: 5) ")
        print("3. Evasive Maneuver ")
        print("> ", end=' ')

        # raw_input = input()
        # if raw_input == "1":
        #     # Hero attacks goblin
        #     myHero.attack(myGoblin)
        # elif raw_input == "2":
        #     pass
        # elif raw_input == "3":
        #     print("Goodbye.")
        #     break
        # else:
        #     print("Invalid input {}".format(raw_input))

        # if myGoblin.health > 0:
        #     # Goblin attacks hero
        #     myGoblin.attack(myHero)

main()

