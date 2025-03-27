import turtle

class FiguraGeometrica:
    """Rappresenta una generica figura geometrica."""
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
        
    def init_draw(self,pen):
        pen.hideturtle()
        pen.up()
        pen.speed(0)
        pen.goto(self.x, self.y)
        pen.down()
        pen.begin_fill()

    def end_draw(self,pen):
        pen.end_fill()
        pen.up()

class Cerchio(FiguraGeometrica):
    """Rappresenta un cerchio disegnato tramite il metodo dot() di Turtle."""
    def __init__(self, x, y, colore,raggio):
        super().__init__(x, y)
        self.colore = colore
        self.raggio = raggio

    def draw(self,pen):
        self.init_draw(pen)  # Metodo definito in FiguraGeometrica
        pen.pencolor(self.colore)
        pen.dot(self.raggio * 2)
        self.end_draw(pen)  # Metodo definito in FiguraGeometrica

class Quadrato(FiguraGeometrica):
    """Rappresenta un quadrato."""
    def __init__(self, x, y, colore,lato):
        super().__init__(x, y)
        self.colore = colore
        self.lato = lato
        self.pen = pen

    def draw(self,pen):
        self.init_draw(pen)  # Metodo definito in FiguraGeometrica
        pen.color(self.colore)
        for _ in range(4):
            pen.forward(self.lato)  # Muovi la tartaruga in avanti di lato
            pen.left(90) 
        self.end_draw(self.pen)  # Metodo definito in FiguraGeometrica

# Create screen object
schermo = turtle.Screen()
schermo.title("Esercizio 1")# Set a custom screen size
schermo.screensize(800, 600, "lightblue")

# Crea un oggetto penna
pen = turtle.Turtle()

figura = FiguraGeometrica(100,100)
#disegno cerchio
cerchio = Cerchio(-100, -100, "red", 30)
cerchio.draw(pen)

# Disegna un quadrato
quadrato = Quadrato(100,100, "blue", 80)
quadrato.draw(pen)

pen.hideturtle()
# Chiudi la finestra grafica quando si clicca su di essa
turtle.exitonclick()
