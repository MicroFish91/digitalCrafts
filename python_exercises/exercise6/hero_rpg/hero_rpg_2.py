#!/usr/bin/env python

# In this simple RPG game, the hero fights the goblin. He has the options to:

# 1. fight goblin
# 2. do nothing - in which case the goblin will attack him anyway
# 3. flee

import random
import time

# Array holds experience required for each level up
levelUp = [50, 200, 400, 800, 1200, 1800, 2400, 3000, 5000, 8000, 12000, 18000, 25000, 40000, 75000]

# Parent class for all character models
class Character:

    def __init__(self, health, power, charType, special, evasion, defense, critical, experience, coins):
        self.maxHealth = health
        self.health = health
        self.power = power
        self.charType = charType
        self.maxSpecial = special
        self.special = special
        self.evasion = evasion
        self.defense = defense
        self.critChance = critical
        self.critMult = 2
        self.level = 1
        self.experience = experience
        self.charging = False
        self.coins = coins
        self.itemPouch = {"consumables": {}, "equipment": {}}

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
            self.maxHealth += 2
            self.health = self.maxHealth
            self.power += 1
            self.maxSpecial += 2
            self.special = self.maxSpecial
            self.evasion += 1
            self.defense += 1
            self.critChance += 1
            self.experience -= levelUp[self.level - 1]
            self.level += 1

            print()
            print("Congratulations again!! You have reached level {}. You gain the following stat points: ".format(self.level))
            print("Max Health: {} + 2 = {}".format(self.maxHealth - 2, self.maxHealth))
            print("Power: {} + 1 = {}".format(self.power - 1, self.power))
            print("Special: {} + 2 = {}".format(self.maxSpecial - 2, self.maxSpecial))
            print("Evasion: {} + 1 = {}".format(self.evasion - 1, self.evasion))
            print("Defense: {} + 1 = {}".format(self.defense - 1, self.defense))
            print("Crit. Chance: {} + 1 = {}".format(self.critMult - 1, self.critMult))
            time.sleep(3)
            print()
            print("Your health has been restored to full.")

        print()
        print("You have {} XP remaining until you reach level {}!".format(levelUp[self.level - 1] - self.experience, self.level))

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

    # Triggers for protagonists upon death
    def death(self, myFoe):
        print("You have died! ")
        time.sleep(1)
        print()
        
        for consumables, quantity in self.itemPouch["consumables"].items():
            print("You lose {} {}. ".format(quantity, consumables))
            self.itemPouch["consumables"][consumables] = 0

        time.sleep(3)
        print()

        if self.level - myFoe.level >= 1:
            print("You lose {} levels.".format(myFoe.level))
            self.level -= myFoe.level
            
            # Stat Reduction
            self.maxHealth -= (2 * myFoe.level)
            self.power -= myFoe.level
            self.maxSpecial -= (2 * myFoe.level)
            self.evasion -= myFoe.level
            self.defense -= myFoe.level
            self.critChance -= myFoe.level
            self.experience = 0

        else:
            print("You lose {} levels.".format(self.level - 1))
            self.maxHealth -= (2 * (self.level - 1))
            self.power -= (self.level - 1)
            self.maxSpecial -= (2 * (self.level - 1))
            self.evasion -= (self.level - 1)
            self.defense -= (self.level - 1)
            self.critChance -= (self.level - 1)
            self.experience = 0
            self.level = 1

        time.sleep(1)

        print()
        print("The gods revive you to fight once more. ")
        print("You return back with {} health. ".format(int(self.maxHealth / 2) + 1))
        print()
        self.health = int(self.maxHealth / 2) + 1

        time.sleep(3)


# Only admin has access to this class (primarily for test purposes)
class godMode(Character):
    def __init__(self):
        super().__init__(1000, 10, "Tyrone Biggums", 100, 10, 2, 20, 0, 100000)
        self.level = 10

    def special_ability(self, foe):
        self.maxHealth = int(input("New max health? "))
        self.health = self.maxHealth
        self.power = int(input("New power stat? "))
        self.defense = int(input("New defense stat? "))
        self.evasion = int(input("New evasion stat? "))
        self.crtical = int(input("New critical strike chance? "))


# Hero is resilient and has the double damage special ability
class Hero(Character):

    def __init__(self):
        super().__init__(15, 5, "Hero", 10, 5, 2, 2, 0, 0)
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
        super().__init__(20, 5, "Goblin", 5, 1, 1, 5, 50, 10)
        self.level = 1

    def attack(self, foe):
        if self.charging:
            self._charging(foe)

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
            self._charging(foe)
        
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
        super().__init__(125, 1, "Zombie", 0, 0, 0, 0, 200, 25)
        self.level = 2

    def special_ability(self, foe):
        print("{}'s hunger for brains is increasing. {} gains +1 power. ".format(self.charType, self.charType))
        self.power += 1

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
        elif myHero == "god":
            print("ENTERING GOD MODE!")
            myHero = godMode()
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

