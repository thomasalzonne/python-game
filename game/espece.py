from function import *
from random import *
import os
clear = lambda: os.system('cls')
class Species:
    def __init__(self, name):
        self.name=name
        self.force=12
        self.pdv=50
        self.agility=20
        self.inventory=[]
    @staticmethod
    def swim(self):
        if self.energy - 3 > 0:
            self.energy -= 3
            return "Je nage"
    def walk(self):
        isfight(self)
        isshop(self)
        if self.energy - 1>0:
            self.energy-=1
            clear()
            print("J'avance")
            accueil(self)
        if self.energy - 1 <=0:
            print("Je devrais me reposer!")
            accueil(self)
    def healfight(self):
        if self.pa - 2 >= 0:
            self.pa-=2
            self.pdv += 5
            print("Je me suis soigné")
        else:
            print("Pas assez de PA")
    def heal(self):
        self.pdv+=5
        print("Soin effectue !")
        accueil(self)
    def bigattack(self,cible):
        if self.pa - 4 >= 0:
            self.pa-=4
            dodge = randint(1,100)
            crit = randint(1,100)
            if dodge> cible.agility*1.3:
                if crit>self.criticalStrike:
                    cible.pdv-=self.force
                    if self.sustain > 0:
                        self.pdv += (self.force/(self.sustain/100))
                    print("Hit!")
                else:
                    cible.pdv-=self.force*2
                    print("Critical Strikeeeeeee!!!")
            else:
                print("Echec cuisant ...")
        else:
            print("Pas assez de PA")
    def attack(self,cible):
        if self.pa - 3 >= 0:
            self.pa-=3
            dodge = randint(1,100)
            crit = randint(1,100)
            if dodge> cible.agility*0.8:
                if crit>self.criticalStrike:
                    cible.pdv-=self.force-4
                    if self.sustain>0:
                        self.pdv += self.force*0.45
                    print("Hit!")
                else:
                    cible.pdv-=(self.force-4)*2
                    print("Critical Strikeeeeeee!!!")
            else:
                print("Echec cuisant ...")
        else:
            print("Pas assez de PA")
    def sleep(self):
        self.energy+=8
        print("Zzzz")
        accueil(self)

    def findutour(self):
        self.pa = 6
        print("Fin du tour")
