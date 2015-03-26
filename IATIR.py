import random 

Boat_Target = 0
ListetirIA = []
Listeboats_J1 = ["1 2","1 3","1 4","1 5","5 3","6 3","7 3","8 3","9 3","10 3","10 10","9 10","1 1","5 5","6 7"]
coordIA = ""
DejaTirerAleat = 1
DejaTirerOriente = 1
ToucherDaffiler = 0
TirX1 = 0
TirY1 = 0
TirY2 = 0
TirX2 = 0
Orientation_tirX = [-1,1]
Orientation_tirY = [-1,1]
Orientation_test = 0
XouY = ["x","y"]

def Tir_IA():

    global CoulerFini
    global ListetirIA
    global boats_J1
    global coordIA
    global ToucherDaffiler
    global DejaTirerAleat
    global DejaTirerOriente
    global TirY1
    global TirX1
    global TirY2
    global TirX2
    global Orientation_tirX
    global Orientation_tirY
    global Orientation_test
    global Boat_Target
    global XouY
    
    if Boat_Target == 0:

        #tir aleatoire
        while DejaTirerAleat == 1:
            x = random.randint(1,10)
            y = random.randint(1,10)
            TirX1 = x
            TirY1 = y
            coordIA = str(x) + " " + str(y)
            try:
                ListetirIA.index(coordIA)
                DejaTirerAleat = 1
                Boat_Target = 1
            except:
                DejaTirerAleat = 0
                
                #TirIA()
        ListetirIA.append(coordIA)
        try:
            Listeboats_J1.remove(coordIA)
            print("toucher en " + coordIA)
            Boat_Target = 1
            ToucherDaffiler = ToucherDaffiler + 1
        except:
            pass
        DejaTirerAleat = 1

    else:

        if ToucherDaffiler == 1:
            #Definition de l'orientation du bateau
            Direction = random.choice(XouY)
            print(Direction)

            if Direction == "y":
                while DejaTirerOriente == 1:

                    PouM = random.choice(Orientation_tirY)
                    x = TirX1
                    y = TirY1 + PouM #-1 ou +1
                    TirX2 = x
                    TirY2 = y

                    try:
                        ListetirIA.index(coordIA)
                        DejaTirerOriente = 1
                    except:
                        DejaTirerOriente = 0

                ListetirIA.append(coordIA)

                try:
                    Listeboats_J1.remove(coordIA)
                    print("toucher en " + coordIA)
                    ToucherDaffiler = ToucherDaffiler + 1
                except:
                    Orientation_tirY.remove(PouM)

                DejaTirerOriente = 1

            else:
                while DejaTirerOriente == 1:
                    PouM = random.choice(Orientation_tirY)
                    x = TirX1 + PouM #-1 ou +1
                    y = TirY1             
                    TirX2 = x
                    TirY2 = y

                    try:
                        ListetirIA.index(coordIA)
                        DejaTirerOriente = 1
                    except:
                        DejaTirerOriente = 0
                ListetirIA.append(coordIA)
                try:
                    Listeboats_J1.remove(coordIA)
                    print("toucher en " + coordIA)
                    ToucherDaffiler = ToucherDaffiler + 1
                except:
                    Orientation_tirX.remove(PouM)

                DejaTirerOriente = 1

        else:
            pass

print(Listeboats_J1)
for gfd in range (1,30):
    Tir_IA()
    print(gfd)
print(ListetirIA)
print(Listeboats_J1)
    
            
            
                
                
