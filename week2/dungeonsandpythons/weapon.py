from random import random


class Weapon:
    def __init__(self, weapontype, damage, critical_strike_percent):
        if type(weapontype) is str:
            self.name = weapontype
        else:
            raise TypeError
        if type(damage) is int or type(damage) is float:
            self.damage = float(damage)
        else:
            raise TypeError
        if type(critical_strike_percent) is int or type(critical_strike_percent) is float:
            if critical_strike_percent >= 0 and critical_strike_percent <= 1:
                self.critical_strike_percent = critical_strike_percent
            elif critical_strike_percent < 0:
                self.critical_strike_percent = 0
            elif critical_strike_percent > 1:
                self.critical_strike_percent = 1
        else:
            raise TypeError

    def critical_hit(self):
        roll = random()
        if roll <= self.critical_strike_percent:
            print("Wow! A critical hit!")
            return True
        else:
            return False
