import random

ListeTirIA = []
DejaTirerAleat = 1
coordIA = ""
Boat_Target = 0
Direction_Boat = 0
XY2 = ["X1","Y1","X-1","Y-1"]
XY = ["X1","Y1","X-1","Y-1"]
Tuple_Oexclue = (-4,-3,-2,-1,1,2,3,4)
Oexclue = []
for jkl in range (0,8):
    #print(Oexclue)
    Oexclue.append(int(Tuple_Oexclue[jkl]))
print(Oexclue)
Boat_Liste = ["1 1","1 2","1 3","1 4","5 5","4 5","3 5","8 8","8 9","10 9","10 10","4 3","4 4","2 9","3 9"]
toucher = 0
Toucher = 0
Couler_memo = 0
Invalide = 1
Couler = 0
DejaTirer = 1
tx = 0
ty = 0
txp = 0
typ = 0
txpp = 0
typp = 0
boats = {'Contre-torpilleur': ['4 7', '3 7', '2 7'], 'Croiseur': ['9 6', '9 7', '9 8', '9 9'], 'Torpilleur': ['10 2', '9 2'], 'Porte-avion': ['6 3', '6 4', '6 5', '6 6', '6 7'], 'Sous-marin': ['2 1', '3 1', '4 1']}

def Initialisation():
	
	YY = 0
	XX = 0
	
	for Xmoinsexclue in range(0,12):
	
	    XX = 0
	    YY = Xmoinsexclue
	    coordIAsetup = str(XX) + " " + str(YY)
	    ListeTirIA.append(coordIAsetup)
	    
	
	for Ymoinsexclue in range(0,12):
	
	    XX = Ymoinsexclue
	    YY = 0
	    coordIAsetup = str(XX) + " " + str(YY)
	    ListeTirIA.append(coordIAsetup)
	
	for Xplusexclue in range(0,12):
	
	    XX = 11
	    YY = Xplusexclue
	    coordIAsetup = str(XX) + " " + str(YY)
	    ListeTirIA.append(coordIAsetup)
	    
	
	for Yplusexclue in range(0,12):
	
	    XX = Yplusexclue
	    YY = 11
	    coordIAsetup = str(XX) + " " + str(YY)
	    ListeTirIA.append(coordIAsetup)
	
	print(ListeTirIA)

def ResetIA():

    global composition, BoatsIA, boats, tx, ty, DejaTirer, Couler, Toucher, Invalide, Couler_memo,Direction, Tuple_XY, x, y, TirX1, TirY1, TirX2, TirY2
    global txp, typ, typp, txpp, toucher, Boat_Liste, Oexclue, XY, Direction_Boat, Boat_Target, coordIA, DejaTirerAleat, ListeTirIA, Tuple_Oexclue

    XY = XY2[:]
    Tuple_Oexclue = (-4,-3,-2,-1,1,2,3,4)
    Oexclue = []
    for jkl in range (0,8):
        print(Oexclue)
        Oexclue.append(int(Tuple_Oexclue[jkl]))
    toucher = 0
    Toucher = 0
    Couler_memo = Couler_meme + 1
    Invalide = 1
    Couler = 0
    DejaTirerAleat = 1
    coordIA = ""
    Boat_Target = 0
    Direction_Boat = 0
    DejaTirer = 1

def Verif_Toucher():

    global composition, BoatsIA, bateautouché, boats, tx, ty, DejaTirer, Couler, Toucher, Invalide, Couler_memo,Direction, Tuple_XY, x, y, TirX1, TirY1, TirX2, TirY2
    global txp, typ, typp, txpp, toucher, Boat_Liste, Oexclue, XY, Direction_Boat, Boat_Target, coordIA, DejaTirerAleat, ListeTirIA, Tuple_Oexclue
    

    if [key for key in boats if coordIA in boats[key]] != []:

        print("                                         **Bateau toucher"+ " " + coordIA)
        Toucher = Toucher + 1
        toucher = 1
        bateautouché = [key for key in boats if coordIA in boats[key]]
        print("                       ^^ "+str(bateautouché))

        if boats[bateautouché[0]] == []:
            print("                                         bateau coulé")
            print("                       // "+str(bateautouché))
            boats.pop(bateautouché[0])
            Couler = 1
    else:
        print("                                         dans l'eau")
        toucher = 0

            
