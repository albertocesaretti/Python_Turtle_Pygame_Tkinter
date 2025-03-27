import turtle
import time

class Sprite(turtle.Turtle):
    def __init__(self, shape):
        super().__init__()
        self.shape(shape)
        self.penup()
        
     # Funzione per spostare la tartaruga in avanti
    def avanti(self):
        self.setx(self.xcor() + 40)
   
    # Funzione per spostare la tartaruga indietro
    def indietro(self):
        self.setx(self.xcor() - 40)

    # Funzione per muovere la tartaruga in alto
    def alto(self):
        self.sety(self.ycor() + 40)

    # Funzione per muovere la tartaruga in alto
    def basso(self):
        self.sety(self.ycor() - 40)
        
    def saluta(self):
        print("ciao sono pikachu")

    def esci(self):
        global run
        run = False
        print(run)
        print("Termina programma")

# Imposta lo schermo
schermo = turtle.Screen()
schermo.bgcolor("white")
schermo.addshape("pikachu.gif")
schermo.setup(width=600, height=600)
schermo.tracer(0)  # Disabilita l'aggiornamento automatico dello schermo

sprite1 = Sprite("pikachu.gif")

# Associa le funzioni ai tasti
schermo.onkey(sprite1.avanti, "d")
schermo.onkey(sprite1.indietro, "a")
schermo.onkey(sprite1.alto, "w")
schermo.onkey(sprite1.basso, "z")
schermo.onkey(sprite1.esci, "e")
# Inizia l'ascolto degli eventi
schermo.listen()        
        
# Ciclo principale del gioco
run = True
while run:
  schermo.update()  # Aggiorna lo schermo
  time.sleep(0.01)  # Pausa per controllare la velocità dell'animazione
  
schermo.bye() 