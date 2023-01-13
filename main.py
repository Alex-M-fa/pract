from tkinter import *
import math
import time

root = Tk()
root.title("Задание 1")
window = Canvas(root, width=600, height=600)
window.pack()

a = 30
b = 30
radius = 200

t = 0
while t < 2 * math.pi:
    coord_x = radius * math.cos(t) + a + 200
    coord_y = radius * math.sin(t) + b + 200
    coord_x1 = radius * math.cos(t + 0.1) + a + 200
    coord_y1 = radius * math.sin(t + 0.1) + b + 200
    print('x=' + str(coord_x) + ' y=' + str(coord_y) + ' x1=' + str(coord_x1) + ' y1=' + str(coord_y1))
    window.create_line(coord_x, coord_y, coord_x1, coord_y1)
    t += 0.1

t = 0
radius2 = 10
coord_x = radius * math.cos(t) + a + radius
coord_y = radius * math.sin(t) + b + radius
ball = window.create_oval(coord_x - radius2, coord_y - radius2, coord_x + radius2, coord_y + radius2, fill="#0f1111")
while True:
    coord_x = radius * math.cos(t) + a + radius
    coord_y = radius * math.sin(t) + b + radius
    coord_x1 = radius * math.cos(t + 0.1) + a + radius
    coord_y1 = radius * math.sin(t + 0.1) + b + radius
    t += 0.1
    window.move(ball, coord_x1 - coord_x, coord_y1 - coord_y)
    root.update()
    time.sleep(0.04)

root.mainloop()
