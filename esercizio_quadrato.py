import turtle

# Create screen object
schermo = turtle.Screen()
schermo.title("Esercizio 1")# Set a custom screen size
schermo.screensize(800, 600, "lightblue")

# Crea un oggetto tartaruga
tartaruga = turtle.Turtle()
tartaruga.shape("turtle")

#Disegno gli assi
for _ in range(4):
    tartaruga.forward(400)  # Muovi la tartaruga in avanti di 100 pixel
    tartaruga.backward(400)
    tartaruga.left(90)     # Ruota la tartaruga di 90 gradi a sinistra

# Disegna un quadrato
for _ in range(4):
    tartaruga.forward(100)  # Muovi la tartaruga in avanti di 100 pixel
    tartaruga.left(90)     # Ruota la tartaruga di 90 gradi a sinistra

tartaruga.hideturtle()
# Chiudi la finestra grafica quando si clicca su di essa
turtle.exitonclick()
