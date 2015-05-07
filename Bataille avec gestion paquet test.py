




"""
BIG TODO :
fonctions doivent écrire un paquet prêt à être décodé

le paquet sera envoyé par la fonction paquetsender (temporairement dans la console), et interpreté par paquethandler

TODO :
ne pas pouvoir jouer tant que tous les bateaux ne sont pas placés
séparer "use" en 2 : un qui fait le paquet et l'autre qui affiche les résultats

tir en 3 temps : 1) on envoie paquet avec shootedpos et selectedbonus
				 2) adversaire recoit paquet, et renvoie les positions touchées ou non (sous forme de dict), adversaire affiche le resultat
				 3) on recoit le dict des pos touchées, et on affiche le résultat
"""












import tkinter as tk



"""
Début partie profil (sauvegarde a pouvoir retrouver)
"""



# import tkinter as tk
from tkinter import filedialog # why !
import base64
import pickle

profileasking = tk.Tk()
profileasking.title("Make your profile !") 

profiledict = {"username" : "", "comment" : "", "image" : None}

imagestring = ""

def imagesearcher():
	global profiledict, imagestring
	imagepath = filedialog.askopenfilename(filetypes = [("Gif images only !", ".gif")] ) # why not tk.filedialog.askopenfilename() ?
	
	if imagepath == "":
		return
	
	with open(imagepath, "rb") as imagefile:
		imagestring = base64.b64encode(imagefile.read())
	
	
	
	image = tk.PhotoImage(data=imagestring)
	profiledict["image"] = image
	imagelabel.config(image=profiledict["image"])



def profileoutput():
	global profiledict, imagestring
	profiledict["image"] = imagestring
	profiledict["username"] = usernameget.get()
	profiledict["comment"] = commentget.get()
	print(profiledict)
	
	
	
	
	
	
	
	with open("/media/prof/USB DISK/Bataille navale/info", "rb+") as savefile: # attention changer le chemin selon l'os
		
		
		"""
		savefile.truncate()
		savefile.write(profiledict["username"] + "\n")
		savefile.write(str(profiledict["image"]))
		savefile.close()
		"""
		
		# on utilise pickle pour la sauvegarde et la retrouvaille du profil
		
		savefile.truncate()
		
		profilepickler = pickle.Pickler(savefile)
		profilepickler.dump(profiledict)
		
		
		
	profileasking.destroy()

def loadsavefile():
	global profiledict
	profilepath = filedialog.askopenfilename(filetypes = [("Your save file !", "info")])

	if profilepath == "":
		return
	
	with open(profilepath, "rb") as savefile:
		
		"""
		profiledict["username"].set(profiledata.readline())
		profiledict["image"] = profiledata.readline()
		"""
		profiledepickler = pickle.Unpickler(savefile)
		profiledict = profiledepickler.load() 
		
	print(profiledict)
		
	# print(profiledict["image"])
	
	usernameget.config(text=profiledict["username"])
	
	
	image = tk.PhotoImage(data=profiledict["image"])
	profiledict["image"] = image
	imagelabel.config(image=profiledict["image"])



# tk.filedialog.askopenfilename()




askusername = tk.Label(profileasking, text="Username")
usernameget = tk.Entry(profileasking, width=10)
askcomment = tk.Label(profileasking, text="Comment")
commentget = tk.Entry(profileasking, width=80)
askimage = tk.Label(profileasking, text="Image")
imageget = tk.Button(profileasking, text="Browse... !", command=imagesearcher)
imagelabel =  tk.Label(profileasking, image=profiledict["image"])
profilegetter = tk.Button(profileasking, text="I'm done !", command=profileoutput)
profileloader = tk.Button(profileasking, text="Load an existing profile", command=loadsavefile)


askusername.grid(row=1, column=0)
usernameget.grid(row=1, column=1)


#askcomment.grid(row=2, column=0)
#commentget.grid(row=2, column=1)


askimage.grid(row=3, column=0)
imageget.grid(row=3, column=1)
imagelabel.grid( column=2)
profilegetter.grid(row=4, column=0, columnspan=2)
profileloader.grid(row=5, column=0, columnspan=2)

profileasking.mainloop()






"""
Fin partie profil
"""






"""
Insérer partie réseau
"""


# on affiche temporairement les paquets envoyés dans le widget "paquetdisplayer", en vert, ce qu'on envoie, en rouge, ce qu'on recoit


def paquetsender(string):
	paquet = string
	
	paquetdisplayer.insert("end", string + "\n", "sended")
	
	# on envoie le paquet pour pouvoir le gerer de l'autre côté

	paquethandler(paquet) # test local


	

