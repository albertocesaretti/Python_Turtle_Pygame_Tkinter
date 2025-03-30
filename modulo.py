import tkinter as tk
from PIL import Image, ImageTk

def esempio_canvas():
    finestra = tk.Tk()
    finestra.title("Esempio Canvas")

    # Carica l'icona
    try:
        icona = tk.PhotoImage(file="icona.png")
        finestra.iconphoto(True, icona)
    except tk.TclError:
        print("Icona non trovata.")

    # Crea una Canvas
    canvas = tk.Canvas(finestra, width=400, height=300)
    canvas.pack()

    # Disegna un rettangolo
    canvas.create_rectangle(50, 50, 200, 150, fill="lightblue")

    # Disegna un cerchio
    canvas.create_oval(250, 50, 350, 150, fill="lightgreen")

    # Aggiungi del testo
    canvas.create_text(200, 250, text="Ciao dalla Canvas!", font=("Arial", 14))

    # Carica un'immagine
    try:
        immagine_pil = Image.open("scoiattolo.jpg")
        immagine = ImageTk.PhotoImage(immagine_pil)
        canvas.create_image(100, 250, image=immagine)
    except FileNotFoundError:
        print("Immagine non trovata.")

    finestra.mainloop()

if __name__ == "__main__":
    print(tk)
    esempio_canvas()
    