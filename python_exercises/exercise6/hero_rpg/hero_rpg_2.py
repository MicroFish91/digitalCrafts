#!/usr/bin/env python

# In this simple RPG game, the hero fights the goblin. He has the options to:

# 1. fight goblin
# 2. do nothing - in which case the goblin will attack him anyway
# 3. flee

import random
import time

# Array holds experience required for each level up
levelUp = [100, 200, 400, 800, 1200, 1800, 2400, 3000, 5000, 8000, 12000, 18000, 25000, 40000, 75000]

# Parent class for all character models
class Character:

    def __init__(self, health, power, charType, special, evasion, defense, critical, experience):
        self.health = health
        self.power = power
        self.charType = charType
        self.special = special
        self.evasion = evasion
        self.defense = defense
        self.critChance = critical
        self.critMult = 2
        self.level = 1
        self.experience = experience
        self.charging = False

    # Basic Attack
    def attack(self, foe):
        if self.attackLand:
            foe.health -= (self.power - foe.defense)
            print("{} does {} damage to the {}.".format(self.charType, self.power - foe.defense, foe.charType))
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
        print("{} is level {}. {} has {} health, {} power, {} special, {} evasion, and {} defense.".format(self.charType, self.level, self.charType, self.health, self.power, self.special, self.evasion, self.defense))

    # When level up requirement is met, stat increase is triggered
    def level_up(self, experience):
        self.experience += experience

        # Level up triggered!
        while self.experience >= levelUp[self.level - 1]:
            self.health += 2
            self.power += 1
            self.special += 2
            self.evasion += 1
            self.defense += 1
            self.critChance += 1
            self.experience -= levelUp[self.level - 1]
            self.level += 1

            print()
            print("Congratulations again!! You have reached level {}. You gain the following stat points: ".format(self.level))
            print("Health: {} + 2 = {}".format(self.health - 2, self.health))
            print("Power: {} + 1 = {}".format(self.power - 1, self.power))
            print("Special: {} + 2 = {}".format(self.special - 2, self.special))
            print("Evasion: {} + 1 = {}".format(self.evasion - 1, self.evasion))
            print("Defense: {} + 1 = {}".format(self.defense - 1, self.defense))
            print("Crit. Chance: {} + 1 = {}".format(self.critMult - 1, self.critMult))

        print()
        print("You have {} XP remaining until you reach level {}!".format(levelUp[self.level] - self.experience, self.level + 1))

    # Increases chance to dodge by 35%. Upon successful dodge, has a chance to trigger a counter
    def evasive_maneuver(self, foe):
        # Checks if the evasion condition is triggered
        if random.randint(0, 100) >= (self.evasion + 35):
            print("{} successfully evades {}.".format(self.charType, foe.charType))

            # Counter triggered
            if random.randint(0, 100) >= 50:
                print("{} finds an opening and counters {} for {} damage!".format(self.charType, foe.charType, self.power - foe.defense))

            else:
                print("{} could not find an opening to perform a counter attack.".format(self.charType))
        
        else:
        # Evade failed
            self.health -= (foe.power - self.defense)
            print("{} attemps to evade. It fails.".format(self.charType))
            print("{} is hit by {} for {} damage.".format(self.charType, foe.charType, foe.power - self.defense))

# Hero is resilient and has the double damage special ability
class Hero(Character):

    def __init__(self):
        super().__init__(15, 5, "Hero", 10, 5, 2, 2, 0)
        self.fatalBlow = 1

    def special_ability(self, foe):
        # Executes if player has enough special ability points
        if self.special >= 5:
            # Executes if attack is not evaded
            if self.attackLand:
                foe.health -= ((self.power * 2) - foe.defense)
                self.special -= 5
                print("HYAAHHH!! SPECIAL ATTACK! {} does {} damage to the {}.".format(self.charType, self.power * 2, foe.charType))
                print("{} has {} SP remaining.".format(self.charType, self.special))

            else:
            # If attack is evaded
                self.special -= 5
                print("{} misses {}.".format(self.charType, foe.charType))
                print("{} has {} SP remaining.".format(self.charType, self.special))

        else:
        # If not enough special ability points
            print("{} winds up to perform a devastating blow.. wait... {} totally whiffed!".format(self.charType, self.charType))

        if foe.health <= 0:
            print("The {} is dead.".format(foe.charType))
        