#	paquetdisplayer.tag_config("received", background="red")
#	paquetdisplayer.tag_config("sended", foreground="green")










































def paquethandler(paquet):
	
	

	# récupération du paquet

	

	
	
	
	if paquet[0] == "g": # paquet lié au jeu
		paquet = paquet[1:]
		
		if paquet == "ready":
			modifyhistorique("Votre adversaire est prêt !", "info")
			
			
			paquetdisplayer.insert("end", "genemyisready" "\n", "received")	
			
			
			return
		elif paquet.split(",")[0] in bonuslist or paquet.split(",")[0] == None:
			paquetdisplayer.insert("end", "genemyisusing " + paquet.split(",")[0] +" on " + paquet.split(",")[1] + "\n", "received")	
			pass
		
		pass
		
		"""
		format d'un paquet jeu :
		
		str(bonus) + "," + str(shootedpos) (bonus = None si pas de bonus sélectionné)
		
		OU
		
		"ready" (le joueur à placé ses bateaux)
		"""
		
	if paquet[0] == "c": # paquet lié au chat
		paquet = paquet[1:]
		pass
		
		"""
		format d'un paquet chat : 
		"message"
		"""
		
	if paquet[0] == "p": # paquet lié au profil
		paquet = paquet[1:]
		pass
		
		"""
		format d'un paquet profil :
		"pseudo" + "," + "image" (image encodée en base64; pseudo = None ou image = None si pas selectionnée)
		"""
































































































"""
Fin partie réseau
"""




"""
Début sélection bonus
"""

asking = tk.Tk()
asking.title("Bonus")


bonuslist = ["Avion", "Radar", "Bombe", "Missile perforant"]
bonusdict = {"Avion": tk.IntVar(), "Radar": tk.IntVar(), "Bombe": tk.IntVar(), "Missile perforant": tk.IntVar()}
bonuscost = {"Avion": 3, "Radar": 5, "Bombe": 9, "Missile perforant": 5}
points = 30
pointsleft = tk.IntVar()
pointsleft.set(points)







'''

def autoupdate(event):
	asking.wait_variable(pointsleft)
	
	
	for bonus in bonusdict:
		pointsleft.set(pointsleft - (asking.grid_slaves(row=bonuslist.index(bonus), column=1)[0].get()*bonuscost[bonus]))
	print(pointsleft)
	
	displaypoint.config(text="Points left = "+ str(pointsleft))
	
	#	pointsused = 
	
	#	bonustochange = event.widget.cget(text)event.widget.grid_info()[row]
	
	#	print(event.widget.grid_info())
	#	print(event.widget.option_get("x", grid))
	
	print(asking.grid_slaves(row=event.widget.grid_info()["row"], column=0)[0].cget("text"))
	
	#
	#			au dessus donne le bonus selectionne
	#	
	
	
	for bonus in bonuslist:
		asking.grid_slaves(row=bonuslist.index(bonus), column=1)[0].config(to=int(pointsleft/bonuscost[bonus]))
	
	
	bonusdict["Avion"]
	bonusdict["Radar"]
	bonusdict["Bombe"]
	bonusdict["Missile perforant"]
'''


def ready():
	
	for bonus in bonusdict:
		bonusdict[bonus] = bonusdict[bonus].get()

	
	print(bonusdict)
	
	
	asking.destroy()
	







def update(event):
	# 1. get event (add or remove a bonus)
	# 2. which bonus
	# 3. do it if possible and change points
	
	"""
	pointsleft.set(points)
	for bonus in bonusdict:
		pointsleft.set(pointsleft.get() - (asking.grid_slaves(row=bonuslist.index(bonus), column=1)[0].get()*bonuscost[bonus]))
		asking.grid_slaves(row=bonuslist.index(bonus), column=1)[0].config(to=int(asking.grid_slaves(row=bonuslist.index(bonus), column=1)[0].cget("to") + int(pointsleft.get()/bonuscost[bonus])))
		print(asking.grid_slaves(row=bonuslist.index(bonus), column=1)[0].cget("to"))
	print(pointsleft.get()/bonuscost["Avion"], "For plane")
	"""
	
	
	todo = event.widget.cget("text")
	selectedbonus = asking.grid_slaves(row=event.widget.grid_info()["row"], column=0)[0].cget("text")
	print(event.widget.grid_info()["row"])
	print(todo)
	print(selectedbonus)


	if todo == "+":
		if pointsleft.get() >= bonuscost[selectedbonus]:
			pointsleft.set(pointsleft.get() - bonuscost[selectedbonus])
			bonusdict[selectedbonus].set(bonusdict[selectedbonus].get() + 1)
		pass
	
	
	if todo == "-":
		if bonusdict[selectedbonus].get() > 0:
			pointsleft.set(pointsleft.get() + bonuscost[selectedbonus])
			bonusdict[selectedbonus].set(bonusdict[selectedbonus].get() - 1)
		pass
	
	
	displaypoint.config(text="Points left = "+ str(pointsleft.get()))
	


