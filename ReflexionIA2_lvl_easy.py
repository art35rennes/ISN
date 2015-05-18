import random

def Initialisation_easy():

    global Grille, CoordGrille, Boat_found, Boat_direction, Boats_joueur, Toucher, nbtir

    Grille = []
    for x in range (1,11):
        for y in range (1,11):
            CoordGrille = str(x) + " " + str(y)
            #print(CoordTirIA)
            Grille.append(CoordGrille)
    print(Grille)
    Boat_found = "non"
    Boat_direction = "non"
    Boats_joueur = {'Contre-torpilleur': ['4 7', '3 7', '2 7'], 'Croiseur': ['9 6', '9 7', '9 8', '9 9'], 'Torpilleur': ['10 2', '9 2'], 'Porte-avion': ['6 3', '6 4', '6 5', '6 6', '6 7'], 'Sous-marin': ['2 1', '3 1', '4 1']}
    Toucher = 0
    nbtir = 0
    Placement_bateau()


def Tir_aleat_easy():

    global Grille, Coord_Tir, nbtir

    Coord_Tir = random.choice(Grille)
    print("Tir aleat " + str(Coord_Tir))
    Grille.remove(Coord_Tir)
    Verif_joueur_toucher()
    nbtir = nbtir + 1



def Verif_joueur_toucher():

    global Grille, Boat_found, Boat_direction, Boats_joueur, Coord_Tir, Toucher, toucher, bateautouche
    
    if [key for key in Boats_joueur if Coord_Tir in Boats_joueur[key]] != []:

        print("                                         **Bateau toucher"+ " " + Coord_Tir)

        Toucher = Toucher + 1
        toucher = "non"
        bateautouche = [key for key in Boats_joueur if Coord_Tir in Boats_joueur[key]]

        print("                       ^^ "+str(bateautouche))

        if Boats_joueur[bateautouche[0]] == []:
            print("                                         bateau coulé")
            print("                       // "+str(bateautouche))
            boats.pop(bateautouche[0])
            Couler = "oui"
    else:
        print("                                         dans l'eau")
        toucher = "non"



def Placement_bateau():

    global BoatsIA
    
    composition = 0

    composition = random.randint(0,10)
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

def Tir_IA_easy():

    while Toucher < 17:
        Tir_aleat_easy()

    if Toucher == 17:
        print("Tout les bateaux ennemies on été coulé")


""".....................................................
    TEST 
"""

Initialisation_easy()

Tir_IA_easy()

print(nbtir) 
