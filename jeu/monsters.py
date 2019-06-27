from species import *
class Monster(Species):
    def __init__(cls,name):
        cls.name=name
        cls.pa = 4
        cls.money = 30
        cls.sustain = 0
        cls.level = 1
        cls.exp = 120 * (1.1 * cls.level)

class Monster_Warior(Monster):
    def __init__(cls,name):
        Monster.__init__(cls,name)
        cls.force = 12
        cls.criticalStrike = 10
        cls.agility = 13
        cls.pdv = 55

class Monster_Archer(Monster):
    def __init__(cls,name):
        Monster.__init__(cls,name)
        cls.force = 8
        cls.criticalStrike = 15
        cls.agility = 18
        cls.pdv = 50
