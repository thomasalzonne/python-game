from personnage import *
from monsters import *
from random import *
from weapons import *

mes_armes={}
mes_armes ["Bow"] = bow=Bow("Curved bow")
mes_armes ["Sword"] = sword=Sword("longsword")
mes_armes ["IE"] = ie=IE("Infinity Edge")
mes_armes ["Bt"] = bt=Bt("Bloodthirst")

class Game:
    def __init__(cls):
        cls.player = Personnage(cls)

    def loop(cls):
        while(cls.player.pdv >0):
            print("Vous êtes level "+str(cls.player.level)+" vous avez "+str(cls.player.money)+" $ et vous avez "+str(cls.player.pdv)+" points de vie.")
            print("Voici les choix que vous avez : \n1- Avancer\n2- Inventaire\n3- Dormir\n4- Soin")
            choix = input("Que voulez vous faire :\n")
            if choix == "1" or choix == "2" or choix == "3" or choix == "4":
                if int(choix) == 1 :
                    cls.player.walk()
                if int(choix) == 2:
                    cls.player.inventaire()
                if int(choix) == 3:
                    cls.player.sleep()
                if int(choix) == 4:
                    cls.player.heal()
            else:
                clear()
                print("je n'ai pas compris")

    def combat(cls):
        liste_monstre=["Monster_Archer","Monster_Warior"]
        mes_monstres={}
        mes_monstres ["Monster_Archer"] = Monster_Archer("César")
        mes_monstres ["Monster_Warior"] = Monster_Warior("césar")
        choixmonster = randint(0,1)
        boss = mes_monstres[liste_monstre[choixmonster]]

        print("Vous entrez en combat")
        while cls.player.pdv>0 and boss.pdv>0:
            cls.choixcombat(boss)

    def choixcombat(cls,boss):
        print("Vos hp :"+str(cls.player.pdv)+" hp du monstre :"+str(boss.pdv))
        print("Vous avez "+str(cls.player.pa)+" PA.")
        print("Que voulez-vous faire ?\n1-Attaque lourde (4pa)\n2-Attaque légère (3pa)\n3-Heal (2pa)\n4-Fin du tour")
        select=input("Reponse :\n")
        if select == "1" or select == "2" or select == "3" or select == "4" :
            if int(select) == 1:
                cls.player.bigattack(boss)
            if int(select) == 2:
                cls.player.attack(boss)
            if int(select) == 3:
                cls.player.healfight()
            if int(select) == 4:
                cls.player.findutour()
                boss.bigattack(cls.player)
                boss.findutour()
                clear()
            if cls.player.pdv <= 0 :
                print("Vous avez perdu")
                exit()
            if boss.pdv <= 0 :
                print("Vous avez gagné")
                cls.player.money += boss.money
                cls.player.exp += boss.exp
                if cls.player.exp >= 100 * cls.player.level :
                    cls.player.exp -= 100 * cls.player.level
                    cls.player.level += 1
                cls.player.findutour()
                del boss
        else:
            clear()
            print("Je n'ai pas compris")
            choixcombat(boss)

    def shop(cls):
        liste_weapon=["Sword","IE","Bt","Bow"]
        marchand=[]
        print("Bonjour jeune aventurier. Viens donc voir ce que je possède.")
        for i in range (0 , 3):
            weapon = randint(0,3)
            marchand.append(liste_weapon[weapon])
            print(liste_weapon[weapon]+ " coute " + str(mes_armes[liste_weapon[weapon]].cost)+"$.")
        cls.choixshop(marchand)

    def choixshop(cls,marchand):
        choice=input("Veux tu quelque chose ? \n 1 pour oui 2 pour non\n")
        if choice == "1" or choice == "2":
            if int(choice) == 1:
                cls.choixarmes(marchand)
                clear()
                print("Voici votre inventaire : ",cls.player.inventory)
            if int(choice) == 2:
                clear()
        else:
            clear()
            print("Je n'ai pas compris")
            cls.choixshop(marchand)

    def choixarmes(cls,marchand):
        print("Quel objet veux tu parmis ces 3 objets ?")
        choiceweap = input("Reponse :")
        if choiceweap == "1" or choiceweap == "2" or choiceweap == "3":
            if int(choiceweap) == 1:
                if cls.player.money >= mes_armes[marchand[0]].cost :
                    cls.player.money-= mes_armes[marchand[0]].cost
                    cls.player.inventory.append(marchand[0])
                    cls.player.force+=mes_armes[marchand[0]].force
                    cls.player.agility+=mes_armes[marchand[0]].agility
                    cls.player.criticalStrike+=mes_armes[marchand[0]].criticalStrike
                    cls.player.sustain+=mes_armes[marchand[0]].sustain
                    print(marchand[0],"a ete ajoute a votre inventaire")
                else:
                    print("Vous n'avez pas assez d'argent !")
            if int(choiceweap) == 2:
                if cls.player.money >= mes_armes[marchand[1]].cost :
                    cls.player.money-= mes_armes[marchand[1]].cost
                    cls.player.inventory.append(marchand[1])
                    cls.player.force+=mes_armes[marchand[1]].force
                    cls.player.agility+=mes_armes[marchand[1]].agility
                    cls.player.criticalStrike+=mes_armes[marchand[1]].criticalStrike
                    cls.player.sustain+=mes_armes[marchand[1]].sustain
                    print(marchand[1],"a ete ajoute a votre inventaire")
                else:
                    print("Vous n'avez pas assez d'argent !")
            if int(choiceweap) == 3:
                if cls.player.money >= mes_armes[marchand[2]].cost :
                    cls.player.money-= mes_armes[marchand[2]].cost
                    cls.player.inventory.append(marchand[2])
                    cls.player.force+=mes_armes[marchand[2]].force
                    cls.player.agility+=mes_armes[marchand[2]].agility
                    cls.player.criticalStrike+=mes_armes[marchand[2]].criticalStrike
                    cls.player.sustain+=mes_armes[marchand[2]].sustain
                    print(marchand[2],"a ete ajoute a votre inventaire")
                else:
                    print("Vous n'avez pas assez d'argent !")
        else:
            clear()
            print("Je n'ai pas compris")
            cls.choixarmes(marchand)
