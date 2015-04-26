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
    print(Oexclue)
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

    global boats, tx, ty, DejaTirer, Couler, Toucher, Invalide, Couler_memo,Direction, Tuple_XY, x, y, TirX1, TirY1, TirX2, TirY2
    global toucher, Boat_Liste, Oexclue, XY, Direction_Boat, Boat_Target, coordIA, DejaTirerAleat, ListeTirIA, Tuple_Oexclue

    XY = XY2[:]
    Tuple_Oexclue = (-4,-3,-2,-1,1,2,3,4)
    Oexclue = []
    Oexclue = Tuple_Oexclue[:]
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

    global boats, tx, ty, DejaTirer, Couler, Toucher, Invalide, Couler_memo,Direction, Tuple_XY, x, y, TirX1, TirY1, TirX2, TirY2
    global toucher, Boat_Liste, Oexclue, XY, Direction_Boat, Boat_Target, coordIA, DejaTirerAleat, ListeTirIA, Tuple_Oexclue

    if [key for key in boats if coordIA in boats[key]] == []:
        print("Bateau toucher"+ " " + coordIA)
        Toucher = Toucher + 1
        toucher = 1
    else:
        toucher = 0
            
def Verif_Tir():

    global boats, tx, ty, DejaTirer, Couler, Toucher, Invalide, Couler_memo,Direction, Tuple_XY, x, y, TirX1, TirY1, TirX2, TirY2
    global toucher, Boat_Liste, Oexclue, XY, Direction_Boat, Boat_Target, coordIA, DejaTirerAleat, ListeTirIA, Tuple_Oexclue
    
    if Boat_Target == 0: #en cas de tiraleat
        try:
            ListeTirIA.remove(coordIA)
            case = "deja"
            ListeTirIA.append(coordIA)
            print("try1")
        except:
            print("except1")
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
                    print("try2")
                except:
                    print("except2")
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
                        print("try3")
                    except:
                        print("except3")
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
                            print("try4")
                        except:
                            print("except4")
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
                            print("try5")
                        except:
                            print("except5")
                        Verif_Toucher()
                        if Toucher == 2:
                            Direction_Boat = 1
        else:
            if Couler == 0:
                try:
                    ListeTirIA.remove(coordIA)
                    case = "deja"
                    ListeTirIA.append(coordIA)
                    print("try1")
                except:
                    print("except1")
                    DejaTirer = 0
                Verif_Toucher()
                Toucher = Toucher + 1
           
        

def TirAleat():

    global boats, tx, ty, DejaTirer, Couler, Toucher, Invalide, Couler_memo,Direction, Tuple_XY, x, y, TirX1, TirY1, TirX2, TirY2
    global toucher, Boat_Liste, Oexclue, XY, Direction_Boat, Boat_Target, coordIA, DejaTirerAleat, ListeTirIA, Tuple_Oexclue

    while DejaTirerAleat == 1:
        x = random.randint(1,10)
        y = random.randint(1,10)
        coordIA = str(x) + " " + str(y)
        Verif_Tir()
    TirX1 = x
    TirY1 = y
                                
        
def IATIR():

    global boats, tx, ty, DejaTirer, Couler, Toucher, Invalide, Couler_memo,Direction, Tuple_XY, x, y, TirX1, TirY1, TirX2, TirY2
    global toucher, Boat_Liste, Oexclue, XY, Direction_Boat, Boat_Target, coordIA, DejaTirerAleat, ListeTirIA, Tuple_Oexclue

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
                        int(tx)
                        print("tx = " + str(tx))
                        x = TirX2 + tx
                        y = TirY2
                        Verif_Tir()
                    Oexclue.remove(tx)
                
                    
                else:
                    while DejaTirer == 1:
                        ty = random.choice(Oexclue)
                        print("ty = " + str(ty))
                        int(ty)
                        y = TirY2 + ty
                        x = TirX2
                        Verif_Tir()
                    Oexclue.remove(ty)

            else:
                print("couler")
                Reset()
        print("fini")


"""
Test
"""

Initialisation()

print(boats)

for i in range (0,15):
    IATIR()
    print(coordIA)
print(ListeTirIA)
print(Boats)
