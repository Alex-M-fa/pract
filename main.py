from tkinter import *
from random import randint


class Raindrop:
    def __init__(self, canvas, x, y, yspeed, length, color='#4682B4'):
        self.x = x
        self.y = y
        self.yspeed = yspeed
        self.length = length
        self.canvas = canvas
        self.line = canvas.create_line(self.x, self.y, self.x, self.y+length, fill=color)

    def move(self):
        self.y += self.yspeed
        self.canvas.move(self.line, 0, self.yspeed)

        # При падении за нижний край холста передвигаем каплю выше верхнего края холста
        if self.y > 600:
            self.canvas.move(self.line, 0, - (600 + self.length))
            self.y -= 600 + self.length


def draw_rain():
    for drop in drops:
        drop.move()

    root.after(8, draw_rain)


root = Tk()
canvas = Canvas(root, width=600, height=600)
canvas.pack()

drops = [Raindrop(canvas, x=randint(0, 600), y=randint(0, 600),
                  yspeed=randint(1, 3), length=randint(5, 20)) for i in range(150)]

draw_rain()

root.mainloop()