for bonus in bonusdict:
	text = tk.Label(asking, text=bonus)
	value = tk.Label(asking, textvariable=bonusdict[bonus])
	buttonplus = tk.Label(asking, text="+", font=("Arial", 20))
	buttonmoins = tk.Label(asking, text="-", font=("Arial", 20))
	buttonplus.bind("<Button-1>", update)
	buttonmoins.bind("<Button-1>", update)
#	scale = tk.Scale(asking, from_=0, to=3, orient="horizontal", variable=bonusdict[bonus], command=update)
#	scale.bind("<Button-1>", autoupdate)
	print(bonusdict[bonus])
	text.grid(row=bonuslist.index(bonus), column=0)
#	scale.grid(row=bonuslist.index(bonus), column=1)
	buttonplus.grid(row=bonuslist.index(bonus), column=3)
	value.grid(row=bonuslist.index(bonus), column=2)
	buttonmoins.grid(row=bonuslist.index(bonus), column=1)




displaypoint = tk.Label(asking, text="Points left = "+ str(points))
displaypoint.grid(columnspan=4, row=len(bonuslist))

button = tk.Button(asking, text="Ready", command=ready)
button.grid(columnspan=4, row=len(bonuslist)+1)


asking.mainloop()


"""
Fin partie selection bonus
"""






"""
Début du jeu :P
"""













fenetre = tk.Tk() #fenetre nécessaire pour variables objet















#imagedict = {"Fire": tk.PhotoImage(file="Fire.png")}











'''


nametowidget(name)

    Gets the widget object corresponding to a widget name.


'''





# paused = False



placepos = ""
placeside = ""
boatsize = ""
boatname = ""
postoplace = []
posplaced = []
selectedbonus = ""
boats = {}

bonuslist = ["Avion", "Radar", "Bombe", "Missile perforant"]

bateauxlist = ["Porte-avion (5 cases)", "Croiseur (4 cases)", "Contre-torpilleur (3 cases)", "Sous-marin (3 cases)", "Torpilleur (2 cases)"]

boatslefts = [boat[0:boat.index(" ")] for boat in bateauxlist]


key = tk.StringVar()

def onboatclick():
	global placeside, placepos, boatsize, boatname, postoplace, boatslefts, boats
	
	postoplace = []
	
	if placepos != "" and placeside != "" and boatsize != "" and boatname in boatslefts:
		if placeside == "Left":
			placeside = [0, -1]
		if placeside == "Right":
			placeside = [0, 1]
		if placeside == "Up":
			placeside = [-1, 0]
		if placeside == "Down":
			placeside = [1, 0]
			
		
		
		maxpos = [int(placepos[0])+int(placeside[0])*int(boatsize), int(placepos[1])+int(placeside[1])*int(boatsize)]
		print(str(maxpos) + "=maxpos")
		if int(maxpos[0]) > 11 or int(maxpos[0]) < 0 or int(maxpos[1]) > 11 or int(maxpos[1]) < 0:
			modifyhistorique("Bateau hors de la grille", "warning")
			return
		
		
		
		for changingpos in range(0, int(boatsize)):
			x = str(int(placepos[0]) + int(changingpos*placeside[0]))
			y = str(int(placepos[1]) + int(changingpos*placeside[1]))
			postoplace.append(str(x) + " " + str(y))
			
		
		
		
		for pos in postoplace:
			if pos in posplaced:
				modifyhistorique("Case déja utilisée !", "warning")
				return
		
		# Here boats can be placed
		
		
		
		
		boats[boatname] = list()
		
		
		for pos in postoplace:
			x = pos[0:pos.index(" ")]
			y = pos[pos.index(" "):]
			bateauquiflotte = grilledefense.grid_slaves(row=int(x), column=(y))[0].create_rectangle(4,4,32,32, fill="blue")
			infodubateauquiflotte = grilledefense.grid_slaves(row=int(x), column=(y))[0].create_text(18,18, text=str(postoplace.index(pos)) + str(boatname[0]) + str(placeside[0]))
			grilledefense.grid_slaves(row=int(x), column=int(y))[0].unbind("<Key>")
			boats[boatname].append(pos)
			posplaced.append(pos)
			
		boatslefts.remove(boatname)
		selectedboatwidget.config(bg="light green")
		print(boats)
		
		
		
		
		if boatslefts == []:
			grilleattaque.grid(row=1, column=2, padx=30, pady=5) # ici tous les bateaux sont placés
			paquetsender("gready") # on dit à l'autre joueur qu'on est prêt
		


