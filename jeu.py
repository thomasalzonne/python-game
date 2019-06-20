from random import *

class Species:
    def __init__(self, name):
        self.name=name
        self.force=12
        self.pdv=50
        self.agility=20
        self.inventory=[]
    @staticmethod
    def swim(self):
        global day
        if self.energy - 3 > 0:
            self.energy -= 3
            return "Je nage"
    def walk(self):
        isfight(self)
        isshop(self)
        global day
        if self.energy - 1>0:
            self.energy-=1
            print("J'avance")
            day+=1
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
        global day
        self.energy+=8
        print("Zzzz")
        day+=1
        accueil(self)

    def findutour(self):
        self.pa = 6
        print("Fin du tour")
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

class Monster(Species):
    global day
    def __init__(self,name):
        self.name=name
        self.pa=4
        self.money = 30
        self.sustain = 0
        self.level = 1 + day -1
        self.exp = 120 * (1.1 * self.level)


class Human(Species):
    def __init__(self,name):
        self.name = name
        self.energy = 100
        self.exp = 0
        self.pa = 6
        self.level = 1
        self.money = 10
        self.sustain = 0
        self.isfighting=False
        self.shopped = False
        self.inventory=[]

class Monster_Warior(Monster):
    def __init__(self,name):
        self.force = 12
        self.criticalStrike = 10
        self.agility = 13
        self.pdv = 55

class Monster_Archer(Monster):
    def __init__(self,name):
        Monster.__init__(self,name)
        self.force = 8
        self.criticalStrike = 15
        self.agility = 18
        self.pdv = 50
class Guerrier(Human):
    def __init__(self,name):
        Human.__init__(self,name)
        self.force = 11
        self.criticalStrike = 8
        self.agility = 13
        self.pdv = 55
class Archer(Human):
    def __init__(self,name):
        Human.__init__(self,name)
        self.force = 8 + self.level - 1
        self.criticalStrike = 13 + (self.level * 0.5)
        self.agility = 20
        self.pdv = 48






def inventaire(player):
    print("Voici votre inventaire : ",player.inventory)
    accueil(player)

def isshop(player):
    if player.shopped == True :
        player.shopped = False
    else:
        shopyn = randint(1,100)
        if shopyn <=12 :
            player.shopped = True
            shop(player)
def shop(player):
    mes_armes={}
    mes_armes ["Bow"] = bow=Bow("Curved bow")
    mes_armes ["Sword"] = sword=Sword("longsword")
    mes_armes ["IE"] = ie=IE("Infinity Edge")
    mes_armes ["Bt"] = bt=Bt("Bloodthirst")
    liste_weapon=["Sword","IE","Bt","Bow"]
    marchand=[]
    print("Bonjour jeune aventurier. Viens donc voir ce que je possède.")
    for i in range (0 , 3):
        weapon = randint(0,3)
        marchand.append(liste_weapon[weapon])
        print(liste_weapon[weapon]+ " coute " + str(mes_armes[liste_weapon[weapon]].cost)+"$.")
    choice=input("Veux tu quelque chose ? \n 1 pour oui 2 pour non\n")
    if int(choice) == 1:
        print("Quel objet veux tu parmis ces 3 objets ?")
        choiceweap = input("Reponse :")
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

        print("Voici votre inventaire : ",player.inventory)
    if int(choice) == 2:
        accueil(player)

def isfight(player):
    if player.isfighting == True :
        player.isfighting = False
    else:
        fight= randint(1,100)
        if fight <= 25 :
            player.isfighting = True
            combat(player)

def combat(player):
    liste_monstre=["Monster_Archer","Monster_Warior"]
    mes_monstres={}
    mes_monstres ["Monster_Archer"] = Monster_Archer("César")
    mes_monstres ["Monster_Warior"] = Monster_Warior("césar")
    choixmonster = randint(0,1)
    boss = mes_monstres[liste_monstre[choixmonster]]

    print("Vous entrez en combat")
    while player.pdv>0 and boss.pdv>0:
        print("Vos hp :"+str(player.pdv)+" hp du monstre :"+str(boss.pdv))
        print("Vous avez "+str(player.pa)+" PA.")
        print("Que voulez-vous faire ?\n1-Attaque lourde\n2-Attaque légère\n3-Heal\n4-Fin du tour")
        select=input("Reponse :\n")
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
            accueil(player)
def accueil(player):
    global day
    choix=0
    print("C'est le jour "+str(day)+", vous êtes niveau "+str(player.level)+"\nvous avez "+str(player.energy)+" d'energie(s) et "+str(player.pdv)+" points de vie.\nVous avez " +str(player.money) + " $.")
    print("Voici les choix que vous avez : \n1- Avancer\n2- Inventaire\n3- Dormir\n4- Soin")
    choix = input("Que voulez vous faire :\n")
    if int(choix) == 1 :
        player.walk()
    elif int(choix) == 2 :
        inventaire(player)
    elif int(choix) == 3 :
        player.sleep()
    elif int(choix) == 4 :
        player.heal()


def main():
    global day
    day=1
    print("Bonjour, bienvenue sur mon jeu python. Avant de jouer tu vas devoir répondre à deux questions.")
    print("Comment t'appelles tu?")
    nom = input("Votre prénom : ")
    print("Très bien " + nom + "! Maintenant j'aimerai savoir quelle classe veux tu jouer.")
    print("1- Archer\n2- Guerrier")
    classe = input("Votre choix : ")
    if int(classe) == 1 :
        player = Archer(nom)
        print("Votre personnage a été créé!")
        accueil(player)
    if int(classe) == 2 :
        player = Guerrier(nom)
        print("Votre personnage a été créé!")
        accueil(player)

if __name__== "__main__":
    main()
