class weapon:
    def __init__(self,name):
        self.name = name

class Sword(weapon):
    def __init__(self,name):
        self.name = name
        self.cost = 75
        self.force = 4
        self.agility = -2
        self.criticalStrike = 13
        self.sustain = 0

class Bt(weapon):
    def __init__(self,name):
        self.name = name
        self.cost = 250
        self.force = 6
        self.agility = -1
        self.criticalStrike = 0
        self.sustain = 5
class IE(weapon):
    def __init__(self,name):
        self.name = name
        self.cost = 230
        self.force = 7
        self.agility = -1
        self.criticalStrike = 25
        self.sustain = 0

class Bow(weapon):
    def __init__(self,name):
        self.name = name
        self.cost = 120
        self.force = 3
        self.agility = 8
        self.criticalStrike = 9
        self.sustain = 0