def boatsetter(event):
	global boatsize, boatname, selectedboatwidget
	selectedboatwidget = event.widget
	selectedboatwidget.focus_set()
	selectedboat = event.widget.itemcget(objet, "text")
	boatsize = selectedboat[selectedboat.index("(")+1]
	
	boatname = selectedboat[0:selectedboat.index(" ")]
	
	print(boatsize, boatname)

def placesetter(event):
	global placepos, placeside
	placepos = event.widget.itemcget(pos, "text").split()
	placeside = event.keysym
	print(placeside)
	print(placepos)
	onboatclick()





def shootedpossetter(event):
	global shootedpos
#	global paused
	
#	if paused == True:
#		return
	
	
#	event.widget.unbind("<Button-1>")
	shootedpos = event.widget.itemcget(pos, "text")
	
	event.widget.focus_set()
	
	print(shootedpos)
	use(shootedpos)






def use(shootedpos):
#	global paused
	
#	if paused == True:
#		return
	
	
	
	
	
	global selectedbonus
	global selectedbonuswidget
	

	
	global key
	
	global bonuswidget
	
	global imagedict
	
	

	
	
#	print(bonus, "hbvdfjbkhf")
	
#	bonuswidget = bonus
	
	
	
	
	
	
	
	
	
	
	x = shootedpos[0:shootedpos.index(" ")]
	y = shootedpos[shootedpos.index(" "):]	
	
	
	
	
	
	if selectedbonus != "":
		if bonusdict[selectedbonus] == 0:
			selectedbonus = ""
			return
	
	
	
	
	
		# ici, on a shootedpos et selectedbonus
	
	
	""" 1) """
	
	paquetsender("g" + str([None if selectedbonus == "" else selectedbonus][0]) + "," + shootedpos)
	
	
	
	
	
	
	
	
	
	
	
	
	
	

	
	#
	# [pos for key in boats for pos in boats[key]] => liste des position de toutes les cases de tous les bateaux
	#
	# ^ pas besoin (en fait si)
	#
	#
	#
	# [key for key in boats if shootedpos in boats[key]] => liste du bateau touché par shootedpos (attention: peut être vide)
	#
	# ^ = bateautouché (self-explainatory)
	#
	#
	#
	# [str(x) + " " + str(y) for x in range(int(shootedpos[0:shootedpos.index(" ")])-1, int(shootedpos[0:shootedpos.index(" ")])+2) for y in range(int(shootedpos[shootedpos.index(" "):])-1,int(shootedpos[shootedpos.index(" "):])+2) if str(x) + " " + str(y) in [str(x) + " " + str(y) for x in range(1,11) for y in range(1,11)]]
	#
	# ^ = bombardés (cases touchées par bombe dans la grille)
	#
	# 
	# set([str(x) + " " + str(y) for x in range(int(shootedpos[0:shootedpos.index(" ")])-1, int(shootedpos[0:shootedpos.index(" ")])+2) for y in range(int(shootedpos[shootedpos.index(" "):])-1,int(shootedpos[shootedpos.index(" "):])+2) if str(x) + " " + str(y) in [str(x) + " " + str(y) for x in range(1,11) for y in range(1,11)]]).intersection([pos for key in boats for pos in boats[key]])
	# 
	# ^ = explosés (bateaux touchés par la bombe)
	#
	#
	# [str(shootedpos[0:shootedpos.index(" ")]) + str(shootedpos[shootedpos.index(" "):]), str(int(shootedpos[0:shootedpos.index(" ")]) + direction[0]) + " " + str(int(shootedpos[shootedpos.index(" "):]) + direction[1])]
	#
	# ^ = survolés (positions survolées par l'avion)
	#
	# [item for item in [str(x) + " " + str(y) for x in range(int(shootedpos[0:shootedpos.index(" ")])-1, int(shootedpos[0:shootedpos.index(" ")])+2) for y in range(int(shootedpos[shootedpos.index(" "):])-1,int(shootedpos[shootedpos.index(" "):])+2) if str(x) + " " + str(y) in [str(x) + " " + str(y) for x in range(1,11) for y in range(1,11)]] + [str(int(shootedpos[0:shootedpos.index(" ")])-2) + " " + str(int(shootedpos[shootedpos.index(" "):]))] + [str(int(shootedpos[0:shootedpos.index(" ")])+2) + " " + str(int(shootedpos[shootedpos.index(" "):]))] + [str(int(shootedpos[0:shootedpos.index(" ")])) + " " + str(int(shootedpos[shootedpos.index(" "):])-2)] + [str(int(shootedpos[0:shootedpos.index(" ")])) + " " + str(int(shootedpos[shootedpos.index(" "):])+2)] if item in [str(x) + " " + str(y) for x in range(1,11) for y in range(1,11)]]
	# 
	# ^ = scannés (positions dans le radar)
	#
	#
	#
	#
	#
	#
	#
	#
	#
	#
	

	
	
	
	
	
	bateautouché = [key for key in boats if shootedpos in boats[key]]
	
	
	if selectedbonus == "":
		if bateautouché != []:
			modifyhistorique("Bateau " + bateautouché[0] + " touché en " + str(shootedpos) + ".", "touché")
			boats[bateautouché[0]].remove(shootedpos)
