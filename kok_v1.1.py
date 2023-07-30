from tkinter import *
import random
import os

okno = Tk() #vytvoří kokno ig
okno.attributes('-fullscreen',True)
okno.title("kok mole nečum")


def get_files_in_folder(folder_path):   #zapíše do listu soubory
    files_list = []
    for filename in os.listdir(folder_path):
        full_path = os.path.join(folder_path, filename)
        if os.path.isfile(full_path):
            files_list.append(full_path)
    return files_list

# Cesta ke složce, ze které chcete načíst soubory
folder_path = "Jozi fotky/"

# Získání souborů ze složky a uložení do listu
files_list = get_files_in_folder(folder_path)

# Výpis seznamu souborů pro kontrolu
print(files_list)



ikonka = PhotoImage(file="Jozi fotky/11.png")
okno.iconphoto(True,ikonka)
okno.config(background="blue")
majtin = random.choice(files_list)
fotka = PhotoImage(file=str(majtin))
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
    fotka = PhotoImage(file=str(majtin))
    pamet[0] = majtin
    label.config(image = fotka)

klikblb = Button(okno,
                 text="kok, klikni",
                 command=klik)
klikblb.pack()

klikblb = Button(okno,
                 text="exit",
                 command=exit)
klikblb.pack()
def exit(event):
    okno.quit()

slovo = "kok"
label = Label(okno, 
              text=slovo, 
              font=("Arial",40,"bold"), 
              fg="green", 
              bg="black",
              relief="raised",
              bd=10,
              padx=10,
              pady=10,
              image = fotka,
              compound="bottom")
label.pack()

#label.place(x=0,y=0)

okno.mainloop() #zařídí že se ti to spustí