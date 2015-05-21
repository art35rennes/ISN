from tkinter import *
import socket, sys
from socket import gethostbyname_ex, gethostname

global role, iphost


def Rejoindre(): #appeler par le bouton rejoindre

    role = 2
    
    fenetre_choix.destroy()

    fenetre_connection = Tk()
    fenetre_connection.title("Bataille Navale Connection")
    
    global ip_serveur
    global port_serveur, fenetre_connection
    
    ip_serveur = StringVar()
    port_serveur = IntVar()

    port_serveur.set(50000)
    ip_serveur.set("192.168.")
    print(port_serveur.get())
    print(ip_serveur.get())

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

    fenetre_connection.mainloop()

    

def connection(): #appeler par la fonction rejoindre quand on clic sur connection

    global ip_serveur, port_serveur, iphost, fenetre_connection

    print(port_serveur.get())
    print(ip_serveur.get())
    
    print("Tentative de création d'un socket à l'adresse "+str(ip_serveur.get())+" sur le port "+str(port_serveur.get())+"...")
    
        
    # création du socket
    
    mySocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try :  

        mySocket.connect((ip_serveur.get(), int(port_serveur.get())))
        print("Socket créé. Connexion au serveur...")
        
    except socket.error:
        print("Echec de la connection. Réessayez...")
        sys.exit()

    print("Vous etes connecte au serveur"+ str(iphost))
    fenetre_connection.destroy()


def Serveur(): #appeler par valider

    global HOST, iphost
        
    role = 1    # role -> serveur(1) ou client(2) pour gerer le tour par tour
    """
    fenetre_attente = Tk()
    fenetre_attente.title("Attente de joueur")

    message = Label(fenetre_attente, text = "En attente de connexion d'un adversaire")

    message.pack(side=TOP)

    fenetre_attente.mainloop()
    """
    
    print("Tentative de création d'un socket à l'adresse "+ str(iphost) +" sur le port 50000...")
    mySocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    try :
        mySocket.bind(("localhost", int(50000)))
        print("En attente d'un joueur...")
                
    except socket.error:
        print("Echec de la connection. Réessayez...")
        sys.exit()

    mySocket.listen(40)
    connexion, adresse = mySocket.accept()

def Choix_IA():

    global fenetre_choix

    fenetre_choix.destroy()

    fenetre_IA = Tk()
    fenetre_IA.title("Choisissez un niveau d'IA")

    button_easy = Button(fenetre_IA, text = "Difficulté: Facile", font="arial 12 bold")
    button_medium = Button(fenetre_IA, text = "Difficulté: Moyenne", font="arial 12 bold")
    button_hard = Button(fenetre_IA, text = "Difficulté: Difficile", font="arial 12 bold")

    button_easy.pack(side=LEFT,padx=50,pady=10)
    button_medium.pack(side=LEFT,padx=50,pady=10)
    button_hard.pack(side=LEFT,padx=50,pady=10)

def Fenetre_ip(): #appeler par le bouton rejoindre

    role = 2
    
    fenetre_ip = Tk()
    fenetre_ip.title("Bataille Navale IP Host")
    
    global iphost
       
    iphost = StringVar()
        
    iphost.set("192.168.")
    print(iphost.get())

    # création des widgets d'entrée
    ip_label = Label(fenetre_ip, text="IP :", font="arial 10 bold")
    ip_entry = Entry(fenetre_ip, width=14, text = iphost)
    test_button = Button(fenetre_ip, text="Valider", font="arial 10 bold", command=fenetre_ip.destroy)

    # placement des widgets d'entrée dans fenetre
    ip_label.pack(side=LEFT,padx=8,pady=8)
    ip_entry.pack(side=LEFT,padx=16,pady=8)
    test_button.pack(side=LEFT,padx=8,pady=8)

    fenetre_ip.mainloop()
    print(iphost.get)

    
iphost = str(gethostbyname_ex(gethostname())[2])
iphost = str(iphost.split("'")[1])
#print(str(iphost.split("'")[1]))
print(iphost)
iphost="197.168.1.33"

if iphost.split(".",5)[0] != "192":
    
    Fenetre_ip()
    iphost = str(iphost)

#Debut du programme

fenetre_choix = Tk()
fenetre_choix.title("Bataille Navale Connection  IP: " + iphost)

button_heber = Button(fenetre_choix, text = "Heberger une partie",font="arial 12 bold",command=Serveur )
button_rej = Button(fenetre_choix, text = "Rejoindre une partie",font="arial 12 bold", command=Rejoindre)
button_ia = Button(fenetre_choix, text = "Jouer contre l'IA",font="arial 12 bold",command=Choix_IA)
taille_x_l = Label(fenetre_choix)
taille_y_b = Label(fenetre_choix)
info_ip = Label(fenetre_choix, text = "Votre IP: " + iphost)

taille_x_l.pack(side=TOP,padx=380,pady=20)
button_heber.pack(side=TOP,padx=50,pady=10)
button_rej.pack(side=TOP,padx=50,pady=10)
button_ia.pack(side=TOP,padx=50,pady=10)
taille_y_b.pack(side=TOP,pady=80)
info_ip.pack(side=BOTTOM)


fenetre_choix.mainloop()
