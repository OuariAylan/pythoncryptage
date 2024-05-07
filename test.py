from tkinter import *

fenetre = tk()
fenetre.tittle("Logiciel de cryptage et de decryptage")
fenetre.iconbitmap("cryptage-des-donnees (3).ico")
fenetre.geometry(200, 300)
fenetre.maxsize(400, 500)

titre = Label(fenetre, text = "MON INTERFACE")
titre.pack()

champ = Entry(fenetre)



mainloop()
