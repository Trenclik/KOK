<<<<<<< Updated upstream:kok.py
import tkinter as tk
from tkinter import ttk
from ttkthemes import ThemedStyle
import random
import os

okno = tk.Tk() #vytvoří kokno ig
=======
import tkinter
import random
import os

okno = tkinter.Tk() #vytvoří kokno ig
>>>>>>> Stashed changes:kok_v1.1.py
okno.attributes('-fullscreen',True)
okno.title("kok mole nečum")
style = ThemedStyle(okno)
style.set_theme("equilux")

def get_files_in_folder(folder_path):   #zapíše do listu soubory
    files_list = []
    for filename in os.listdir(folder_path):
        full_path = os.path.join(folder_path, filename)
        if os.path.isfile(full_path):
            files_list.append(full_path)
    return files_list

# Cesta ke složce, ze které chcete načíst soubory
folder_path = "upraveny_josi/"             
# Získání souborů ze složky a uložení do listu
files_list = get_files_in_folder(folder_path)

# Výpis seznamu souborů pro kontrolu
# print(files_list)      bruh nedá se to číst



ikonka = tk.PhotoImage(file="11.png")
okno.iconphoto(True,ikonka)
okno.config(background="black")
majtin = random.choice(files_list)
fotka = tk.PhotoImage(file=str(majtin))
pamet = [majtin]


def klik():   #po kliknutí se změní fotka
    majtin = random.choice(files_list)
    kok = True
    while kok:
        if majtin == pamet[0]:
            majtin = random.choice(files_list)
            pass
        else:
            kok = False
    pamet.clear
    global fotka
    fotka = tk.PhotoImage(file=str(majtin))
    pamet[0] = majtin
    label.config(image = fotka)

<<<<<<< Updated upstream:kok.py
klikblb = ttk.Button(okno,
=======
tkinter.klikblb = Button(okno,
>>>>>>> Stashed changes:kok_v1.1.py
                 text="kok, klikni",
                 command=klik)
tkinter.klikblb.pack()

<<<<<<< Updated upstream:kok.py
klikblb = ttk.Button(okno,
=======
tkinter.klikblb = Button(okno,
>>>>>>> Stashed changes:kok_v1.1.py
                 text="exit",
                 command=exit)
tkinter.klikblb.pack()
def exit(event):
    okno.quit()

slovo = "kok"
label = ttk.Label(okno, 
              text=slovo,
              image = fotka,
              compound="bottom")
label.pack()

#label.place(x=0,y=0)

okno.mainloop() #zařídí že se ti to spustí