#			flamme = grilledefense.grid_slaves(row=int(x), column=int(y))[0].create_oval(8,8,28,28, fill="red")
			flamme = grilledefense.grid_slaves(row=int(x), column=int(y))[0].create_image(18,18, image=imagedict["Fire"])
#			grilledefense.grid_slaves(row=int(x), column=int(y))[0].flamme = imagedict["Fire"]
			grilleattaque.grid_slaves(row=int(x), column=(y))[0].config(bg="red")
			
			
			
			
			
			
			if boats[bateautouché[0]] == []:
				modifyhistorique("Bateau " + bateautouché[0] + " coulé !", "alert")
				boats.pop(bateautouché[0])
		else:
			modifyhistorique("Dans l'eau.", "info")
			grilleattaque.grid_slaves(row=int(x), column=(y))[0].config(bg="lightblue")
	
	
	
	
	
	
	
	if selectedbonus == bonuslist[0]:
		
		
		
		
		grilleattaque.grid_slaves(row=int(x), column=int(y))[0].grab_set()
		grilleattaque.grid_slaves(row=int(x), column=int(y))[0].bind("<Key>", lambda event: key.set(event.keysym))
		
	#	paused = True
		
		grilleattaque.grid_slaves(row=int(x), column=int(y))[0].wait_variable(key)
		
		
		
		grilleattaque.grid_slaves(row=int(x), column=int(y))[0].grab_release()
		
		
		if key.get() not in ["Left", "Up", "Down", "Right"]:
			selectedbonus = ""
			return
	#	paused = False
		
		direction = ""
		
		
		
		
		if key.get() == "Left":
			direction = [0, -1]
		if key.get() == "Right":
			direction = [0, 1]
		if key.get() == "Up":
			direction = [-1, 0]
		if key.get() == "Down":
			direction = [1, 0]
			
			
			
		print(direction)
		survolés = [str(shootedpos[0:shootedpos.index(" ")]) + str(shootedpos[shootedpos.index(" "):]), str(int(shootedpos[0:shootedpos.index(" ")]) + direction[0]) + " " + str(int(shootedpos[shootedpos.index(" "):]) + direction[1])]
		
		
		if [pos for pos in survolés if pos in [pos for key in boats for pos in boats[key]]] == []:
			modifyhistorique("Rien en vue.", "info")
			
			
		for pos in survolés:
			
			
			
			if pos in [str(x) + " " + str(y) for x in range(1,11) for y in range(1,11)]:
				bateautouché = [key for key in boats if pos in boats[key]]
				
			x = pos[0:pos.index(" ")]
			y = pos[pos.index(" "):]
			
			if bateautouché != []:
					modifyhistorique("Bateau " + [key for key in boats if pos in boats[key]][0] + " repéré et torpillé en " + str(pos) + ".", "touché")
					boats[bateautouché].remove(pos)
					flamme = grilledefense.grid_slaves(row=int(x), column=int(y))[0].create_image(18,18, image=imagedict["Fire"])
					grilleattaque.grid_slaves(row=int(x), column=(y))[0].config(bg="red")
					
					if boats[bateautouché[0]] == []:
						modifyhistorique("Bateau " + bateautouché[0] + " coulé !", "alert")
						boats.pop(bateautouché[0])
				
			else:
				grilleattaque.grid_slaves(row=int(x), column=(y))[0].config(bg="light blue")
				
	
	if selectedbonus == bonuslist[1]:
		scannés = [item for item in [str(x) + " " + str(y) for x in range(int(shootedpos[0:shootedpos.index(" ")])-1, int(shootedpos[0:shootedpos.index(" ")])+2) for y in range(int(shootedpos[shootedpos.index(" "):])-1,int(shootedpos[shootedpos.index(" "):])+2) if str(x) + " " + str(y) in [str(x) + " " + str(y) for x in range(1,11) for y in range(1,11)]] + [str(int(shootedpos[0:shootedpos.index(" ")])-2) + " " + str(int(shootedpos[shootedpos.index(" "):]))] + [str(int(shootedpos[0:shootedpos.index(" ")])+2) + " " + str(int(shootedpos[shootedpos.index(" "):]))] + [str(int(shootedpos[0:shootedpos.index(" ")])) + " " + str(int(shootedpos[shootedpos.index(" "):])-2)] + [str(int(shootedpos[0:shootedpos.index(" ")])) + " " + str(int(shootedpos[shootedpos.index(" "):])+2)] if item in [str(x) + " " + str(y) for x in range(1,11) for y in range(1,11)]]
		for pos in scannés:
			bateaurepéré = [key for key in boats if pos in boats[key]]
	
			x = pos[0:pos.index(" ")]
			y = pos[pos.index(" "):]
			
			if bateaurepéré != []:
				modifyhistorique("Signal reçu en " + str(x) + " " + str(y) + ".", "info")
				grilleattaque.grid_slaves(row=int(x), column=(y))[0].config(bg="light green")
			
			else:
				grilleattaque.grid_slaves(row=int(x), column=(y))[0].config(bg="light blue")
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	if selectedbonus == bonuslist[2]:
		bombardés = [str(x) + " " + str(y) for x in range(int(shootedpos[0:shootedpos.index(" ")])-1, int(shootedpos[0:shootedpos.index(" ")])+2) for y in range(int(shootedpos[shootedpos.index(" "):])-1,int(shootedpos[shootedpos.index(" "):])+2) if str(x) + " " + str(y) in [str(x) + " " + str(y) for x in range(1,11) for y in range(1,11)]]
		explosés = set([str(x) + " " + str(y) for x in range(int(shootedpos[0:shootedpos.index(" ")])-1, int(shootedpos[0:shootedpos.index(" ")])+2) for y in range(int(shootedpos[shootedpos.index(" "):])-1,int(shootedpos[shootedpos.index(" "):])+2) if str(x) + " " + str(y) in [str(x) + " " + str(y) for x in range(1,11) for y in range(1,11)]]).intersection([pos for key in boats for pos in boats[key]])
		
		if explosés != set():
			modifyhistorique("La bombe a explosé.", "touché")
			for pos in bombardés:
				x = pos[0:pos.index(" ")]
				y = pos[pos.index(" "):]
				grilleattaque.grid_slaves(row=int(x), column=(y))[0].config(bg="hot pink")
				
		else:
			modifyhistorique("La bombe a coulé.", "info")
			for pos in bombardés:
				x = pos[0:pos.index(" ")]
				y = pos[pos.index(" "):]
				grilleattaque.grid_slaves(row=int(x), column=(y))[0].config(bg="lightblue")
			
		for pos in bombardés:
			x = pos[0:pos.index(" ")]
			y = pos[pos.index(" "):]
			bateautouché = [key for key in boats if pos in boats[key]]
			if bateautouché != []:
		#		modifyhistorique("Bateau " + [key for key in boats if pos in boats[key]][0] + " explosé en " + str(pos) + ".")
				boats[bateautouché[0]].remove(pos)
				flamme = grilledefense.grid_slaves(row=int(x), column=int(y))[0].create_image(18,18, image=imagedict["Fire"])
		#		grilleattaque.grid_slaves(row=int(x), column=(y))[0].config(bg="red")

				if boats[bateautouché[0]] == []:
					modifyhistorique("Bateau " + bateautouché[0] + " coulé !", "alert")
					boats.pop(bateautouché[0])
	
	
	
	if selectedbonus == bonuslist[3]:
		if bateautouché != []:
			modifyhistorique("Bateau " + bateautouché[0] + " touché-coulé !", "alert")
			grilleattaque.grid_slaves(row=int(x), column=(y))[0].config(bg="darkred")
			for pos in boats[[key for key in boats if shootedpos in boats[key]][0]]:
				x = pos[0:pos.index(" ")]
				y = pos[pos.index(" "):]
				flamme = grilledefense.grid_slaves(row=int(x), column=int(y))[0].create_image(18,18, image=imagedict["Fire"])
				
			boats.pop(bateautouché[0])
			
		else:
			modifyhistorique("Dans l'eau", "info")
			grilleattaque.grid_slaves(row=int(x), column=(y))[0].config(bg="lightblue")
	
	
	
	
	
	
	
	
	
	
	
	
	for bonus in bonusdict:
		if bonus == selectedbonus:
			bonusdict[selectedbonus] = bonusdict[selectedbonus] - 1
	print(bonusdict)
	
	
	
	if boats == {}:
		modifyhistorique("Perdu, tous vos bateaux sont coulés !", "alert")
	
	
	
	
	
	
	
	
	
	
	

	
	
	print(selectedbonus, "THIS IS SELECTED BONUS")
	
	print(bonusdict)
	"""
	if selectedbonus != "":
		for canvas in bonuswidget.grid_slaves():
			print("is", selectedbonus, "in", str(canvas.itemcget(objet, "text")), "?", str(selectedbonus) in str(canvas.itemcget(objet, "text")))
			if str(selectedbonus) in str(canvas.itemcget(objet, "text")):
				print(canvas.itemcget(objet, "text"), "objet text")
				canvas.itemconfig(objet, text=str(selectedbonus) + " (" + str(bonusdict[selectedbonus]) + " restants)")
				print("a changer en ", str(selectedbonus) + " (" + str(bonusdict[selectedbonus]) + " restants)")
				selectedbonus = ""
				return
		
	"""

	if selectedbonus != "":
		selectedbonuswidget.itemconfig(objet, text=str(selectedbonus) + " (" + str(bonusdict[selectedbonus]) + " restants)")
		selectedbonus = ""
		return
	
	selectedbonus = ""
	
	
	
	
	
	
	
	'''
	
	if selectedbonus == "":
		for key in boats:
			if shootedpos in boats[key]:
				modifyhistorique("Bateau " + str(key) + " touché en " + str(shootedpos) + ".")
				flamme = grilledefense.grid_slaves(row=int(x), column=(y))[0].create_oval(8,8,28,28, fill="red")
				grilleattaque.grid_slaves(row=int(x), column=(y))[0].config(bg="red")
				
				
				
				
				
				boats[key].remove(shootedpos)
				
				if boats[key] == []:
					boats.pop(key)
					modifyhistorique("Bateau " + str(key) + " coulé !")
					break
					
		if shootedpos not in posplaced:
				modifyhistorique("Dans l'eau")
				grilleattaque.grid_slaves(row=int(x), column=(y))[0].config(bg="lightblue")
		
		
		
		
		
		
		
	if selectedbonus == bonuslist[3]:
		for key in boats:
			if shootedpos in boats[key]:
				modifyhistorique("Bateau " + str(key) + " touché-coulé !")
				grilleattaque.grid_slaves(row=int(x), column=(y))[0].config(bg="red")
				for pos in boats[key]:
					x = pos[0:pos.index(" ")]
					y = pos[pos.index(" "):]
					flamme = grilledefense.grid_slaves(row=int(x), column=(y))[0].create_oval(8,8,28,28, fill="red")
					
				boats.pop(key)
				break
				
			if shootedpos not in posplaced:
				modifyhistorique("Dans l'eau")
				grilleattaque.grid_slaves(row=int(x), column=(y))[0].config(bg="lightblue")
		
		
	if boats == {}:
		modifyhistorique("Perdu, tous vos bateaux sont coulés !")
	
	
	selectedbonus = ""
		
		
'''










