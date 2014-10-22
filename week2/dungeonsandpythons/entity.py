#

class Entity:
    def __init__(self, name, health):
        if type(name) is str:
            if name.isalpha():
                self.name = name
            else:
                raise ValueError
            if health == int(health) and health > 0:
                self.max_health = int(health) # in case the input value is float
                self.health = int(health)
            else:
                raise ValueError
            self.weapon = None
        else:
            raise TypeError
    def get_health(self):
        print("the character", self.name, " is at", self.health, "/", self.max_health, "health")
        return self.health
    
    def is_alive(self):
        if self.health > 0:
            print(self.name, "is alive and kickin'!(%d / %d)" % (self.health, self.max_health))
            return True
        else:
            print(self.name, "is gone from this world")
            return False
        
    def take_damage(self, damage_points):
        if damage_points > 0:
            self.health -= int(damage_points)
        else:
            print("you can't do negative damage!")
            return False
        
    def take_healing(self, healing_points):
        if self.is_alive():
            self.health += healing_points
        else:
            print("are you trying to raise the dead")
            return False
        if self.health > self.max_health:   
            self.health = self. max_health
        
    def has_weapon(self):
        if self.weapon == None:
            print("barely hands")
            return False
        else:
            #print("equipped with", self.weapon.name)
            return True
        
    def equip_weapon(self, weapon):
        self.weapon = weapon
        
    def attack(self):
        if self.has_weapon():
            damage = round(self.weapon.damage + self.weapon.damage * (self.weapon.critical_hit()))
            return damage
        else:
            damage = 0
            return damage