def Verif_Tir():

    global composition, BoatsIA, boats, tx, ty, DejaTirer, Couler, Toucher, Invalide, Couler_memo,Direction, Tuple_XY, x, y, TirX1, TirY1, TirX2, TirY2
    global txp, typ, typp, txpp, toucher, Boat_Liste, Oexclue, XY, Direction_Boat, Boat_Target, coordIA, DejaTirerAleat, ListeTirIA, Tuple_Oexclue
    
    
    if Boat_Target == 0: #en cas de tiraleat
        try:
            ListeTirIA.remove(coordIA)
            case = "deja"
            ListeTirIA.append(coordIA)
            #print("try1")
        except:
            #print("except1")
            DejaTirerAleat = 0
        Verif_Toucher()
        if toucher == 1:
            Boat_Target = 1
    else:
        if Direction_Boat == 0:
            
            if Direction == "X1":
                XY.remove("X1")
                print(str(Direction)+ " remove")
                try:
                    ListeTirIA.remove(coordIA)
                    case = "deja"
                    ListeTirIA.append(coordIA)
                    #print("try2")
                except:
                    #print("except2")
                    pass
                Verif_Toucher()
                if Toucher == 2:
                    Direction_Boat = 1
            else:
                if Direction == "X-1":
                    XY.remove("X-1")
                    print(str(Direction)+ " remove")
                    try:
                        ListeTirIA.remove(coordIA)
                        case = "deja"
                        ListeTirIA.append(coordIA)
                        #print("try3")
                    except:
                        #print("except3")
                        pass
                    Verif_Toucher()
                    if Toucher == 2:
                        Direction_Boat = 1
                else:
                    if Direction == "Y1":
                        XY.remove("Y1")
                        print(str(Direction)+ " remove")
                        try:
                            ListeTirIA.remove(coordIA)
                            case = "deja"
                            ListeTirIA.append(coordIA)
                            #print("try4")
                        except:
                            #print("except4")
                            pass
                        Verif_Toucher()
                        if Toucher == 2:
                            Direction_Boat = 1
                    else:
                        XY.remove("Y-1")
                        print(str(Direction)+ " remove")
                        try:
                            ListeTirIA.remove(coordIA)
                            case = "deja"
                            ListeTirIA.append(coordIA)
                            #print("try5")
                        except:
                            #print("except5")
                            pass
                        Verif_Toucher()
                        if Toucher == 2:
                            Direction_Boat = 1
        else:
            if Couler == 0:
                try:
                    ListeTirIA.remove(coordIA)
                    case = "deja"
                    ListeTirIA.append(coordIA)
                    print("la")
                    try:
                        typp = Oexclue.pop(typ)
                    except:
                        txpp = Oexclue.pop(txp)
                    
                except:
                    print("la2")
                    DejaTirer = 0
                Verif_Toucher()
                Toucher = Toucher + 1
            else:
                try:
                    ListeTirIA.remove(coordIA)
                    case = "deja"
                    ListeTirIA.append(coordIA)
                    print("ici")
                except:
                    print("ici2")
                    DejaTirer = 0
                Verif_Toucher()
                Toucher = Toucher + 1
                
           
        

def TirAleat():

    global composition, BoatsIA, boats, tx, ty, DejaTirer, Couler, Toucher, Invalide, Couler_memo,Direction, Tuple_XY, x, y, TirX1, TirY1, TirX2, TirY2
    global txp, typ, typp, txpp, toucher, Boat_Liste, Oexclue, XY, Direction_Boat, Boat_Target, coordIA, DejaTirerAleat, ListeTirIA, Tuple_Oexclue

    while DejaTirerAleat == 1:
        x = random.randint(1,10)
        y = random.randint(1,10)
        coordIA = str(x) + " " + str(y)
        Verif_Tir()
    TirX1 = x
    TirY1 = y
                                
        
