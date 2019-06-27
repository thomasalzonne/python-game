import os
from random import *
clear = lambda: os.system('cls')
class Species:
    def __init__(cls):
        cls.level=1
        cls.inventory=[]
        cls.energy=100
        cls.pa=6
        cls.sustain = 0
        cls.money = 1000
        cls.exp = 0
    def bigattack(cls,cible):
        if cls.pa - 4 >= 0:
            cls.pa-=4
            dodge = randint(1,100)
            crit = randint(1,100)
            if dodge> cible.agility*1.3:
                if crit>cls.criticalStrike:
                    cible.pdv-=cls.force
                    if cls.sustain > 0:
                        cls.pdv += (cls.force/(cls.sustain/100))
                    print("Hit!")
                else:
                    cible.pdv-=cls.force*2
                    print("Critical Strikeeeeeee!!!")
            else:
                print("Echec cuisant ...")
        else:
            print("Pas assez de PA")
    def attack(cls,cible):
        if cls.pa - 3 >= 0:
            cls.pa-=3
            dodge = randint(1,100)
            crit = randint(1,100)
            if dodge> cible.agility*0.8:
                if crit>cls.criticalStrike:
                    cible.pdv-=cls.force-4
                    if cls.sustain>0:
                        cls.pdv += cls.force*0.45
                    print("Hit!")
                else:
                    cible.pdv-=(cls.force-4)*2
                    print("Critical Strikeeeeeee!!!")
            else:
                print("Echec cuisant ...")
        else:
            print("Pas assez de PA")
    def healfight(cls):
        if cls.pa - 2 >= 0:
            cls.pa-=2
            cls.pdv += 5
            print("Je me suis soigné")
        else:
            print("Pas assez de PA")
    def findutour(self):
        self.pa = 6
        print("Fin du tour")
