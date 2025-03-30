import tkinter as tk

def converti():
    try:
        valore = float(entry_valore.get())
        da_unita = lista_da.get(lista_da.curselection())
        a_unita = lista_a.get(lista_a.curselection())

        if da_unita == "Metri" and a_unita == "Piedi":
            risultato = valore * 3.28084
        elif da_unita == "Piedi" and a_unita == "Metri":
            risultato = valore / 3.28084
        else:
            risultato = valore  # Se le unità sono le stesse

        label_risultato.config(text=f"Risultato: {risultato:.2f} {a_unita}")
    except ValueError:
        label_risultato.config(text="Inserisci un numero valido")

# Creazione della finestra principale
finestra = tk.Tk()
finestra.title("Convertitore di Misure")

# Label e Entry per il valore da convertire
label_valore = tk.Label(finestra, text="Valore:")
label_valore.pack()
entry_valore = tk.Entry(finestra)
entry_valore.pack()

# Liste per le unità di misura
label_da = tk.Label(finestra, text="Da:")
label_da.pack()
lista_da = tk.Listbox(finestra, height=2)
lista_da.insert(1, "Metri")
lista_da.insert(2, "Piedi")
lista_da.pack()

label_a = tk.Label(finestra, text="A:")
label_a.pack()
lista_a = tk.Listbox(finestra, height=2)
lista_a.insert(1, "Metri")
lista_a.insert(2, "Piedi")
lista_a.pack()

# Bottone per convertire
bottone_converti = tk.Button(finestra, text="Converti", command=converti)
bottone_converti.pack()

# Label per il risultato
label_risultato = tk.Label(finestra, text="Risultato:")
label_risultato.pack()

finestra.mainloop()