def IATIR():

    global composition, BoatsIA, boats, tx, ty, DejaTirer, Couler, Toucher, Invalide, Couler_memo, Direction, Tuple_XY, x, y, TirX1, TirY1, TirX2, TirY2
    global txp, typ, typp, txpp, toucher, Boat_Liste, Oexclue, XY, Direction_Boat, Boat_Target, coordIA, DejaTirerAleat, ListeTirIA, Tuple_Oexclue

    if Boat_Target == 0:
        print("Tir random")
        TirAleat()
        ListeTirIA.append(coordIA)
        DejaTirerAleat = 1
    else:
        if Direction_Boat == 0:
            print("Choix direction" + " " + str(XY))
            L = len(XY)
            L2 = L - 1
            a = random.randint(0,L2)
            print("a="+str(a)+" L="+str(L)+" L2="+str(L2))
            Direction = XY[a]
            if Direction == "X1":
                print("X1")
                x = TirX1 + 1
                y = TirY1
                coordIA = str(x) + " " + str(y)
                Verif_Tir()
            else:
                if Direction == "X-1":
                    print("X-1")
                    x = TirX1 - 1
                    y = TirY1
                    coordIA = str(x) + " " + str(y)
                    Verif_Tir()
                else:
                    if Direction == "Y1":
                        print("Y1")
                        y = TirY1 + 1
                        x = TirX1
                        coordIA = str(x) + " " + str(y)
                        Verif_Tir()
                    else:
                        print("Y-1")
                        y = TirY1 - 1
                        x = TirX1
                        coordIA = str(x) + " " + str(y)
                        Verif_Tir()
                        ########################################
        else:

            TirX2 = x
            TirY2 = y
            
            if Couler == 0:
                if Direction == "X-1" or Direction == "X1":
                    while DejaTirer == 1:
                        tx = random.choice(Oexclue)
                        txp = Oexclue.index(tx)
                        print("txp = "+str(txp))
                        #print(type(txp))
                        print("tx = " + str(tx))
                        print(Oexclue)
                        int(tx)
                        y = TirY1 
                        x = TirX1 + tx
                        print("x y = ",x,y)
                        coordIA = str(x) + " " + str(y)
                        Verif_Tir()
                    txpp = Oexclue.pop(txp)
                    print("::  " + str(Oexclue))
                    DejaTirer = 1
                    
                
                    
                else:
                    while DejaTirer == 1:
                        print(Oexclue)
                        ty = random.choice(Oexclue)
                        typ = Oexclue.index(ty)
                        print("typ = "+str(typ))
                        #print(type(typ))
                        print("ty = " + str(ty))
                        
                        int(ty)
                        y = TirY1 + ty
                        x = TirX1
                        print("x y = ",x,y)
                        coordIA = str(x) + " " + str(y)
                        Verif_Tir()
                    
                    print("::  " + str(Oexclue))
                    DejaTirer = 1
                    

            else:
                print("couler")
                Reset()
                print("fini")

def Placement_bateau():

    global composition, BoatsIA, boats, tx, ty, DejaTirer, Couler, Toucher, Invalide, Couler_memo,Direction, Tuple_XY, x, y, TirX1, TirY1, TirX2, TirY2
    global txp, typ, typp, txpp, toucher, Boat_Liste, Oexclue, XY, Direction_Boat, Boat_Target, coordIA, DejaTirerAleat, ListeTirIA, Tuple_Oexclue

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
                

"""
Test
"""

Initialisation()
Placement_bateau()

print(boats)
print(" ")
a=-4
listetest = []
for i in range (0,9):
    listetest.append(a)
    a=a+1
print("listetest = "+ str(listetest))

print(" ")

for i in range (0,50):
    IATIR()
    print(coordIA)

print(" ")
print(ListeTirIA)
print(" ")
print(boats)
