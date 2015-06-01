import random

def Initialisation_IA_hard(): #Definie toute les variable qui seront utilisee plus tard

    global Grille, CoordGrille, Boat_found, Boat_direction, Boats_joueur, Toucher,Croix, a_remove, Grande_Croix, Couler

    Grille = []
    for x in range (1,11): #Genere toute les coordonnees de la grille
        for y in range (1,11):
            CoordGrille = str(x) + " " + str(y)
            #                                                                                                               print(CoordTirIA)
            Grille.append(CoordGrille)
    print(Grille)
    Boat_found = 0
    Boat_direction = 0
    Boats_joueur = {'Contre-torpilleur': ['4 7', '3 7', '2 7'], 'Croiseur': ['9 6', '9 7', '9 8', '9 9'], 'Torpilleur': ['10 2', '9 2'], 'Porte-avion': ['6 3', '6 4', '6 5', '6 6', '6 7'], 'Sous-marin': ['2 1', '3 1', '4 1']}
    Toucher = 0
    Croix = []
    #                                                                                                                       print(len(Croix))
    a_remove = []
    Couler = 0
    Grande_Croix = []

    Placement_bateau()
   


def Reset_IA_hard(): #Permet a l'IA de rapartire en tir aleatoire suite a une erreur ou un bateau ennemie couler

    global Boat_found, Boat_direction, touche, Couler,Croix, Grande_Croix, a_remove

    if len(Grande_Croix) > 0: #Les coordonnees n'ayant pas ete tirer dans la derniere phase de tir son reinserer dans la grille afin de pouvoir les reutiliser
            for nbcase in range (0,(len(Grande_Croix))):
                Grille.append(Grande_Croix[nbcase])

    Toucher = 0
    Croix = []
    #                                                                                                                       print(len(Croix))
    a_remove = []
    Couler = 0
    Grande_Croix = []
    Boat_found = 0
    Boat_direction = 0
    print("                                                                               RESET")


def Tir_aleat(): #Choisie un lot de coordonnée parmit toute celle disponible dans Grille

    global Grille, Coord_Tir, Premiere_touche, Croix

    Coord_Tir = random.choice(Grille)
    print("Tir aleat " + str(Coord_Tir))
    Grille.remove(Coord_Tir)
    Premiere_touche = Coord_Tir
    Croix = []


    
def Croix_de_tir(): # La croix de tir correspond aux 4 cases qui entourent Premiere_touche 

    global Grille, Boat_found, Boat_direction, Coord_Tir, Premiere_touche, Croix, a_remove


    if len(Croix) == 0 :

        a_remove = []

        x = Premiere_touche.split(" ",1)[0]
        y = Premiere_touche.split(" ",1)[1]

        xbis = int(x) + 1    
        Croix.append(str(xbis) + " " + str(y))

        xbis = int(x) - 1
        Croix.append(str(xbis) + " " + str(y))

        ybis = int(y) + 1
        Croix.append(str(x) + " " + str(ybis))

        ybis = int(y) - 1
        Croix.append(str(x) + " " + str(ybis))

        for nbcase in range(0,len(Croix)): #On verifie si les coordonnees genere sont encore disponible

            try:
                Grille.remove(Croix[nbcase])
            except:
                a_remove.append(Croix[nbcase]) #On stocke les coordonnes qui se trouve dans Croix mais pas dans Grille (elles ont deja ete tirer)

        #                                                                                                                   print(a_remove)
        if len(a_remove) > 0:
            for nbcase in range (0,(len(a_remove)-1)):

                Croix.remove(a_remove[nbcase])

        #                                                                                                                   print("Croix = " + str(Croix))                 
    


