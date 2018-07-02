#!/usr/bin/env python

# In this simple RPG game, the hero fights the goblin. He has the options to:

# 1. fight goblin
# 2. do nothing - in which case the goblin will attack him anyway
# 3. flee

class Character:

    def __init__(self, health, power, charType):
        self.health = health
        self.power = power
        self.charType = charType

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
        print("{} has {} health and {} power.".format(self.charType, self.health, self.power))

    
class Hero(Character):

    def __init__(self, health, power):
        super().__init__(health, power, "Hero")


class Goblin(Character):
    
    def __init__(self, health, power):
        super().__init__(health, power, "Goblin")


class Zombie(Character):
    def __init__(self, health, power):
        super().__init__(health, power, "Zombie")



def main():
    myHero = Hero(10, 5)
    myGoblin = Goblin(6, 2)
    myZombie = Zombie(10000, 1)

    while myGoblin.alive() and myHero.alive():
        myHero.print_status()
        myGoblin.print_status()       
        print()
        print("What do you want to do?")
        print("1. fight goblin")
        print("2. do nothing")
        print("3. flee")
        print("> ", end=' ')
        raw_input = input()
        if raw_input == "1":
            # Hero attacks goblin
            myHero.attack(myGoblin)
        elif raw_input == "2":
            pass
        elif raw_input == "3":
            print("Goodbye.")
            break
        else:
            print("Invalid input {}".format(raw_input))

        if myGoblin.health > 0:
            # Goblin attacks hero
            myGoblin.attack(myHero)

main()