#!/usr/bin/env python

# In this simple RPG game, the hero fights the goblin. He has the options to:

# 1. fight goblin
# 2. do nothing - in which case the goblin will attack him anyway
# 3. flee

class Hero:
    def __init__(self):
        self.health = 10
        self.power = 5
    
    def attack(self, enemy):
        enemy.health -= self.power
        print("You do {} damage to the goblin.".format(self.power))
        if enemy.health <= 0:
            print("The goblin is dead.")

class Goblin:
    def __init__(self):
        self.health = 6
        self.power = 2


def main():
    myHero = Hero()
    myGoblin = Goblin()

    while myGoblin.health > 0 and myHero.health > 0:
        print("You have {} health and {} power.".format(myHero.health, myHero.power))
        print("The goblin has {} health and {} power.".format(myGoblin.health, myGoblin.power))
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
            myHero.health -= myGoblin.power
            print("The goblin does {} damage to you.".format(myGoblin.power))
            if myHero.health <= 0:
                print("You are dead.")

main()