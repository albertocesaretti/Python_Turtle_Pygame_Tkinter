import tkinter as tk

def calcola():
    valore = float(entry1.get())
    unita = listbox1.get(listbox1.curselection())
    if unita == "Pollici":
        risultato = valore*2.54 
        risultato = str(risultato)+ " : cm "
    elif unita == "Piedi":
        risultato = round(valore/ 3.28084, 2)
        risultato = str(risultato)+ " : m "
    elif unita == "Miglio":
        risultato = round(valore*1.6, 2)
        risultato = str(risultato)+ " : km "
    else:
        risultato = valore
        
    lbl2.config(text=risultato)

#main
schermo = tk.Tk()
schermo.title("Covertitore di misura anglosassoni")
schermo.geometry("600x400")
schermo.config(bg = "lightgray")
schermo.resizable(width=True, height=True)

lbl1 = tk.Label(schermo,text = "Valore da inserire", font =("Arial", 14))
lbl1.grid(row=0, column=0, sticky= "w")

print(lbl1.config().keys())

entry1 = tk.Entry(schermo,font =("Arial", 14))
entry1.grid(row=1, column=0, sticky= "nw")

listbox1 = tk.Listbox(schermo, height = 4, font =("Arial", 14))
listbox1.grid(row=1,column=1, sticky="e")
listbox1.insert(1,"Pollici")
listbox1.insert(2,"Piedi")
listbox1.insert(3,"Miglio")

btn1 = tk.Button(schermo, text = "Converti",font =("Arial", 14), command = calcola)
btn1.grid(row=2, column=0, sticky = "w")

lbl2 = tk.Label(schermo,text = "Risultato", bg ="white", fg = "red", font =("Arial", 14))
lbl2.grid(row=3, column=0, sticky= "w")


schermo.mainloop()