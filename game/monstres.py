from espece import Species

class Monster(Species):
    def __init__(self,name):
        self.name=name
        self.pa = 4
        self.money = 30
        self.sustain = 0
        self.level = 1
        self.exp = 120 * (1.1 * self.level)

class Monster_Warrior(Monster):
    def __init__(self,name):
        Monster.__init__(self,name)
        self.force = 12
        self.criticalStrike = 10
        self.agility = 13
        self.pdv = 55

class Monster_Archer(Monster):
    def __init__(self,name):
        Monster.__init__(self,name)
        self.force = 8
        self.criticalStrike = 15
        self.agility = 18
        self.pdv = 50
