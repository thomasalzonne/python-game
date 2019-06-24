from random import *
from accueil import *
from plop import Monster_Warrior
import os
clear = lambda: os.system('cls')
Monster_Warrior.Monster_Warrior("césar")
mes_monstres={}
#mes_monstres ["boss_Warior"] = boss_Warrior = Monster_Warrior("césar")
#mes_monstres ["boss_Archer"] = boss_Archer = Monster_Archer("César")
def combat(player):
    liste_monstre=["boss_Archer","boss_Warior"]
    choixmonster = randint(0,1)
    mes_monstres[liste_monstre[choixmonster]]

    print("Vous entrez en combat")
    while player.pdv>0 and boss.pdv>0:
        choixcombat(player,boss)

def choixcombat(player,boss):
    print("Vos hp :"+str(player.pdv)+" hp du monstre :"+str(boss.pdv))
    print("Vous avez "+str(player.pa)+" PA.")
    print("Que voulez-vous faire ?\n1-Attaque lourde\n2-Attaque légère\n3-Heal\n4-Fin du tour")
    select=input("Reponse :\n")
    if select == "1" or select == "2" or select == "3" or select == "4" :
        if int(select) == 1:
            player.bigattack(boss)
        if int(select) == 2:
            player.attack(boss)
        if int(select) == 3:
            player.healfight()
        if int(select) == 4:
            player.findutour()
            boss.bigattack(player)
            boss.findutour()
            clear()
        if player.pdv <= 0 :
            print("Vous avez perdu")
            exit()
        if boss.pdv <= 0 :
            print("Vous avez gagné")
            player.money += boss.money
            player.exp += boss.exp
            if player.exp >= 100 * player.level :
                player.exp -= 100 * player.level
                player.level += 1
            player.findutour()
            del boss
            Monster.level += 1
            accueil(player)
    else:
        clear()
        print("Je n'ai pas compris")
        choixcombat(player,boss)
