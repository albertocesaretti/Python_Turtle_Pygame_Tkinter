import turtle

# Funzione per spostare la tartaruga in avanti
def avanti():
    tartaruga.forward(50)

# Funzione per spostare la tartaruga indietro
def indietro():
    tartaruga.backward(50)

# Funzione per ruotare la tartaruga a sinistra
def sinistra():
    tartaruga.left(45)

# Funzione per ruotare la tartaruga a destra
def destra():
    tartaruga.right(45)

# Crea una finestra e una tartaruga
finestra = turtle.Screen()
tartaruga = turtle.Turtle()

# Associa le funzioni ai tasti
finestra.onkey(avanti, "w")
finestra.onkey(indietro, "s")
finestra.onkey(sinistra, "a")
finestra.onkey(destra, "d")

# Inizia l'ascolto degli eventi
finestra.listen()

# Mantiene la finestra aperta
finestra.mainloop()