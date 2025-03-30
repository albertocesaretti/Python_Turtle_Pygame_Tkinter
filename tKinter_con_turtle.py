import turtle
import tkinter as tk

def disegna_quadrato():
    tartaruga.begin_fill()
    tartaruga.color("red")
    for i in range(4):
        tartaruga.fd(100)
        tartaruga.left(90)
    tartaruga.end_fill()
    
#main
schermo = tk.Tk() #creo lo schemo
schermo.title("Turtle in Tkinter")
schermo.geometry("800x600")
#schermo.configure(background='yellow')
schermo.resizable(width=False, height=False)

canvas1 = tk.Canvas(schermo, width=500, height=500, bg="yellow")
canvas1.grid(row=0,column=0)

schermoTurtle = turtle.TurtleScreen(canvas1)
tartaruga = turtle.RawTurtle(schermoTurtle)

btn = tk.Button(schermo, text = "Disegna", font=("Arial",14), fg = "red", command = disegna_quadrato)
btn.grid(row=1, column=0, sticky ="w")

schermo.mainloop() #creo un ciclo