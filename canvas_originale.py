import tkinter as tk
from PIL import Image, ImageTk

def esempio_canvas():
    schermo = tk.Tk()
    schermo.title("Esempio Canvas")

    # Carica l'icona
    try:
        icona = tk.PhotoImage(file="python.png")
        schermo.iconphoto(True, icona)
    except tk.TclError:
        print("Icona non trovata.")

    # Crea una Canvas
    canvas = tk.Canvas(schermo, width=400, height=300, bg = "yellow")
    canvas.pack() #oggetti visualizzati uno di sotto l'altro

    # Disegna un rettangolo
    canvas.create_rectangle(30, 30, 200, 80, fill="lightblue")

    # Disegna un cerchio
    canvas.create_oval(250, 50, 350, 150, fill="lightgreen")

    # Aggiungi del testo
    canvas.create_text(300, 250, text="Ciao dalla Canvas!", font=("Arial", 14))

    # Carica un'immagine
    try:
        immagine_pil = Image.open("scoiattolo.jpg")
        immagine = ImageTk.PhotoImage(immagine_pil)
        canvas.create_image(90, 200, image=immagine)
    except FileNotFoundError:
        print("Immagine non trovata.")

    schermo.mainloop()

if __name__ == "__main__":
    print(tk)
    esempio_canvas()
  