from tkinter import *
import socket, sys
from socket import gethostbyname_ex, gethostname




global role

"""
"""
def Valider(): #appeler par la fonction IP_host
    global fenetre_hebergeur

    try:
        print(HOST.get())
    except:
        print(HOST)

    try:
        fenetre_hebergeur.destroy()
    except:
        pass

    Serveur()

"""
"""
def IP_host(): #appeler par le bouton heberger
    
    
    global HOST
    global fenetre_hebergeur
    
    HOST = StringVar()
    fenetre_choix.destroy()
    
    # L'ip du serveur pour le socket est directement recuperer sur l'ordinateur
    
    try:
        
        HOST = [ip for ip in socket.gethostbyname_ex(socket.gethostname())[2] if not ip.startswith("127.")][0]
        Valider()
    
    except:
        
        fenetre_hebergeur = Tk()
        fenetre_hebergeur.title("Bataille Navale IP")
         
        HOST = StringVar()
    
        # création des widgets d'entrée
        ip_label = Label(fenetre_hebergeur, text="Entrer votre IP :", font="arial 10 bold")
        ip_entry = Entry(fenetre_hebergeur, width=14, text = HOST)
        test_button = Button(fenetre_hebergeur, text="Valider", font="arial 10 bold", command=Valider)

        # placement des widgets d'entrée dans fenetre
        ip_label.pack(side=LEFT,padx=8,pady=8)
        ip_entry.pack(side=LEFT,padx=8,pady=8)
        test_button.pack(side=LEFT,padx=30,pady=8)

        fenetre_hebergeur.mainloop

"""
"""

def Rejoindre(): #appeler par le bouton rejoindre

    role = 2
    
    fenetre_choix.destroy()

    fenetre_connection = Tk()
    fenetre_connection.title("Bataille Navale Connection")
    
    global ip_serveur
    global port_serveur
    
    ip_serveur = StringVar()
    port_serveur = IntVar()

    # création des widgets d'entrée
    ip_label = Label(fenetre_connection, text="IP :", font="arial 10 bold")
    ip_entry = Entry(fenetre_connection, width=14, text = ip_serveur)
    port_label = Label(fenetre_connection, text="Port :", font="arial 10 bold")
    port_entry = Entry(fenetre_connection, width=5, text = port_serveur)
    test_button = Button(fenetre_connection, text="Connection", font="arial 10 bold", command=connection)

    # placement des widgets d'entrée dans fenetre
    ip_label.pack(side=LEFT,padx=8,pady=8)
    ip_entry.pack(side=LEFT,padx=16,pady=8)
    port_label.pack(side=LEFT,padx=8,pady=8)
    port_entry.pack(side=LEFT,padx=8,pady=8)
    test_button.pack(side=LEFT,padx=8,pady=8)

    fenetre_connection.mainloop

"""
"""

def connection(): #appeler par la fonction rejoindre quand on clic sur connection

    
    print("Tentative de création d'un socket à l'adresse "+str(ip_serveur.get())+" sur le port "+str(port_serveur.get())+"...")
    
        
    # création du socket
    
    mySocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try :  

        mySocket.connect((ip_server.get(), int(port_serveur.get())))
        print("Socket créé. Connexion au serveur...")
        
    except socket.error:
        print("Echec de la connection. Réessayez...")
        sys.exit()

    print("Vous etes connecte au serveur"+ str(HOST))
    fenetre_connection.destroy()

"""
"""

def Serveur(): #appeler par valider

    global HOST
        
    role = 1    # role -> serveur(1) ou client(2) pour gerer le tour par tour

    try:    
        print("Tentative de création d'un socket à l'adresse "+ str(HOST.get()) +" sur le port 50000...")
    except:
        print("Tentative de création d'un socket à l'adresse "+ str(HOST) +" sur le port 50000...")
    mySocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try :
        mySocket.bind((str(HOST), int(50000)))
        print("En attente d'un joueur...")
                
    except socket.error:
        print("Echec de la connection. Réessayez...")
        sys.exit()

    mySocket.listen(40)
    connexion, adresse = mySocket.accept()

   
"""
Fin definition des fonctions
"""


#Debut du programme

fenetre_choix = Tk()
fenetre_choix.title("Bataille Navale Connection  IP: " + str(gethostbyname_ex(gethostname())[2]))

button_heber = Button(fenetre_choix, text = "Heberger une partie",font="arial 12 bold",command=IP_host )
button_rej = Button(fenetre_choix, text = "Rejoindre une partie",font="arial 12 bold", command=Rejoindre)
button_ia = Button(fenetre_choix, text = "Jouer contre l'IA",font="arial 12 bold")
taille_x_l = Label(fenetre_choix)
taille_y_b = Label(fenetre_choix)
info_ip = Label(fenetre_choix, text = "Votre IP: " +str(gethostbyname_ex(gethostname())[2]))

taille_x_l.pack(side=TOP,padx=380,pady=20)
button_heber.pack(side=TOP,padx=50,pady=10)
button_rej.pack(side=TOP,padx=50,pady=10)
button_ia.pack(side=TOP,padx=50,pady=10)
taille_y_b.pack(side=TOP,pady=80)
info_ip.pack(side=BOTTOM)


fenetre_choix.mainloop()

"""
#Programme Bataille navale
"""

"""
#Jeu Partie Serveur
"""

"""
#Jeu Partie Client
"""