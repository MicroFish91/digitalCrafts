#!/usr/bin/env python

# In this simple RPG game, the hero fights the goblin. He has the options to:

# 1. fight goblin
# 2. do nothing - in which case the goblin will attack him anyway
# 3. flee

import random

# Array holds experience required for each level up
levelUp = [100, 200, 400, 800, 1200, 1800, 2400, 3000, 5000, 8000, 12000, 18000, 25000]

class Character:

    def __init__(self, health, power, charType, special, evasion, defense, critical):
        self.health = health
        self.power = power
        self.charType = charType
        self.special = special
        self.evasion = evasion
        self.defense = defense
        self.critChance = critical
        self.critMult = 2
        self.level = 1
        self.experience = 0

    # Basic Attack
    def attack(self, foe):
        foe.health -= self.power
        print("{} does {} damage to the {}.".format(self.charType, self.power, foe.charType))
        if foe.health <= 0:
            print("The {} is dead.".format(foe.charType))

    # Returns a float indicating final damage multiplier after critical chance and damage are taken into account
    def criticalDamage(self):
        if random.randint(0, 100) <= self.critChance:
            print("WOW! CRITICAL HIT!! {}X damage multiplier activated!!!".format(self.critMult))
            return self.critMult
        else:
            return 1

    # Returns a boolean to see if attack lands
    def attackLand(self):
        if random.randint(0, 100) <= self.evasion:
            return False
        else:
            return True

    # Returns a boolean to see if character is still alive
    def alive(self):
        if self.health > 0:
            return True
        else:
            return False

    # Prints key attributes of the character
    def print_status(self):
        print("{} is level {}. {} has {} health, {} power, {} special, {} evasion, and {} defense.".format(self.charType, self.level, self.charType self.health, self.power, self.special, self.evasion, self.defense))

    # When level up requirement is met, stat increase is triggered
    def levelUp(self):
        self.health += 2
        self.power += 1
        self.special += 2
        self.evasion += 1
        self.defense += 1
        self.critChance += 1
        self.level += 1

# Hero is resilient and has the double damage special ability
# At level 5 and above, automatically survives through one fatal blow
class Hero(Character):

    def __init__(self):
        super().__init__(15, 5, "Hero", 10, 5, 2, 2)
        self.fatalBlow = 1

    def special_ability(self, foe):
        if self.special_ability >= 5:
            foe.health -= (self.power * 2)
            self.special_ability -= 5
            print("{} does {} damage to the {}.".format(self.charType, self.power * 2, foe.charType))
            print("{} has {} SP remaining.".format(self.charType, self.special_ability))
        else:
            print("{} winds up to perform a devastating blow.. wait, {} totally whiffed.".format(self.charType, self.charType))
        if foe.health <= 0:
            print("The {} is dead.".format(foe.charType))
        

class Goblin(Character):

    def __init__(self):
        super().__init__(20, 3, "Goblin", 5, 1, 1, 5)
        self.experience = 50

    def special_ability(self, foe):
        print("Nothing happened.")
        


class Zombie(Character):
    def __init__(self):
        super().__init__(100, 1, "Zombie", 0, 0, 0, 0)
        self.experience = 200

    def special_ability(self, foe):
        print("Nothing happened.")


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
        print("4. Use Item")
        print("5. Flee")
        print("> ", end=' ')

        userInput = input()

        # ************************
        # ***   Player Move    ***
        # ************************

        # Basic Attack
        if userInput == "1":
            myHero.attack(myFoe)

        # Special Attack
        elif userInput == "2":
            myHero.special_ability(myFoe)
        
        # Evasive Maneuver
        elif userInput == "3":
            
        # Use Item
        elif userInput == "4":

        # Flee
        elif userInput == "5":

        
        # Invalid output
        else:
            print("Invalid input.")
            print("Your character's indecision cost you your turn.")



        # ************************
        # ***    Enemy Move    ***
        # ************************

        foeMove = random.randint(1, 2)

        # Foe performs a basic attack
        if foeMove == 1:
            myFoe.attack(myHero)
        
        # Foe performs a special attack
        elif foeMove == 2:
            myFoe.special_ability(myHero)

        # Foe performs an evasive maneuver
        elif foeMove == 3:
            
        
        # Shouldn't ever trigger
        else:
            print("That's strange, your foe chose to do nothing.")

main()