# Stats modifiers stored in following order using arrays:
# [maxHealth, currentHealth, power, special, evasion, defense, critical, experience]
def itemShop(myHero):

    # Returns an array of the hero's current consumables
    def consumable_list(myHero):
        itemList = []

        for item in myHero.itemPouch["consumables"]:
            itemList.append(myHero.itemPouch["consumables"][item])

        return itemList

    def equipment_list(myHero):
        itemList = []

        for item in myHero.itemPouch["equipment"]:
            itemList.append(myHero.itemPouch["equipment"][item])
        
        return itemList

    def buy_health(myHero):
        
        healthConsumables = {
            "potion_of_health": {
                "cost": 3, 
                "statMod": [0, 10, 0, 0, 0, 0, 0, 0],
                "permanent": True,
                "tooltip": "potion_of_health: May be used in combat to instantly restore 10 health.  Worth 3 coins. ",
                "quantity": 1
                },

            "potion_of_greater_health": {
                "cost": 5,
                "statMod": [0, 20, 0, 0, 0, 0, 0, 0],
                "permanent": True,
                "tooltip": "potion_of_greater_health: May be used in combat to instantly restore 20 health. Worth 5 coins.",
                "quantity": 1
                },

            "elixir_of_health": {
                "cost": 10,
                "statMod": [0, 40, 0, 0, 0, 0, 0, 0], 
                "permanent": True,
                "tooltip": "elixir_of_health: May be used in combat to instantly restore 40 health. Worth 10 coins.",
                "quantity": 1
                },

            "elixir_of_max_health": {
                "cost": 20,
                "statMod": [0, 999, 0, 0, 0, 0, 0, 0], 
                "permanent": True,
                "tooltip": "elixir_of_max_health: May be used in combat to instantly restore all of your health. Worth 20 coins.",
                "quantity": 1
                },

            "fountain_of_youth": {
                "cost": 400,
                "statMod": [5, 999, 0, 0, 0, 0, 0, 0], 
                "permanent": True,
                "tooltip": "fountain_of_youth: Take a sip from the fountain to permanently gain 5 health points as well as restore your current health to max. Worth 400 coins.",
                "quantity": 1
                }
        }

        buying = True

        while buying:
            
            print("You have {} coins.".format(myHero.coins))
            print("Please enter the name of that which you would like to buy! ")
            print()

            for item in healthConsumables:
                print(healthConsumables[item]["tooltip"])
            
            print("Press 'B' to exit. ")

            time.sleep(2)
            
            userInput = input()

            if userInput == "B":
                buying = False
            else:
                if myHero.coins >= healthConsumables[userInput]["cost"]:
                    myHero.coins -= healthConsumables[userInput]["cost"]

                    itemCompare = consumable_list(myHero)

                    if healthConsumables[userInput] not in itemCompare:
                        myHero.itemPouch["consumables"][userInput] = healthConsumables[userInput]
                    else:
                        myHero.itemPouch["consumables"][userInput]["quantity"] += 1
                else:
                    print("Not enough coins to purchase this item, please try again later.")
                    print()

            time.sleep(1)      

    def buy_equipment(myHero):
        equipment = {
            "great_sword": {
                "cost": 250,
                "statMod": [0, 0, 5, 10, -2, 0, 5, 0],
                "durability:": 100,
                "hands": 2,
                "tooltip": "great_sword: 2-handed weapon imbued with +5 power, +10 special, and +5% to critical chance. Reduces your evasion by 2%. Durability 100. Worth 250 coins."
            },

            "short_sword": {
                "cost": 125,
                "statMod": [0, 0, 2, 5, 0, 0, 2, 0],
                "durability": 75,
                "hands": 1,
                "tooltip": "short_sword: 1-handed weapon imbued with +2 power, +5 special, and +2% to critical chance. Durability 75. Worth 125 coins. "
            },

            "metal_shield": {
                "cost": 125,
                "statMod": [5, 0, 0, 0, 0, 2, 0, 0],
                "hands": 1,
                "tooltip": "metal_shield: 1-handed shield imbued with +5 health and +2 defense. Worth 125 coins."
            }
        }

        buying = True

        while buying:
            
            print("You have {} coins.".format(myHero.coins))
            print("Please enter the name of that which you would like to buy! ")
            print()

            for item in equipment:
                print(equipment[item]["tooltip"])
            
            print("Press 'B' to exit. ")

            time.sleep(2)
            
            userInput = input()

            if userInput == "B":
                buying = False
            else:
                if myHero.coins >= equipment[userInput]["cost"]:

                    itemCompare = equipment_list(myHero)

                    if equipment[userInput] not in itemCompare:
                        myHero.coins -= equipment[userInput]["cost"]
                        myHero.itemPouch["equipment"][userInput] = equipment[userInput]
                    else:
                        print("You already own this item. Equipment items are unique and only one of each may be held at a time.")
                else:
                    print("Not enough coins to purchase this item, please try again later.")
                    print()

            time.sleep(1)

    def viewItems(myHero):
        
        print("You own the following items: ")
        print()
        time.sleep(1)

        # Print Consumables
        print("Consumables:")
        for item in myHero.itemPouch["consumables"]:
            print("{} You have {} of this item. ".format(myHero.itemPouch["consumables"][item]["tooltip"], myHero.itemPouch["consumables"][item]["quantity"]))

        print()
        time.sleep(1)

        # Print Equipment
        print("Equipment:")
        for item in myHero.itemPouch["equipment"]:
            print(myHero.itemPouch["equipment"][item]["tooltip"])


    powerConsumables = {
        "potion_of_strength": {
            "cost": 10, 
            "statMod": [0, 0, 5, 0, 0, 0, 0, 0],
            "permanent": False,
            "turns": 2,
            "tooltip": "Potion of Strength: May be used in combat to instantly gain 5 power for 2 turns. "
        },

        "potion_of_greater_strength": {
            "cost": 25,
            "statMod": [0, 0, 10, 0, 0, 0, 0, 0],
            "permanent": False,
            "turns": 5,
            "tooltip": "Potion of Greater Strength: May be used in combat to instantly gain 10 power for 5 turns. "
        },

        "testosterone_therapy": {
            "cost": 300,
            "statMod": [0, 0, 2, 0, 0, 0, 0, 0],
            "permanent": True,
            "tooltip": "Testosterone Therapy: Enroll for testosterone therapy and permanently gain 2 power. "
        }
    }

    defenseConsumables = {
        "potion_of_defense": {
            "cost": 10, 
            "statMod": [0, 0, 0, 0, 0, 2, 0, 0],
            "permanent": False,
            "turns": 2,
            "tooltip": "Potion of Defense: May be used in combat to instantly gain 3 defense for 2 turns. "
        },

        "potion_of_greater_defense": {
            "cost": 25,
            "statMod": [0, 0, 0, 0, 0, 4, 0, 0],
            "permanent": False,
            "turns": 5,
            "tooltip": "Potion of Greater Defense: May be used in combat to instantly gain 4 defense for 5 turns. "
        },
    }

    shopCheck = True

    while shopCheck:
        print("Welcome to the item shop! ")
        print("""
        What would you like to view? 
        1. Health Consumables
        2. Power Consumables
        3. Defense Consumables
        4. Equipment
        5. View Current Inventory
        6. Back to Start
        """)

        userInput = input()

        if userInput == "1":
            buy_health(myHero)
        elif userInput == "2":
            print("Functionality not yet added.")
        elif userInput == "3":
            print("Functionality not yet added.")
        elif userInput == "4":
            buy_equipment(myHero)
        elif userInput == "5":
            viewItems(myHero)
        elif userInput == "6":
            shopCheck = False
        else:
            print("Invalid entry, please try again.")

