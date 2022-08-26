from tkinter import *
import random
import time

class Ball:
    def __init__(self, canvas, color):
        self.canvas = canvas

        self.id = canvas.create_rectangle(50, 50, 25, 25, fill=color)

        starts = [-3, -2, -1, 1, 2, 3]
        random.shuffle(starts)

        self.times = 0
        self.clash = 0
        self.x = starts[0]
        self.y = -3
        self.canvas_height = canvas.winfo_height()
        self.canvas_width = canvas.winfo_width()

        canvas.move(self.id, 245, 100)

    def addTimes(self):
        self.clash = self.clash + 1
        if self.clash == 4 and not self.times > 5:
            self.clash = 0
            self.times = self.times + 1


    def draw(self):
        self.canvas.move(self.id, self.x, self.y)

        pos = self.canvas.coords(self.id)
        if pos[1] <= 0:
            self.addTimes()
            self.y = 3 + self.times
        elif pos[3] >= self.canvas_height:
            self.addTimes()
            self.y = -3 - self.times
        elif pos[0] <= 0:
            self.addTimes()
            self.x = 3 + self.times
        elif pos[2] >= self.canvas_width:
            self.addTimes()
            self.x = -3 - self.times

tk = Tk()
tk.title('ScreenSaver')
canvas = Canvas(tk, width=1200, height=600, bd=0, highlightthickness=0)
canvas.pack()
tk.update()


ball = Ball(canvas, 'red')

while 1:
    ball.draw()    
    tk.update()
    tk.update_idletasks()
    time.sleep(0.0001)