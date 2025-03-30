import tkinter as tk

def calcola():
    op1 = str(entry1.get())
    op2 = str(entry2.get())
    if op1 and op2:
        somma = op1 + op2
    print("Hello World")
    lbl3.config(text = str(somma), bg = "pink", fg="red")

schermo = tk.Tk() #creo lo schemo
schermo.title("Esercizio 1")
schermo.geometry("400x200")
schermo.configure(background='yellow')
schermo.resizable(width=True, height=True)

lbl1 = tk.Label(schermo, text = "Operatore 1")
lbl1.grid(row=0, column=1)

lbl2 = tk.Label(schermo, text = "Operatore 2")
lbl2.grid(row=1, column=1)

lbl3 = tk.Label(schermo, text = "Risultato")
lbl3.grid(row=3, column=0)

print(lbl1.config().keys()) #le parole chiave per configurare una label

entry1 = tk.Entry(schermo)
entry1.grid(row = 0, column = 0)

entry2 = tk.Entry(schermo)
entry2.grid(row = 1, column = 0)

btn = tk.Button(schermo, text = "Somma", command = calcola)
btn.grid(row=2, column=0)

schermo.mainloop() #creo un ciclo