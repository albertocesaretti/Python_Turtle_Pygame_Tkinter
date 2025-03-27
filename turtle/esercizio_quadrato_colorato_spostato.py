import turtle
import random as r

class FiguraGeometrica:#padre, super classe, classe base 
    def __init__(self,x,y):
        self.x = x
        self.y = y
        
    def preparaSpostaPenna(self,pen):
        pen.speed(0)
        pen.up()
        pen.goto(self.x,self.y)
        pen.down()
        pen.begin_fill()
        
    def terminaDisegno(self,pen):
        pen.end_fill()
        pen.up()
        pen.hideturtle() 

class Quadrato(FiguraGeometrica):#classe figlio, sottoclasse
    def __init__(self, x, y, colore, lato):
        super().__init__(x,y)
        self.colore = colore
        self.lato = lato
        
    def disegna(self,pen):
        self.preparaSpostaPenna(pen)
        pen.color(self.colore)
        for i in range(4):
            pen.fd(self.lato)
            pen.left(90)
        self.terminaDisegno(pen)

class Cerchio(FiguraGeometrica):
    def __init__(self, x, y, colore, raggio):
        super().__init__(x,y)
        self.colore = colore
        self.raggio = raggio
        
    def disegna(self,pen):
        self.preparaSpostaPenna(pen)
        pen.color(self.colore)
        pen.dot(self.raggio*2, self.colore)
        self.terminaDisegno(pen)    
#main
# Create screen object
schermo = turtle.Screen()
schermo.title("Esercizio 1")# Set a custom screen size
schermo.screensize(800, 600, "lightblue")

pen = turtle.Turtle()
lista_colori = ["red","white","yellow","pink","orange"]
lista_quadrati = []
lista_cerchi = []
for i in range(20):
    quadrato = Quadrato(r.randint(-300,300),\
                        r.randint(-300,300),r.choice(lista_colori),r.randint(50,100))
    lista_quadrati.append(quadrato)

for i in range(20):
   lista_quadrati[i].disegna(pen)
   
   
for i in range(20):
    cerchio = Cerchio(r.randint(-300,300), r.randint(-300,300),\
                      r.choice(lista_colori), r.randint(20,30))
    lista_cerchi.append(cerchio)

for i in range(20):
   lista_cerchi[i].disegna(pen)    
"""
quadrato1 = Quadrato(100,100,"red",80)
quadrato1.disegna(pen)

cerchio1 = Cerchio(-100, -100, "blue", 30)
cerchio1.disegna(pen)
"""
"""
#Disegno gli assi
def disegnaAssi(pen):   
    for _ in range(4):
        pen.forward(400)  # Muovi la tartaruga in avanti di 100 pixel
        pen.backward(400)
        pen.left(90)     # Ruota la tartaruga di 90 gradi a sinistra

# Disegna un quadrato
def disegnaQuadrato(pen):
    for _ in range(4):
        pen.forward(100)  # Muovi la tartaruga in avanti di 100 pixel
        pen.left(90)     # Ruota la tartaruga di 90 gradi a sinistra
        

def preparaSpostaPenna(x,y,pen,colore):
    pen.up()
    pen.goto(x,y)
    pen.down()
    pen.begin_fill()
    pen.color(colore)

def terminaDisegno(pen):
    pen.end_fill()
    pen.up()
    pen.hideturtle()

# Crea un oggetto tartaruga
pen = turtle.Turtle()
pen.shape("turtle")
disegnaAssi(pen)
preparaSpostaPenna(100,100,pen,"red")
disegnaQuadrato(pen)
terminaDisegno(pen)
"""
# Chiudi la finestra grafica quando si clicca su di essa
turtle.exitonclick()