def coins(self, foe):
    self.coins += foe.coins
    print("You have gained {} coins for killing the {}. You now have {} coins. ".format(foe.coins, foe.charType, self.coins))

def main():

    # Initialize variables
    playAgain = True
    myHero = chooseProtagonist()

    while playAgain:
        
        # Start menu
        print("What would you like to do? ")
        print("1. View inventory & buy from item shop. ")
        print("2. Fight a monster. ")

        userInput = input()

        # Visit the item shop
        if userInput == "1":
            itemShop(myHero)

        # Initialize new foe
        myFoe = chooseFoe()

        # FIGHT!!!!!!
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

            time.sleep(1)
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
                    time.sleep(1)
                    myFoe.attack(myHero)
                
                # Foe performs a special attack
                elif foeMove == 2:
                    print("{} retaliates with a special attack!".format(myFoe.charType))
                    time.sleep(1)
                    myFoe.special_ability(myHero)
                
                # Foe uses an item
                elif foeMove == 3:
                    print("Foe uses an item.")
                    time.sleep(1)

                # Shouldn't ever trigger
                else:
                    print("That's strange, your foe chose to do nothing.")

            else:
            # If Foe is dead
                print("Congratulations! {}'s death has granted you {} XP!!".format(myFoe.charType, myFoe.experience))
                time.sleep(2)
                myHero.level_up(myFoe.experience)
                time.sleep(5)

                print()
                coins(myHero, myFoe)

            # If you are dead
            if myHero.health <= 0:
                myHero.death(myFoe)

        # Check is user would like to continue playing
        userInput = input("Would you like to play again ('Y' or 'N')? ")

        if userInput == "N":
            playAgain = False

main()

