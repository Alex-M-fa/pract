import tkinter as tk


root = tk.Tk()
root.title("Силы Сопротивления")
width = 600
height = 600
c = tk.Canvas(root, width=width, height=height, bg="black")
c.pack()
c.create_rectangle(0, height//2, width+2, height+2, fill='grey')


class Rec:

    def __init__(self, c, x1, y1, x2, y2, a, b, mass, color="white"):

        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
        self.a = a
        self.b = b
        self.c = c

        self.v = 4
        self.F_str = 0.015 * self.v * self.a * self.b
        self.mass = mass
        self.Acceleration = (self.F_str / mass) * 50
        self.ball = c.create_rectangle(self.x1 - self.a, self.y1 - self.b, self.x2 +
                                self.a, self.y2 + self.b, fill=color, outline='white', width=2)

    def move_ball(self):
        if c.coords(self.ball)[3] < height//2:
            c.move(self.ball, 0, self.v)
            c.after(1000//60, self.move_ball)
        elif height//2 <= c.coords(self.ball)[3] + self.F_str < height:
            c.move(self.ball, 0, self.F_str)
            c.after(1000//60, self.move_ball)
        else:
            c.move(self.ball, 0, height + 1 - c.coords(self.ball)[3])
            c.after(1000//60, self.iter_1)

    def iter_1(self):
        if c.coords(self.ball)[3] - self.Acceleration >= height - self.mass*0.2:
            c.move(self.ball, 0, - self.Acceleration)
            c.after(1000//60, self.iter_1)
        elif c.coords(self.ball)[3] <= height:
            c.after(1000//60, self.iter_2)

    def iter_2(self):
        if c.coords(self.ball)[3] + self.Acceleration < height:
            c.move(self.ball, 0, self.Acceleration)
            c.after(1000//60, self.iter_2)
        else:
            c.move(self.ball, 0, height + 1 - c.coords(self.ball)[3])
            c.after(1000//60, self.iter_3)

    def iter_3(self):
        if c.coords(self.ball)[3] - self.Acceleration >= height - self.mass*0.1:
            c.move(self.ball, 0, -self.Acceleration)
            c.after(1000//60, self.iter_3)
        else:
            c.after(1000//60, self.iter_stop)

    def iter_stop(self):
        if c.coords(self.ball)[3] + self.Acceleration < height:
            c.move(self.ball, 0, self.Acceleration)
            c.after(1000//60, self.iter_stop)

        else:
            # Конечная координата частицы равна height + 1
            c.move(self.ball, 0, height + 1 - c.coords(self.ball)[3])

def esc(event):
    root.destroy()


root.bind('<Escape>', esc)


# Создание частиц
# <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<  >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
a = 20
b = 10
mass1 = 601
ball1 = Rec(c, 100, 20, 100, 20, a, b, mass1, color="#a0a0a0")
ball1.move_ball()



root.mainloop()