from tkinter import *
import socket, sys

# L'ip du serveur pour le socket est directement recuperer sur l'ordinateur
HOST = ([ip for ip in socket.gethostbyname_ex(socket.gethostname())[2] if not ip.startswith("127.")][0])
global role


def Rejoindre():

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
    ip_entry.pack(side=LEFT,padx=8,pady=8)
    port_label.pack(side=LEFT,padx=8,pady=8)
    port_entry.pack(side=LEFT,padx=8,pady=8)
    test_button.pack(side=LEFT,padx=8,pady=8)

    fenetre_connection.mainloop

def connection():

    print("Tentative de création d'un socket à l'adresse "+str(ip_serveur.get())+" sur le port "+str(port_serveur.get())+"...")
    # création du socket
    
    mySocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try :  
        mySocket.connect((ip_server.get(), int(port_serveur.get())))
        print("Socket créé. Connexion au serveur...")
        
        connexion.send(str("Vous etes connecte au serveur"+ str([ip for ip in socket.gethostbyname_ex(socket.gethostname())[2] if not ip.startswith("127.")][0])))
    except :
        print("Echec de la connection. Réessayez...")

    fenetre_connection.destroy()

def Serveur():
    role = 1    # role -> serveur(1) ou client(2) pour gerer le tour par tour
    fenetre_choix.destroy()
    
    print("Tentative de création d'un socket à l'adresse "+ HOST +" sur le port 50000...")

    try :
        mySocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        mySocket.bind((HOST, int(50000)))
        print("En attente d'un joueur...")
        mySocket.listen(5)
        connexion, adresse = mySocket.accept()
        
    except :
        print("Echec de la connection. Réessayez...")

   
"""
Fin definition des fonctions
"""

fenetre_choix = Tk()
fenetre_choix.title("Bataille Navale Connection  IP: " + str([ip for ip in socket.gethostbyname_ex(socket.gethostname())[2] if not ip.startswith("127.")][0]))

button_heber = Button(fenetre_choix, text = "Heberger une partie",font="arial 12 bold", command=Serveur)
button_rej = Button(fenetre_choix, text = "Rejoindre une partie",font="arial 12 bold", command=Rejoindre)
button_ia = Button(fenetre_choix, text = "Jouer contre l'IA",font="arial 12 bold")
taille_x_l = Label(fenetre_choix)
taille_y_b = Label(fenetre_choix)
info_ip = Label(fenetre_choix, text = "Votre IP: " +str([ip for ip in socket.gethostbyname_ex(socket.gethostname())[2] if not ip.startswith("127.")][0]))

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
