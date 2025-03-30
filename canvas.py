import tkinter as tk
from PIL import Image, ImageTk

def cancella():
    txt1.delete( 1.0, tk.END)

def calcola():
    print("ciao")
    somma = 0
    n_voti =0
    voti = txt1.get(1.0, tk.END)
    lista_voti = voti.split()
    print(lista_voti)
    
    unita = listbox1.get(listbox1.curselection())
    if unita == "Voto Max":
        risultato = max(lista_voti)
        risultato = "Il voto max risulta " + str(risultato)
    elif unita == "Voto Min":
        risultato = min(lista_voti)
        risultato = "Il voto minimo risulta " +str(risultato)
    elif unita == "Media":
        for numero in lista_voti:
            somma += int(numero)
            n_voti += 1
        risultato = "La media risulta " + str(round(somma/n_voti,2))
    else:
        risultato = valore    
    
    lbl2.config(text=risultato)


schermo = tk.Tk()
schermo.title("Esempio Canvas")

# Carica l'icona
try:
    icona = tk.PhotoImage(file="python.png")
    schermo.iconphoto(True, icona)
except tk.TclError:
    print("Icona non trovata.")
    
lbl1 = tk.Label(schermo,text ="Inserisci i voti dell'alunno",  font=("Cambria",15))
lbl1.grid(row=0,column=0, sticky = "nw") 

lbl2 = tk.Label(schermo,text ="Risultato",  font=("Cambria",15))
lbl2.grid(row=4,column=0, sticky = "nw") 


    #crea Text box
txt1 = tk.Text(schermo,width=20, height= 5, font=("Cambria",15))
txt1.grid(row=1,column=0, sticky = "nw")

listbox1 = tk.Listbox(schermo,height = 4, font =("Arial", 14))
listbox1.grid(row=2,column=0, sticky="w")
listbox1.insert(1,"Voto Max")
listbox1.insert(2,"Voto Min")
listbox1.insert(3,"Media")

btn1 = tk.Button(schermo,text = "Calcola", command = calcola,  font =("Cambria", 14)) #command = calcola
btn1.grid(row=3, column=0, sticky = "nw")

btn2 = tk.Button(schermo,text = "Cancella", command = cancella,  font =("Cambria", 14)) #command = calcola
btn2.grid(row=3, column=0)
# Crea una Canvas
canvas = tk.Canvas(schermo, width=400, height=300,bg ="yellow")
canvas.grid(row=5,column=0, sticky = "nw") 

# Disegna un rettangolo
canvas.create_rectangle(10, 10, 100, 50, fill="lightblue")

# Disegna un cerchio
canvas.create_oval(250, 50, 350, 150, fill="lightgreen")

# Aggiungi del testo
canvas.create_text(100, 80, text="Ciao dalla Canvas!", font=("Arial", 14))

# Carica un'immagine
try:
    immagine_pil = Image.open("scoiattolo.jpg")
    immagine = ImageTk.PhotoImage(immagine_pil)
    canvas.create_image(100, 200, image=immagine)
except FileNotFoundError:
    print("Immagine non trovata.")

