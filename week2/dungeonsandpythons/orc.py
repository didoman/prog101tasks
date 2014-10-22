from entity import Entity


class Orc(Entity):
    def __init__(self, name, health, berserk_factor):
        super().__init__(name, health)
        if type(berserk_factor) is int:
            berserk_factor = float(berserk_factor)
            self.berserk_factor = berserk_factor
        elif type(berserk_factor) is float and berserk_factor < 1.0:
            berserk_factor = 1.0
            self.berserk_factor = berserk_factor
        elif type(berserk_factor) is float and berserk_factor > 2.0:
            berserk_factor = 2.0
            self.berserk_factor = berserk_factor
        elif type(berserk_factor) is float:
            self.berserk_factor = berserk_factor
        else:
            raise TypeError
        self.is_in_berserk = False
        
    def go_berserk(self):
        # orcs goes berserk below 60% health
        if self.health < self.max_health * 0.6 and self.health > 0:
            self.is_in_berserk = True
            print(self.name, "looks enraged!")
        else:
            print(self.name, "cannot go berserk right now")
        return self.is_in_berserk

    def is_alive(self):
        self.go_berserk()
        return Entity.is_alive(self)

    def attack(self):
        damage = Entity.attack(self)
        return round(damage + damage * self.is_in_berserk * self.berserk_factor)
    
        
    