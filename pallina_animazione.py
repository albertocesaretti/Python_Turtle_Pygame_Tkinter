import turtle
import time
import random as r

#classe pallina che deriva dalla classe padre Turtle
class Pallina(turtle.Turtle):
    def __init__(self, x, y, dx, dy, colore, shape):
        super().__init__()
        self.x = x
        self.y = y
        self.up() #alzo la penna dal foglio
        self.colore = colore
        self.shape(shape) #associo una forma alla penna
        self.goto(x,y)
        self.color(colore)
        self.dx = dx #velocita x
        self.dy = dy #velocita y
               
    def muovi(self):
      self.setx(self.xcor() + self.dx)
      self.sety(self.ycor() + self.dy)
    
    def controlloCollisioneBordi(self):
      # Controllo dei bordi
      if self.xcor() > 290:
        self.dx *= -1  # Inverti la direzione orizzontale
        print("*****Tocca il bordo superiore dx *****")
        print(self.xcor())
        print(self.dx)
         #correzione = r.randint(-20, -1)
         #print(correzione)
      if self.xcor() < -290:     
        self.dx *= -1  # Inverti la direzione orizzontale
        print("*****Tocca il bordo inferiore SX *****")
        print(self.xcor())
        print(self.dx)
        #correzione = r.randint(1,20)
        #print(correzione)
      if self.ycor() > 290:
         self.dy *= -1  # Inverti la direzione verticale 
      if self.ycor() < -290:
        self.dy *= -1  # Inverti la direzione verticale 

# Imposta lo schermo
schermo = turtle.Screen()
schermo.bgcolor("white")
schermo.setup(width=600, height=600)
schermo.tracer(0)  # Disabilita l'aggiornamento automatico dello schermo

# Creo la pallina 1 e 2
pallina1 = Pallina( 0, 0, 3, 3, "red", "circle")
pallina2 = Pallina( -100, 100, -2, -3, "blue", "circle")
# Ciclo principale del gioco
while True:
  schermo.update()  # Aggiorna lo schermo
  pallina1.muovi()
  pallina1.controlloCollisioneBordi()
  pallina2.muovi()
  pallina2.controlloCollisioneBordi()
  time.sleep(0.01)  # Pausa per controllare la velocità dell'animazione
  