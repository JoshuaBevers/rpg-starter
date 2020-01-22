# Hero class.
import random

# Creating Variables.
shadow = Shadow("Shadow", 1, 4, 0)
medic = Medic("Medic", 11, 1, 2)
zard = Zombie("zardilla",1,2)    
goblin = Goblin("goblin",6, 2, 1)
hero = Hero("hero", 10, 5, 1)


class Character():

    def __init__(self, name, health, power, defense):
        self.power = power
        self.health = health
        self.name = ""
        self.defense = defense
    
    def isAlive(self):
        if (self.health <= 0):
            return False
        else: return True

    def apply_damage(self, defender):
        damage = defender.block(self.attack())
        # if isinstance(defender, zombie):
        print("You made it to damage.")
        defender.health = defender.health - damage
        #     print('you are here.')
        #     pass
        # else:
        #     defender.health = defender.health - self.power
        #     return defender.health
        return defender.health

    def printHealth(self):
        print("The health of the {} is {} and the power is {}".format(self.name, self.health, self.power))
    
    def choice(self, other ):
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
            self.apply_damage(other)
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



class Hero(Character):

    def __init__(self,name, health, power, defense):
        self.power = power
        self.health = health
        self.name = name
        self.defense = defense
    def attack(self):
        num = random.randint(1,5)
        if num == 1:
            pot_damage = self.power * 2
            return pot_damage
        else: return self.power
    
class Zombie(Character):

    def __init__(self, name, health, power, defense):
        self.name = name
        self.health = health
        self.power = power
        self.defense = defense

    
    def block(self, attack_power):
        pot_damage = attack_power - self.defense
        return pot_damage
    
    def alive_status():
        return True

# goblin class
class Goblin(Character):

    def __init__(self,name, health, power, defense):
        self.power = power
        self.health = health
        self.name = name
        self.defense = defense

    def block(self, attack_power):
        damage = attack_power - self.defense
        return damage

class Medic(Character):

    def __init__(self,name, health, power, defense):
        self.power = power
        self.health = health
        self.name = name
        self.defense = defense
    def block(self, attack_power):
        num = random.randint(1,5)
        pot_damage = attack_power - self.defense
        if num == 1:
            pot_damage = pot_damage - 2
            return pot_damage
        else: return pot_damage

class Shadow(Character):

    def __init__(self,name, health, power, defense):
        self.power = power
        self.health = health
        self.name = name
        self.defense = defense
    def block(self, attack_power):
        num = random.randint(1,10)
        pot_damage = 0
        if num == 1:
            pot_damage = attack_power - self.defense
        return pot_damage

def game(hero, enemy):
    while (hero.isAlive() and enemy.isAlive()):
        hero.choice(enemy)
        print("you made it past choice.")
        print("The enemies health is: " + str(enemy.health))
        # enemy.attack(hero)


game(hero, shadow)