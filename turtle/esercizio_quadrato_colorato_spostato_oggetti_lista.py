import turtle

# Create screen object
schermo = turtle.Screen()
schermo.title("Esercizio 1")# Set a custom screen size
schermo.screensize(800, 600, "lightblue")

class FiguraGeometrica:#classe padre, base, super classe
    def __init__(self, x,y):
        self.x = x
        self.y = y

    def preparaSpostaPenna(self,pen):
        pen.up()
        pen.goto(self.x,self.y)
        pen.down()
        pen.begin_fill()
 
    def terminaDisegno(self,pen):
        pen.end_fill()
        pen.up()
        pen.hideturtle()

class Quadrato(FiguraGeometrica):
    def __init__(self,x,y, colore, lato):
        super().__init__(x,y)
        self.colore = colore
        self.lato = lato
        
    def disegna(self,pen):
        self.preparaSpostaPenna(pen)
        pen.color(self.colore)
        for _ in range(4):
            pen.forward(self.lato)  # Muovi la tartaruga in avanti di 100 pixel
            pen.left(90)     # Ruota la tartaruga di 90 gradi a sinistra
        self.terminaDisegno(pen)

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
"""
# Crea un oggetto tartaruga
pen = turtle.Turtle()
pen.shape("turtle")
import random as r
lista_colori = ["red","yellow","black","pink","orange"]
lista_quadrati = []
for i in range(10):    
    quadrato = Quadrato(r.randint(-300,300),r.randint(-300,300),\
                        r.choice(lista_colori), r.randint(50,100))
    lista_quadrati.append(quadrato)

for i in range(10):
    lista_quadrati[i].disegna(pen)
#quadrato2 = Quadrato(-100,-100,"yellow", 100)
#quadrato2.disegna(pen)


"""
disegnaAssi(pen)
preparaSpostaPenna(100,100,pen,"red")
disegnaQuadrato(pen)
terminaDisegno(pen)
"""
# Chiudi la finestra grafica quando si clicca su di essa
turtle.exitonclick()
