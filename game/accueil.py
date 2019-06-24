import os
clear = lambda: os.system('cls')
def accueil(player):
    choix=0
    print("Vous êtes niveau "+str(player.level)+"\nvous avez "+str(player.energy)+" d'energie(s) et "+str(player.pdv)+" points de vie.\nVous avez " +str(player.money) + " $.")
    print("Voici les choix que vous avez : \n1- Avancer\n2- Inventaire\n3- Dormir\n4- Soin")
    choix = input("Que voulez vous faire :\n")
    if choix == "1" or choix == "2" or choix == "3" or choix == "4":
        if int(choix) == 1 :
            player.walk()
        elif int(choix) == 2 :
            inventaire(player)
        elif int(choix) == 3 :
            player.sleep()
        elif int(choix) == 4 :
            player.heal()
    else:
        clear()
        print("je n'ai pas compris")
        accueil(player)