def Generation_grande_croix(): #Il ne s'agit pas réellement d'une croix mais d'une ligne, on utilise toujours en case de reference Premiere_touche
                               #La ligne est horizontale ou verticale cela depend de Deuxieme_touche. Grande_Croix contient 7cases au maximum, case de reference +4 et -4
                               #exemple: Premiere_touche: "4 4" Deuxieme_touche: "4 5", le bateau est donc horizontale. Grande_Croix : "4 1", "4 2", "4 3", "4 6", "4 7", "4 8"

    global Grille, Boat_found, Boat_direction, Coord_Tir, Premiere_touche, Croix, Deuxieme_Touche, Grande_Croix

    if len(Croix) > 0: #On reintegre les coordonnees restante dans Croix dans la Grille afin de pouvoir les reutiliser
            for nbcase in range (0,(len(Croix))):
                Grille.append(Croix[nbcase])
                
            #                                                                                                               print("croix = " + str(Croix))
            Croix = []

    x1 = Premiere_touche.split(" ",1)[0]
    y1 = Premiere_touche.split(" ",1)[1]

    x2 = Deuxieme_Touche.split(" ",1)[0]
    y2 = Deuxieme_Touche.split(" ",1)[1]

    x1=int(x1); y1=int(y1); x2=int(x2); y2=int(y2)

    #                                                                                                                       print("len grande croix = " + str(len(Grande_Croix)))
    
    if len(Grande_Croix) == 0: #On ne regenre une liste que si elle vide ce qui n'arrive que suite a un reset
        if x1 - x2 == 0:
           #                                                                                                                print("je suis passer la ")
            for i in range (-4,5):
                if i != 110: #110 car avec 0 une erreur ce produisait, ce if est donc surement inutile
                    #                                                                                                       print("                        par la i=" + str(i))
                    y1bis  = y1+i
                    #                                                                                                       print("y1bis = " + str(y1))
                    tempe = str(x1) + " " + str(y1bis)
                    #print("tempe = " + str(tempe))
                    Grande_Croix.append(tempe)
                    try:
                        Grille.remove(tempe); 
                    except:
                        Grande_Croix.remove(tempe)           
        else:
            #                                                                                                               print("je suis passer la aussi ")
            for i in range (-4,5):
                if i != 110:
                    #                                                                                                       print("                        par la aussi i=" + str(i))
                    x1bis  = x1+i
                    #                                                                                                       print("y1bis = " + str(x1))
                    tempe = str(x1bis+1) + " " + str(y1)
                    #print("tempe = " + str(tempe))
                    Grande_Croix.append(tempe)
                    try:
                        Grille.remove(tempe)
                    except:
                        Grande_Croix.remove(tempe)
    #                                                                                                                       print("                                    Grande Croix = " + str(Grande_Croix))

                                  

        
    
    


def Tir_IA():

    global Grille, Boat_found, Boat_direction, Coord_Tir, Premiere_touche, Croix, Deuxieme_Touche, Couler, Grande_Croix


    if Boat_found == 0: #Si aucun bateau n'a ete trouver

        Tir_aleat()
        Verif_joueur_toucher()

    elif Boat_direction == 0: #Si un bateau a ete trouver mais que l'on ne connait sa direction
        
        Croix_de_tir()
        Coord_Tir = random.choice(Croix)
        Deuxieme_Touche = Coord_Tir
        print("Tir en " + str(Coord_Tir) + "^")
        Croix.remove(Coord_Tir)
        #                                                                                                                   print(Croix)
        Verif_joueur_toucher()

    else: #On termine de couler le navire ennemie

        #                                                                                                                   print("len croix = " + str(len(Croix)))
        Generation_grande_croix()
        try:
            Coord_Tir = random.choice(Grande_Croix)
            Grande_Croix.remove(Coord_Tir)
            print("Tir en " + str(Coord_Tir))
            Verif_joueur_toucher()
        except:
            Reset_IA_hard()
        
        
        #                                                                                                                   print("fait //")
        print(" ")
        
        


def Verif_joueur_toucher(): #On verifie si on a toucher un navire ennemie et si il est couler

    """
    Note a Leo: C'est surement dans cette fonction qu'il gerer la partie graphique de l'IA
    """

    global Grille, Boat_found, Boat_direction, Boats_joueur, Coord_Tir, Toucher, toucher, bateautouche, Premiere_touche, Couler
    
    if [key for key in Boats_joueur if Coord_Tir in Boats_joueur[key]] != []:
        
        print("                                         **Bateau toucher"+ " " + Coord_Tir)
        Toucher = Toucher + 1
        toucher = 1
        
        if Boat_found == 1:
            Boat_direction = 1
        
        Boat_found = 1
                   
        bateautouche = [key for key in Boats_joueur if Coord_Tir in Boats_joueur[key]]
        Boats_joueur[bateautouche[0]].remove(Coord_Tir)
        print("                       ^^ "+str(bateautouche))
        #                                                                                                                   print("on est la")

        if Boats_joueur[bateautouche[0]] == []:
            print("                                         bateau coulé")
            print("                       // "+str(bateautouche)+" coulé")
            Boats_joueur.pop(bateautouche[0])
            Reset_IA_hard() #Si couler alors reset
            #                                                                                                               print("on est la2")
    else:
        print("                                         dans l'eau")
        toucher = "non"
        #                                                                                                                   print("on est la3")



