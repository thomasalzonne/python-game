from species import *
from random import *
import os
clear = lambda: os.system('cls')
class Personnage(Species) :
    def __init__(cls , game):
        Species.__init__(cls)
        cls.game = game
        cls.nom = ""
        cls.isfighting = False
        cls.shopped = False
        while cls.nom == "":
            print("Bonjour, bienvenue sur mon jeu python. Avant de jouer tu vas devoir répondre à deux questions.")
            print("Comment t'appelles tu?")
            cls.nom = input("Votre prénom : ")
        choice = 0
        while((choice != 1) & (choice != 2)):
            clear()
            choice = input("Ta classe, 1 pour être un guerrier et 2 pour être un archer")
            try:
                choice= int(choice)
            except ValueError:
                print("Pas un nombre")
                continue
            if (choice == 1):
                cls.force = 11
                cls.criticalStrike = 8
                cls.agility = 13
                cls.pdv = 55
                cls.classe = "Guerrier"
            if (choice == 2):
                cls.force = 8 + cls.level - 1
                cls.criticalStrike = 13 + (cls.level * 0.5)
                cls.agility = 20
                cls.pdv = 48
                cls.classe = "Archer"
    def isfight(cls):
        if cls.isfighting == True :
            cls.isfighting = False
        else:
            fight= randint(1,100)
            if fight <= 1 :
                cls.isfighting = True
                clear()
                print("combat")
                cls.game.combat()
    def walk(cls):
        cls.isfight()
        cls.isshop()
        if cls.energy - 1>0:
            cls.energy-=1
            print("J'avance")
        if cls.energy - 1 <=0:
            print("Pas assez d'énergie")

    def isshop(cls):
        if cls.shopped == True :
            cls.shopped = False
        else:
            shopyn = randint(1,100)
            if shopyn <=99 :
                cls.shopped = True
                cls.game.shop()
    def heal(cls):
        cls.pdv+=5
        print("Soin effectue !")

    def sleep(cls):
        cls.energy+=8
        print("Zzzz")

    def inventaire(cls):
        print("Voici votre inventaire : ",cls.inventory)
