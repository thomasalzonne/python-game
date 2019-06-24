# -*- coding: utf-8 -*-
from random import *
import os
clear = lambda: os.system('cls')
from personnages import *
from accueil import *

def choixperso(nom):
    print("Très bien " + nom + "! Maintenant j'aimerai savoir quelle classe veux tu jouer.")
    print("1- Archer\n2- Guerrier")
    classe = input("Votre choix : ")
    if classe == "1" or classe == "2":
        if classe == "1" :
            player = Archer(nom)
            clear()
            print("Votre personnage a été créé!")
            accueil(player)
        if classe == "2" :
            player = Guerrier(nom)
            clear()
            print("Votre personnage a été créé!")
            accueil(player)
    else:
        clear()
        print("Je n'ai pas compris")
        choixperso(nom)

def main():
    print("Bonjour, bienvenue sur mon jeu python. Avant de jouer tu vas devoir répondre à deux questions.")
    print("Comment t'appelles tu?")
    nom = input("Votre prénom : ")
    if nom != "":
        choixperso(nom)
        clear()
    else:
        clear()
        print("Je n'ai pas compris")
        main()


if __name__== "__main__":
    main()