def Placement_bateau():

    global BoatsIA
    
    composition = 0

    composition = random.randint(0,10) #on choisie un composition aleatoirement en theorie on peut en rajouter autant que l'on veux
    print(" ")
    print("composition " + str(composition))
    print(" ")

    if composition == 0:
        BoatsIA = {'Porte-avion': ['2 2', '2 3', '2 4', '2 5', '2 6'], 'Croiseur': ['3 8', '4 8', '5 8', '6 8'], 'Contre-torpilleur': ['4 5', '4 4', '4 3'], 'Torpilleur': ['8 8', '8 9'], 'Sous-marin': ['7 5', '8 5', '9 5']}
    elif composition == 1:
        BoatsIA = {'Contre-torpilleur': ['9 8', '9 9', '9 10'], 'Torpilleur': ['3 4', '3 3'], 'Croiseur': ['1 6', '1 5', '1 4', '1 3'], 'Porte-avion': ['3 8', '4 8', '5 8', '6 8', '7 8'], 'Sous-marin': ['6 4', '7 4', '8 4']}
    elif composition == 2:
        BoatsIA = {'Croiseur': ['4 5', '4 4', '4 3', '4 2'], 'Torpilleur': ['9 6', '10 6'], 'Contre-torpilleur': ['6 8', '7 8', '8 8'], 'Porte-avion': ['3 6', '3 7', '3 8', '3 9', '3 10'], 'Sous-marin': ['7 4', '7 3', '7 2']}
    elif composition == 3:
        BoatsIA = {'Sous-marin': ['7 3', '6 3', '5 3'], 'Contre-torpilleur': ['6 7', '5 7', '4 7'], 'Porte-avion': ['10 3', '10 4', '10 5', '10 6', '10 7'], 'Torpilleur': ['8 5', '7 5'], 'Croiseur': ['4 5', '3 5', '2 5', '1 5']}
    elif composition == 4:
        BoatsIA = {'Croiseur': ['7 1', '8 1', '9 1', '10 1'], 'Sous-marin': ['8 10', '9 10', '10 10'], 'Porte-avion': ['6 10', '5 10', '4 10', '3 10', '2 10'], 'Torpilleur': ['3 1', '2 1'], 'Contre-torpilleur': ['1 3', '1 4', '1 5']}
    elif composition == 5:
        BoatsIA = {'Sous-marin': ['3 5', '3 4', '3 3'], 'Contre-torpilleur': ['5 5', '6 5', '7 5'], 'Torpilleur': ['6 7', '6 8'], 'Croiseur': ['4 7', '4 8', '4 9', '4 10'], 'Porte-avion': ['5 3', '6 3', '7 3', '8 3', '9 3']}
    elif composition == 6:
        BoatsIA = {'Croiseur': ['3 6', '4 6', '5 6', '6 6'], 'Sous-marin': ['3 4', '4 4', '5 4'], 'Contre-torpilleur': ['3 5', '4 5', '5 5'], 'Torpilleur': ['3 3', '4 3'], 'Porte-avion': ['3 7', '4 7', '5 7', '6 7', '7 7']}
    elif composition == 7:
        BoatsIA = {'Sous-marin': ['1 1', '2 1', '3 1'], 'Croiseur': ['6 6', '6 5', '6 4', '6 3'], 'Porte-avion': ['9 9', '8 9', '7 9', '6 9', '5 9'], 'Torpilleur': ['9 3', '9 4'], 'Contre-torpilleur': ['2 7', '2 8', '2 9']}
    elif composition == 8:
        BoatsIA = {'Sous-marin': ['8 4', '8 5', '8 6'], 'Porte-avion': ['3 5', '3 6', '3 7', '3 8', '3 9'], 'Contre-torpilleur': ['6 6', '6 7', '6 8'], 'Croiseur': ['4 3', '5 3', '6 3', '7 3'], 'Torpilleur': ['8 9', '9 9']}
    else:
        Placement_bateau()

    print(BoatsIA)
    print(" ")

""".....................................................
    TEST 
"""
def TEST():

    global Toucher, n, Boats_joueur
    
    Initialisation_IA_hard()
    n = 0
    
    while Toucher < 17 or len(Boats_joueur) != 0:
        n = n + 1
        print("                                                                    " + str(n))
        Tir_IA() 
    print("Tout le navire on ete couler")
               
"""
moyenne = []
m = 0

for couille in range (0,100):
    TEST()
    print(n)
    m = m + n
    moyenne.append(n)
print(moyenne)
print(m/len(moyenne))
"""

TEST()

"""

----------------Code useless-----------------------------

27201

Direction = random.choice(Liste_Direction)
        print("Direction " + Direction)
        Liste_Direction.remove(Direction)

        if Direction == "X1":

            x = Coord_Tir_1.split(" ")[0]
            print(x)
            print("")
            x = x + 1
            print(x)
            Coord_Tir = str(x) + " " + str(y)

        elif Direction == "X-1":

            x = Coord_Tir_1.split(" ")[0]
            print(x)
            print("")
            int(x)
            x = x - 1
            print(x)
            Coord_Tir = str(x) + " " + str(y)

        elif Direction == "Y1":

            y = Coord_Tir_1.split(" ")[1]
            print(y)
            print("")
            int(y)
            y = y + 1
            print(y)
            Coord_Tir = str(x) + " " + str(y)

        elif Direction == "Y-1":

            y = Coord_Tir_1.split(" ")[1]
            print(y)
            print("")
            int(y)
            y = y - 1
            print(y)
            Coord_Tir = str(x) + " " + str(y)

print(Grille); print(" "); print(Boats_joueur)
"""
