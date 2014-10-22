from entity import Entity

class Hero(Entity):
    def __init__(self, name, health, nickname):
        super().__init__(name, health)
        if nickname.isalpha():
            self.nickname = nickname
        else:
            raise ValueError
            
    def known_as(self):
        fullnick = self.name + " the " + self.nickname
        #print(fullnick)
        return fullnick