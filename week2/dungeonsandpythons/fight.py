from random import random


class Fight:
    def __init__(self, hero, villain):
        roll = random()
        if roll < 0.5:
            self.firststrike = hero.name
        else:
            self.firststrike = villain.name
        self.simulate_fight(hero, villain)

    def compute_round(self, attacker, defender):
        if attacker.has_weapon():
            print(attacker.name, "swings", attacker.weapon.name)
            damage = attacker.attack()
            print(defender.name, "takes", damage, "points of damage")
            defender.take_damage(damage)

            if not defender.is_alive():
                print("looks like that was all from", defender.name)
                self.outcome = "The winner is " + str(attacker.name)
        elif not attacker.has_weapon():
            print(attacker.name, "flex muscles and tries to wrestle with", defender.name, "but to no avail")
            print("maybe", attacker.name, "would do better with a weapon")

    def simulate_fight(self, hero, villain):
        self.round = 0
        self.outcome = None
        while self.outcome == None:
            print("----- round:", self.round,"-----")
            if self.round == 0:
                print("Behold! A mighty clash is about to begin")
                print("Our hero,", hero.name, "also known as", hero.known_as())
                print("has challanged a devious adversary -", villain.name, "!")
                print("\n\n The two fighters looks at each other, viciously")
                print("it seems", self.firststrike, "is taking the initiative!")
                
            elif self.round == 1:
                if self.firststrike == hero.name:
                    self.turn = 1
                    self.compute_round(hero, villain)
                elif self.firststrike == villain.name:
                    self.turn = 2
                    self.compute_round(villain, hero)
            elif (self.round+self.turn) % 2 == 0:
                self.compute_round(hero, villain)
            elif (self.round+self.turn) % 2 == 1:
                self.compute_round(villain, hero)

            self.round+=1
        print(self.outcome)