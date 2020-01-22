# top level class
class Character():

    def __init__(self, name, health, power):
        self.power = power
        self.health = health
        self.name = ""
    
    # Checks if the player is alive. Used in the battle loop.
    def isAlive(self):
        if (self.health <= 0):
            print(str(self.name) + " is dead." )
            return False
        else: return True
    
    #attack method
    def attack(self, defender):
        if isinstance(defender, zombie):
            pass
        else:
            defender.health = defender.health - self.power
            return defender.health

    # print method for the basic assignment. (not used in actual gameplay.)
    def printHealth(self):
        print("The health of the {} is {} and the power is {}".format(self.name, self.health, self.power))
    
    # Players turn.
    def choice(self, other):
        print("You have {} health and {} power.".format(hero.health, hero.power))
        print("The {} has {} health and {} power.".format(other.name, other.health, other.power))
        print()
        print("What do you want to do?")
        print("1. fight {}".format(other.name))
        print("2. do nothing")
        print("3. flee")
        print("> ",)
        user_input = input()
        if user_input == "1":
            self.attack(other)
            print("You do {} damage to the {}.".format(self.power , other.name ))
            if other.health <= 0:
                print("The {} is dead.".format(other.name))
        elif user_input == "2":
            return 2
        elif user_input == "3":
            print("Goodbye.")
            return 3
        else:
            print("Invalid input %r" % user_input)

# inherited from character. Sets the hero's turn.
class hero(Character):
    def __init__(self,name, health, power):
        self.power = power
        self.health = health
        self.name = name

# Zombie class for bonus assignment.
class zombie(Character):
    def __init__(self, name, health, power):
        self.name = name
        self.health = health
        self.power = power

# goblin class
class goblin(Character):
    def __init__(self,name, health, power):
        self.power = power
        self.health = health
        self.name = name

# battle loop.
def battle(hero, enemy):
    while (hero.isAlive() and enemy.isAlive()):
        hero.choice(enemy)
        enemy.attack(hero)

# Variables.
zard = zombie("zardilla",1,2)    
goblin = goblin("goblin",6, 2)
hero = hero("hero", 10, 5)

#function calls starts the battle loop.
battle(hero, zard)