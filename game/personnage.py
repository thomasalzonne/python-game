import espece

class Human(Species):
    def __init__(self,name):
        self.name = name
        self.energy = 100
        self.exp = 0
        self.pa = 6
        self.level = 1
        self.money = 1000
        self.sustain = 0
        self.isfighting=False
        self.shopped = False
        self.inventory=[]

class Guerrier(Human):
    def __init__(self,name):
        Human.__init__(self,name)
        self.force = 11
        self.criticalStrike = 8
        self.agility = 13
        self.pdv = 55
class Archer(Human):
    def __init__(self,name):
        Human.__init__(self,name)
        self.force = 8 + self.level - 1
        self.criticalStrike = 13 + (self.level * 0.5)
        self.agility = 20
        self.pdv = 48

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
