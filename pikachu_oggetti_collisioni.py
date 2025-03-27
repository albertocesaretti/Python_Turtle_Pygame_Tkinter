import turtle
import time

class Penna(turtle.Turtle):
    def __init__(self, x, y, colore, dimensione, carattere):
        super().__init__()
        self.x = x
        self.y = y
        self.colore = colore
        self.dimensione = dimensione
        self.carattere = carattere
        self.up() #alzo la penna dal foglio
        #self.scrivi("ciao mondo")
        
    def scrivi(self, testo):
        self.up()
        self.goto(self.x , self.y)
        print("ciao")
        self.down()
        self.write(testo, font = (self.carattere, self.dimensione, "normal"))
        self.up()
        #self.hideturtle()
        

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
        #print(self.xcor())
        #print(self.dx)
         #correzione = r.randint(-20, -1)
         #print(correzione)
      if self.xcor() < -290:     
        self.dx *= -1  # Inverti la direzione orizzontale
        #correzione = r.randint(1,20)
        #print(correzione)
      if self.ycor() > 290:
         self.dy *= -1  # Inverti la direzione verticale 
      if self.ycor() < -290:
        self.dy *= -1  # Inverti la direzione verticale 

class Sprite(turtle.Turtle):
    def __init__(self, x, y, dx, dy, shape):
        super().__init__()
        self.x = x
        self.y = y
        self.up() #alzo la penna dal foglio
        self.shape(shape) #associo una forma alla penna
        self.goto(x,y)
        self.dx = dx #spostamento in x
        self.dy = dy #spostamento in y
        
     # Funzione per spostare la tartaruga in avanti
    def avanti(self):
        self.setx(self.xcor() + self.dx)
   
    # Funzione per spostare la tartaruga indietro
    def indietro(self):
        self.setx(self.xcor() - self.dx)

    # Funzione per muovere la tartaruga in alto
    def alto(self):
        self.sety(self.ycor() + self.dy)

    # Funzione per muovere la tartaruga in alto
    def basso(self):
        self.sety(self.ycor() - self.dy)
        
    def controlloCollisione(self,pen):
        global aggiornaPunteggio
        if  pen.xcor() - 20 <=  self.xcor() <= pen.xcor() + 20 and\
            pen.ycor() - 20 <=  self.ycor() <= pen.ycor() + 20 :
                #self.hideturtle()
                self.goto(-270, 270)
                aggiornaPunteggio = True

    def mostra(self):
        self.showturtle()
        
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

sprite1 = Sprite(-270, 270, 40, 40, "pikachu.gif")

# Associa le funzioni ai tasti
schermo.onkey(sprite1.avanti, "d")
schermo.onkey(sprite1.indietro, "a")
schermo.onkey(sprite1.alto, "w")
schermo.onkey(sprite1.basso, "z")
schermo.onkey(sprite1.mostra, "s")
schermo.onkey(sprite1.esci, "e")
# Inizia l'ascolto degli eventi
schermo.listen()        

# Creo penna 1
penna1 = Penna(0, 250, "black", 16, "Arial")
# Creo la pallina 1 e 2
pallina1 = Pallina( 0, 0, 3, 3, "red", "circle")
pallina2 = Pallina( -100, 100, -2, -3, "blue", "circle")

# Ciclo principale del gioco
aggiornaPunteggio = False
aggiornaPunteggioOld = False

punteggio = 0
run = True
while run:
  schermo.update()  # Aggiorna lo schermo
  pallina1.muovi()
  pallina1.controlloCollisioneBordi()
  pallina2.muovi()
  pallina2.controlloCollisioneBordi()
  sprite1.controlloCollisione(pallina1)
  time.sleep(0.01)  # Pausa per controllare la velocità dell'animazione
  if aggiornaPunteggioOld == False and aggiornaPunteggio==True:
      punteggio += 1
      penna1.clear()
      penna1.scrivi(f"Punteggio : {punteggio} ")
      aggiornaPunteggio = False
  aggiornaPunteggioOld = aggiornaPunteggio
  
  
schermo.bye() 