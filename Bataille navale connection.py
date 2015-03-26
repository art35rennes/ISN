from tkinter import *
import socket, sys

# PREMIERE PARTIE : CONNECTION

# fonctions et commandes

def variable_default():
    ip_serveur = StringVar("192.168.1.33")
    port_serveur = StringVar(50000)
    g

    
def connection():
    print("Tentative de création d'un socket à l'adresse "+str(ip_serveur.get())+" sur le port "+str(port_serveur.get())+"...")
    # création du socket
    try :
        mySocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        mySocket.connect((ip_server.get(), int(port_serveur.get())))
        print("Socket rejoins. Connection au serveur")
        fenetre.destroy()
    except :
        print("Echec de la connection. Réessayez...")
    
# création de la fenêtre de connection
fenetre = Tk()
fenetre.title("Bataille Navale Connection")

# création des variables de connection

"""
ip_serveur = "192.168.102.172"
port_serveur = 50000
"""


ip_serveur = StringVar()
port_serveur = StringVar()

# création des widgets d'entrée
ip_label = Label(fenetre, text="IP :")
ip_entry = Entry(fenetre, width=14, text = ip_serveur)
port_label = Label(fenetre, text="Port :")
port_entry = Entry(fenetre, width=5, text = port_serveur)
test_button = Button(fenetre, text="Connection", command=connection)
test_defvariable = Button(fenetre, text="Ip test", command=variable_default)

# placement des widgets d'entrée dans fenetre
ip_label.pack(side=LEFT,padx=5,pady=5)
ip_entry.pack(side=LEFT,padx=5,pady=5)
port_label.pack(side=LEFT,padx=5,pady=5)
port_entry.pack(side=LEFT,padx=5,pady=5)
test_button.pack(side=LEFT,padx=5,pady=5)
test_defvariable.pack(side=LEFT,padx=5,pady=5)

# à ne pas oublier...
fenetre.mainloop()
