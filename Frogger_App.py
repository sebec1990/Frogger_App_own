import tkinter
import math
from turtle \
import RawTurtle


class Frog(RawTurtle):
    def __init__(self,canvas):
        super().__init__(canvas)
        self.shape("Img/frogger.gif")
        self.left(90)
        self.penup()
        self.goto(0,-250)

class FroggerApplication(tkinter.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.pack()
        self.buildWindow()
        
    def buildWindow(self):
        self.master.title("Frogger!")
        canvas = tkinter.Canvas(self, width=600, height=600)
        canvas.pack(side=tkinter.LEFT)

        turtle = RawTurtle(canvas)
        screen = turtle.getscreen()
        screen.tracer(0)
        screen.register_shape("Img/frogger.gif")

        turtle.color("blue")
        turtle.begin_fill()
        for distance in [350, 200, 700,200, 350]:
            turtle.forward(distance)
            turtle.left(90)
        turtle.end_fill()
        turtle.ht()


        turtle = RawTurtle(canvas)
        turtle.color("grey")
        turtle.begin_fill()
        for distance in [350, 200, 700, 200, 350]:
            turtle.forward(distance)
            turtle.right(90)
        turtle.end_fill()
        turtle.ht()

        frog = Frog(canvas)


        def jump():
            frog.forward(10)
            screen.update()

        screen.onkeypress(jump, "Up")
        screen.listen()

        screen.update()

def main():
    root = tkinter.Tk()
    application = FroggerApplication(root)
    application.mainloop()
    
main()