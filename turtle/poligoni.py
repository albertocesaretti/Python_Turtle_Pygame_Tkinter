from turtle import *

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
class Polyline:
    def __init__(self):
        self.points = []
        self.ninja = Turtle
    def	add_point(self, point):
        self.points.append(point)
    def	add_points(self, points):
        self.points += points
    def	draw(self):
        self.ninja = Turtle()
        self.ninja.speed(0)
        self.ninja.hideturtle()
        self.ninja.penup()
        self.ninja.goto(self.points[0].x, self.points[0].y)
        self.ninja.pendown()
        
        for point in self.points[1:]:
            self.ninja.goto(point.x, point.y)
"""
        3 Scrivi con Thonny il codice Python riportato di seguito,
        per costruire e disegnare una polilinea.
        Con File →Salva con nome... salva il modulo con nome app.py.

        from turtle import done
        from point import Point
        from polyline import Polyline
"""
#main
polyline = Polyline()
polyline.add_point(Point(0, 0))
polyline.add_points([Point(20, 50), Point(0, 100), Point(-100, 150), Point(100, 200)])
polyline.draw()
exitonclick()