def sendmessage(event):
	if event.widget.get() != "":
		messageaenvoyer = event.widget.get()
		event.widget.delete(0, "end")
		modifyhistorique(" >> " + messageaenvoyer, "chat")
		
		paquetsender("c" + messageaenvoyer)







def modifyhistorique(string, tag=None):
			# définition des tags
		
	historique.tag_config("alert", background="red")
	historique.tag_config("warning", foreground="orange")
	historique.tag_config("info", foreground="blue")
	historique.tag_config("chat", foreground="green")
	historique.tag_config("touché", foreground="purple")
		
		
	if string != "":	
		historique.config(state="normal")
		historique.insert("end", string + "\n", (tag))
		historique.see("end")
		historique.config(state="disabled")






def bonussetter(event):
	global selectedbonus
	
	global selectedbonuswidget
	
	selectedbonuswidget = event.widget
	selectedbonuswidget.focus_set()
	selectedbonus = event.widget.itemcget(objet, "text")
	selectedbonus = selectedbonus[0:selectedbonus.index("(")-1]
	print(selectedbonus)
	print(bonus)
	
















'''

bonuslist = ["Avion", "Radar", "Bombe", "Missile perforant"]

bateauxlist = ["Porte-avion (5 cases)", "Croiseur (4 cases)", "Contre-torpilleur (3 cases)", "Sous-marin (3 cases)", "Torpilleur (2 cases)"]

boatslefts = [boatname[0:boatname.index(" ")] for boatname in [boat for boat in bateauxlist]]


for x in range(0, len(bateauxlist)):
	boatslefts.append(bateauxlist[x][0:bateauxlist[x].index(" ")])
	print(boatslefts)
'''








