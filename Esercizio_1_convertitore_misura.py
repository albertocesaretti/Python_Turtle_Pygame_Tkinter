import tkinter as tk

def calcola():
    try:
        valore = float(entry1.get())
        unita = listBox1.get(listBox1.curselection())

        if unita == "Pollici":
            print("ciao mamma")
            risultato = round(valore *2.54 ,2)#conversione 1 pollice = 2,54 cmm
            risultato =  str(risultato) + " : cm"
        elif unita == "Piedi":
            risultato = round(valore / 3.28084, 2)
            risultato =  str(risultato) + " : m"
        elif unita == "Miglio":
            risultato = valore * 1.6
            risultato =  str(risultato) + " : km"
        else:
            risultato = valore  # Se le unità sono le stesse

        lbl2.config(text=risultato)
    except ValueError:
        lbl2.config(text="Inserisci un numero valido")

schermo = tk.Tk() #creo lo schemo
schermo.title("Convertitore misure anglosassoni")
schermo.geometry("400x200")
schermo.configure(background='yellow')
schermo.resizable(width=True, height=True)

lbl1 = tk.Label(schermo, text = "Valore da convertire")
lbl1.grid(row=0, column=0,sticky="w")

print(lbl1.config().keys()) #le parole chiave per configurare una label

entry1 = tk.Entry(schermo) #valore da convertire
entry1.grid(row = 1, column = 0,sticky="nw")

listBox1 = tk.Listbox(schermo, height=4)
listBox1.insert(1, "Pollici")
listBox1.insert(2, "Piedi")
listBox1.insert(3, "Miglio")
listBox1.grid(row = 1, column = 1,sticky="se")

btn = tk.Button(schermo, text = "Converti", command = calcola)
btn.grid(row=2, column=0,sticky="w")

lbl2 = tk.Label(schermo, text = "risultato", bg="white")
lbl2.grid(row=3, column=0,sticky="w")

schermo.mainloop() #creo un ciclo