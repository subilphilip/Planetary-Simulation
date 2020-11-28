from tkinter import *
from math import *
from turtle import *
G = 6.67408e-11
objects = []
period = 86400

output = 1
scale = 598391482.8
#3844000 for earth-moon, 598391482.8 for solar system,  550750000 for mars


class Body:
    def __init__(self, name, mass, xpos, ypos, xvel, yvel, color, size):
        objects.append(name)
        self.name = name
        self.mass = mass
        self.xpos = xpos
        self.ypos = ypos
        self.xvel = xvel
        self.yvel = yvel
        self.color = color
        self.size = size

        self.draw = Turtle()
        #self.draw.hideturtle()
        self.draw.left(90)
        self.draw.penup()
        self.draw.speed(0)
        self.draw.goto(self.xpos/scale, self.ypos/scale)
        self.draw.pendown()
        self.draw.color(color)
        #self.draw.dot(self.size, color)
        self.prevx = xpos
        self.prevy = ypos

    def calc(self):
        self.totalfx = 0
        self.totalfy = 0
        for object in objects:
            if object != self.name:
                object = eval(object)
                dx = object.prevx - self.xpos
                dy = object.prevy - self.ypos
                d = sqrt((dx**2)+(dy**2))
                f = (G*object.mass*self.mass)/(d**2)
                theta = atan2(dy, dx)
                fx = cos(theta) * f
                fy = sin(theta) * f
                self.totalfx += fx
                self.totalfy += fy
        self.xvel += self.totalfx/self.mass * period
        self.yvel += self.totalfy/self.mass * period
        self.xpos += self.xvel * period
        self.ypos += self.yvel * period

    def move(self):
        self.draw.goto(self.xpos/scale, self.ypos/scale)
        #self.draw.dot(self.size, self.color)

def press():
    run.destroy()
    days = 1
    while True:
        for i in range(output):
            for object in objects:
                eval(object).prevx = eval(object).xpos
                eval(object).prevy = eval(object).ypos
            for object in objects:
                eval(object).calc()
        print(days)
        days += 1 * period / 86400 * output

        for object in objects:
            eval(object).move()
def venuson():
    if CheckVar1.get() == 1:
        try:
            objects.remove("venus")
            objects.append("venus")
        except:
            objects.append("venus")

    if CheckVar1.get() == 0:
        try:
            objects.remove("venus")
        except:
            pass

def outputchange():
    global output
    output = outputslider.get()


#try:
#    output = int(input("""How often do you want the changes to be made?
#The larger the gap the faster the days go by, but the odder the orbit shape!"""))
#except:
#    pass

screen = Tk()
#canvas = screen.getcanvas()
run = Button(screen.master, text="START", command=press)
run.pack()#screen.create_window(-200, -200, window=run)
CheckVar1 = IntVar()
venon = Checkbutton(screen.master, text = "Venus", variable = CheckVar1, onvalue = 1, offvalue = 0, height=5, width = 20, command= venuson)
outputslider = Scale(screen, from_ = 1, to = 100, orient = HORIZONTAL)
outputslider.set(1)
outputslider.pack()
change = Button(screen, text= "Change Output", command = outputchange)
change.pack()
venon.pack()
venon.select()
sun = Body("sun", 1.9885e30, 0, 0, 0, 0, "yellow", 30)
mercury = Body("mercury", 3.3011e23, 57909050000, 0, 0, 47362, "gray", 8)
venus = Body("venus", 4.8675e24, 108208000000, 0, 0, 35020, "orange", 14)
#death = Body("death", -(1.9885e30), 227939200000, 0, 0, 0, "black", 30)
#earth = Body("earth", 5.97237e24, 149598023000, 0, 0, 29780, "blue", 15)
#moon = Body("moon", 7.342e22, 149598023000 + 384399000, 0, 0, 29780 + 1022, "gray", 5)
#mars = Body("mars", 6.4171e23, 227939200000, 0, 0, 24007, "red", 10)

# while True:
#     for i in range(output):
#         for object in objects:
#             eval(object).prevx = eval(object).xpos
#             eval(object).prevy = eval(object).ypos
#         for object in objects:
#             eval(object).calc()
#     print(days)
#     days += 1 * period / 86400 * output
#
#     for object in objects:
#         eval(object).move()
mainloop()