fenetre.title("Bataille-navale")

bonus = tk.Canvas(fenetre, height = 300, width = 200, bg = "white")

for x in range(0, len(bonuslist)+1):
	case = tk.Canvas(bonus, bg="white", height=50, width=200)
	image = case.create_image(100,20)
	if x == 0:
		text = case.create_text(100,25, text="Bonus :", fill="red", font=("Purisa", 20))
		case.config(bg="pink")
	elif x > 0:
		objet = case.create_text(100,25, text=str(bonuslist[x-1]) + " (" + str(bonusdict[bonuslist[x-1]]) + " restants)", tags=str(bonuslist[x-1]))
		case.bind("<Button-1>", bonussetter)
	#   case.bind("<Button-3>", onrightclick)
		print(case.gettags(bonuslist[x-1]))
		print(bonuslist[x-1])
	
	
	"""
	TEMPORARY DISPLAY
	"""
	
	
		
	case.grid(row=x)
	print(fenetre.nametowidget(bonus))
	print(bonus.find_withtag("Avion",))
	
	"""
	END OF TEMPORARY DISPLAY
	"""
	

bonus.grid(row=1, column=1, padx=10)

"""
"""
bonuswidget = bonus
"""
"""









bateaux = tk.Canvas(fenetre, height = 300, width = 200, bg = "white")

