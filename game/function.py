from random import *
from armes import *
from accueil import *
from combat import *
import os
clear = lambda: os.system('cls')
mes_armes={}
mes_armes ["Bow"] = bow=Bow("Curved bow")
mes_armes ["Sword"] = sword=Sword("longsword")
mes_armes ["IE"] = ie=IE("Infinity Edge")
mes_armes ["Bt"] = bt=Bt("Bloodthirst")


def isshop(player):
      if player.shopped == True :
          player.shopped = False
      else:
          shopyn = randint(1,100)
          if shopyn <=1 :
              player.shopped = True
              shop(player)
def isfight(player):
    if player.isfighting == True :
        player.isfighting = False
    else:
        fight= randint(1,100)
        if fight <= 99 :
            player.isfighting = True
            combat(player)
def shop(player):
    liste_weapon=["Sword","IE","Bt","Bow"]
    marchand=[]
    print("Bonjour jeune aventurier. Viens donc voir ce que je possède.")
    for i in range (0 , 3):
        weapon = randint(0,3)
        marchand.append(liste_weapon[weapon])
        print(liste_weapon[weapon]+ " coute " + str(mes_armes[liste_weapon[weapon]].cost)+"$.")
    choixshop(player,marchand)
def choixshop(player,marchand):
    choice=input("Veux tu quelque chose ? \n 1 pour oui 2 pour non\n")
    if choice == "1" or choice == "2":
        if int(choice) == 1:
            choixarmes(player, marchand)
            clear()
            print("Voici votre inventaire : ",player.inventory)
        if int(choice) == 2:
            accueil(player)
            clear()

    else:
        clear()
        print("Je n'ai pas compris")
        choixshop(player,marchand)

def choixarmes(player,marchand):
    print("Quel objet veux tu parmis ces 3 objets ?")
    choiceweap = input("Reponse :")
    if choiceweap == "1" or choiceweap == "2" or choiceweap == "3":
        if int(choiceweap) == 1:
            if player.money >= mes_armes[marchand[0]].cost :
                player.money-= mes_armes[marchand[0]].cost
                player.inventory.append(marchand[0])
                player.force+=mes_armes[marchand[0]].force
                player.agility+=mes_armes[marchand[0]].agility
                player.criticalStrike+=mes_armes[marchand[0]].criticalStrike
                player.sustain+=mes_armes[marchand[0]].sustain
                print(marchand[0],"a ete ajoute a votre inventaire")
            else:
                print("Vous n'avez pas assez d'argent !")
        if int(choiceweap) == 2:
            if player.money >= mes_armes[marchand[1]].cost :
                player.money-= mes_armes[marchand[1]].cost
                player.inventory.append(marchand[1])
                player.force+=mes_armes[marchand[1]].force
                player.agility+=mes_armes[marchand[1]].agility
                player.criticalStrike+=mes_armes[marchand[1]].criticalStrike
                player.sustain+=mes_armes[marchand[1]].sustain
                print(marchand[1],"a ete ajoute a votre inventaire")
            else:
                print("Vous n'avez pas assez d'argent !")
        if int(choiceweap) == 3:
            if player.money >= mes_armes[marchand[2]].cost :
                player.money-= mes_armes[marchand[2]].cost
                player.inventory.append(marchand[2])
                player.force+=mes_armes[marchand[2]].force
                player.agility+=mes_armes[marchand[2]].agility
                player.criticalStrike+=mes_armes[marchand[2]].criticalStrike
                player.sustain+=mes_armes[marchand[2]].sustain
                print(marchand[2],"a ete ajoute a votre inventaire")
            else:
                print("Vous n'avez pas assez d'argent !")
    else:
        clear()
        print("Je n'ai pas compris")
        choixarmes(player,marchand)
