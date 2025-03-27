import turtle

# Create screen object
schermo = turtle.Screen()
schermo.title("Esercizio 1")

# Set a custom screen size
schermo.screensize(800, 600, "lightblue")

# Crea un oggetto tartaruga
tartaruga = turtle.Turtle()
tartaruga2 = turtle.Turtle() #creo una seconda penna

#Disegno gli assi
for _ in range(4):
    tartaruga.forward(400)  # Muovi la tartaruga in avanti di 100 pixel
    tartaruga.backward(400)
    tartaruga.left(90)     # Ruota la tartaruga di 90 gradi a sinistra

# Disegna un quadrato
for _ in range(4):
    tartaruga.forward(100)  # Muovi la tartaruga in avanti di 100 pixel
    tartaruga2.forward(-100)  # Muovi la tartaruga in avanti di 100 pixel
    tartaruga.left(90)     # Ruota la tartaruga di 90 gradi a sinistra
    tartaruga2.left(90)

# Chiudi la finestra grafica quando si clicca su di essa
turtle.exitonclick()