for x in range(0, len(bateauxlist)+1):
	case = tk.Canvas(bateaux, bg="white", height=50, width=200)
	image = case.create_image(100,20)
	if x == 0:
		text = case.create_text(100,25, text="Bateaux :", fill="dark blue", font=("Purisa", 20))
		case.config(bg="azure2")
	elif x > 0:
		objet = case.create_text(100,25, text=str(bateauxlist[x-1]), state="")
		case.bind("<Button-1>", boatsetter)
	#	case.bind("<Button-3>", onrightclick)
	case.grid(row=x)

bateaux.grid(row=2, column=1, padx=10)



grilleattaque = tk.Canvas(fenetre, bg = "white")

for x in range(1, 10+1):
	for y in range(1, 10+1):
	
		case = tk.Canvas(grilleattaque, bg="white", height=36, width=36)
	#	image = case.create_image(18,18)
		pos = case.create_text(18,18, text=str(x) + " " + str(y), state="hidden")
		case.bind("<Button-1>", shootedpossetter)
   #     case.bind("<Button-3>", onrightclick)
		case.grid(row=x, column=y)




# grilleattaque.grid(row=1, column=2, padx=30, pady=5) # on attend que tous les bateaux soient placés pour l'afficher








grilledefense = tk.Canvas(fenetre, bg = "white")

for x in range(1, 10+1):
	for y in range(1, 10+1):
	
		case = tk.Canvas(grilledefense, bg="white", height=36, width=36)
	#	image = case.create_image(18,18)
		pos = case.create_text(18,18, text=str(x) + " " + str(y), state="hidden")
		case.bind("<Button-1>", lambda event: event.widget.focus_set())
		case.bind("<Key>", placesetter)
   #     case.bind("<Button-3>", onrightclick)
		case.grid(row=x, column=y)
grilledefense.grid(row=2, column=2, padx=30, pady=5)





historique = tk.Text(fenetre, bg="white", height=40, width=40)

historique.config(state="disabled")

historique.grid(column=3, row=1, rowspan=2, sticky="NS", pady=10, padx=10)



chat = tk.Entry(fenetre, width=35)


chat.bind("<Return>", sendmessage)
chat.grid(column=3, row=2, sticky="S", pady=10, padx=10)




"""
Partie affichage du profil en cours
"""



profiledisplayer = tk.Canvas(fenetre, bg = "light green", height=200, width=300)

usernamedisplayer = profiledisplayer.create_text(150,20, text=profiledict["username"], font=("Ubuntu", 20), fill="dark green")

profileimage = tk.PhotoImage(data=profiledict["image"])


print(profileimage)


profileimagedisplayer = profiledisplayer.create_image(150,100, image=profileimage)


profiledisplayer.grid(column=4, row=1, rowspan=2, padx=10, sticky="N")







# faire la même chose pour le profil ennemi

















"""
Fin partie affichage du profil
"""


"""
temporaire : afficheur de paquet
"""




paquetdisplayer = tk.Text(fenetre, bg="grey", height=40, width=40)

paquetdisplayer.tag_config("received", foreground="red")
paquetdisplayer.tag_config("sended", foreground="green")



paquetdisplayer.grid(column=5, row=1, rowspan=2, sticky="NS", pady=10, padx=10)















"""
fin : temporaire : afficheur de paquet
"""



fenetre.mainloop()