class Goblin(Character):

    def __init__(self):
        super().__init__(20, 3, "Goblin", 5, 1, 1, 5, 50)

    def attack(self, foe):
        if self.charging:
            _charging(foe)

        elif self.attackLand:
            foe.health -= (self.power - foe.defense)
            print("{} does {} damage to the {}.".format(self.charType, self.power - foe.defense, foe.charType))

        if foe.health <= 0:
            print("The {} is dead.".format(foe.charType))

    def special_ability(self, foe):
        if self.special >= 5 and not self.charging:   
            # Performs special ability (charge) 
            print("{} begins flailing about rapidly. It appears he is charging up for an attack.".format(self.charType))
            self.special -= 5
            self.charging = True

        elif self.special < 5 and not self.charging:
            # If not enough special ability points
            print("{} winds up to perform a devastating blow.. wait... {} totally whiffed!".format(self.charType, self.charType))

        elif self.charging:
            _charging(foe)
            

    def _charging(self, foe):
        if self.attackLand:
            # Unleash the charged attack
            foe.health -= (self.power * 3 - foe.defense)
            print("{} unleashes his charged attack all over the {} for {} damage.".format(self.charType, foe.charType, self.power * 3 - foe.defense))
            self.charging = False
        else:
            # Charged attack misses
            print("{} misses his charge attack and runs into a wall. {} takes 2 damage.".format(self.charType, self.charType))
            self.health -= 2
            self.charging = False
 
class Zombie(Character):

    def __init__(self):
        super().__init__(100, 1, "Zombie", 0, 0, 0, 0, 200)

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

def battlePrompt():
    print("What do you want to do? ")
    print("1. Basic Attack ")
    print("2. Special Ability (Cost: 5) ")
    print("3. Evasive Maneuver ")
    print("4. Use Item")
    print("5. Flee")
    print("> ", end=' ')

# Need to add max health function


def main():

    # Initialize variables
    playAgain = true
    myHero = chooseProtagonist()
    myFoe = chooseFoe()

    while playAgain:
        # Initialize new foe
        myFoe = chooseFoe()

        while myHero.alive() and myFoe.alive():
            print()
            myHero.print_status()
            myFoe.print_status()       
            print()
            time.sleep(3)

            # Displays battle prompt options
            battlePrompt()

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
                print("You perform an evasive maneuver.")

            # Use Item
            elif userInput == "4":
                print("You use an item.")

            # Flee
            elif userInput == "5":
                print("You attempt to flee.")
            
            # Invalid output
            else:
                print("Invalid input.")
                print("Your character's indecision cost you your turn.")

            time.sleep(3)
            print()

            # ************************
            # ***    Enemy Move    ***
            # ************************

            foeMove = random.randint(1, 2)

            # If Foe is still alive
            if myFoe.health > 0:

                # Foe performs a basic attack
                if foeMove == 1:
                    print("{} retaliates with a basic attack!".format(myFoe.charType))
                    time.sleep(3)
                    myFoe.attack(myHero)
                
                # Foe performs a special attack
                elif foeMove == 2:
                    print("{} retaliates with a special attack!".format(myFoe.charType))
                    time.sleep(3)
                    myFoe.special_ability(myHero)
                
                # Foe uses an item
                elif foeMove == 3:
                    print("Foe uses an item.")
                    time.sleep(3)

                # Shouldn't ever trigger
                else:
                    print("That's strange, your foe chose to do nothing.")

            else:
            # If Foe is dead
                print("Congratulations! {}'s death has granted you {} XP!!".format(myFoe.charType, myFoe.experience))
                time.sleep(2)
                myHero.level_up(myFoe.experience)
                time.sleep(5)

        userInput

main()

