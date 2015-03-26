import random
"""
Bite in coming
"""
ListeTirIA = []
DejaTirerAleat = 1
coordIA = ""
Boat_Target = 0
Direction_Boat = False
Tuple_XY = XY = ("X1","Y1","X-1","Y-1")
XY = ["X1","Y1","X-1","Y-1"]
Tuple_Oexclue = (-4,-3,-2,-1,1,2,3,4)
Oexclue = []
Oexclue = Tuple_Oexclue[:]
Boat_Liste = ["1 1","1 2","1 3","1 4","5 5","4 5","3 5","8 8","8 9","10 10","4 3","4 4","2 9","3 9"]
toucher = 0

def Verif_Toucher():
    global Direction, Tuple_XY, x, y, TirX1, TirY1, TirX2, TirY2, toucher, Boat_Liste, Oexclue, XY, Direction_Boat, Boat_Target, coordIA, DejaTirerAleat, ListeTirIA, Tuple_Oexclue

    try:
        Boat_Liste.remove(coordIA)
        print("Bateau toucher")
        toucher = 1
    except:
        toucher = 0
        
def Verif_Tir():

    global Direction, Tuple_XY, x, y, TirX1, TirY1, TirX2, TirY2, toucher, Boat_Liste, Oexclue, XY, Direction_Boat, Boat_Target, coordIA, DejaTirerAleat, ListeTirIA, Tuple_Oexclue

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
        if Direction_Boat == False:
            if Direction == "X1":
                XY.remove("X1")
                try:
                    ListeTirIA.remove(coordIA)
                    case = "deja"
                    ListeTirIA.append(coordIA)
                    print("try2")
                except:
                    print("except2")
                Verif_Toucher()
                if toucher == 1:
                    Drection_Boat = True
            else:
                if Direction == "X-1":
                    XY.remove("X-1")
                    try:
                        ListeTirIA.remove(coordIA)
                        case = "deja"
                        ListeTirIA.append(coordIA)
                        print("try3")
                    except:
                        print("except3")
                    Verif_Toucher()
                    if toucher == 1:
                        Drection_Boat = True
                else:
                    if Direction == "Y1":
                        XY.remove("Y1")
                        try:
                            ListeTirIA.remove(coordIA)
                            case = "deja"
                            ListeTirIA.append(coordIA)
                            print("try4")
                        except:
                            print("except4")
                        Verif_Toucher()
                        if toucher == 1:
                            Drection_Boat = True
                    else:
                        XY.remove("Y-1")
                        try:
                            ListeTirIA.remove(coordIA)
                            case = "deja"
                            ListeTirIA.append(coordIA)
                            print("try5")
                        except:
                            print("except5")
                        Verif_Toucher()
                        if toucher == 1:
                            Drection_Boat = True
    
        
        

def TirAleat():

    global Direction, Tuple_XY, x, y, TirX1, TirY1, TirX2, TirY2, Boat_Liste, Oexclue, XY, Direction_Boat, Boat_Target, coordIA, DejaTirerAleat, ListeTirIA, Tuple_Oexclue

    while DejaTirerAleat == 1:
        x = random.randint(1,10)
        y = random.randint(1,10)
        coordIA = str(x) + " " + str(y)
        Verif_Tir()
    TirX1 = x
    TirY1 = y
                                
        
def IATIR():

    global Direction, Tuple_XY, x, y, TirX1, TirY1, TirX2, TirY2, Boat_Liste, Oexclue, XY, Direction_Boat, Boat_Target, coordIA, DejaTirerAleat, ListeTirIA, Tuple_Oexclue

    if Boat_Target == 0:
        print("Tir random")
        TirAleat()
        ListeTirIA.append(coordIA)
        DejaTirerAleat = 1
    else:
        if Direction_Boat == False:
            print("Choix direction")
            Direction = random.choice(XY)
            if Direction == "X1":
                print("X1")
                x = TirX1 + 1
                coordIA = str(x) + " " + str(y)
                Verif_Tir()
            else:
                if Direction == "X-1":
                    print("X-1")
                    x = TirX1 - 1
                    coordIA = str(x) + " " + str(y)
                    Verif_Tir()
                else:
                    if Direction == "Y1":
                        print("Y1")
                        y = TirY1 + 1
                        coordIA = str(x) + " " + str(y)
                        Verif_Tir()
                    else:
                        print("Y-1")
                        y = TirY1 - 1
                        coordIA = str(x) + " " + str(y)
                        Verif_Tir()
                        ########################################
        else:
            if Couler == 0:
                if Direction == "X-1" or Direction == "X1":
                    while DejaTirerAleat == 1:
                        x = random.choice(Oexclue)
                        if coordIA in ListeTirIA == False:
                            DejaTirerAleat = 0
                            TirX2 = x
                            TirY2 = y
                            coordIA = str(x) + " " + str(y)
                        else:
                            pass
                    
                    
                    ListeTirIA.append(coordIA)
                else:
                    while DejaTirerAleat == 1:
                        y = random.choice(Oexclue)
                        if coordIA in ListeTirIA == False:
                            DejaTirerAleat = 0
                            TirX2 = x
                            TirY2 = y
                            coordIA = str(x) + " " + str(y)
                        else:
                            pass
                    
                    ListeTirIA.append(coordIA)
            else:
                pass

print(Boat_Liste)
for i in range (0,10):
    IATIR()
    print(coordIA)
print(ListeTirIA)
print(Boat_Liste)
