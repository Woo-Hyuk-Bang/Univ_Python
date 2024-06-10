# 2024-05-14 파이썬 - 실습코드
"""
1. p432 ~ 433 calculator2.py
2. p445 ~ 446 paint.py
3. p449 ~ 450 bounding_ball3.py

"""

# 1.
from tkinter import *

window = Tk()
window.title("My calculator")
display = Entry(window, width=33, bg="yellow")
display.grid(row=0, column=0, columnspan=5)

button_list = [
'7',  '8',  '9',  '/',  'C',    
'4',  '5',  '6',  '*',  ' ',   
'1',  '2',  '3',  '-',  ' ', 
'0',  '.',  '=',  '+',  ' ' ]

def click(key):
    if  key == "=":
        result = eval(display.get())
        s = str(result)
        display.insert(END, "=" + s)
    else:
        display.insert(END, key)

row_index = 1
col_index = 0
for button_text in button_list:
    Button(window, text=button_text, width=5,
           command=lambda t=button_text: click(t)).grid(row=row_index,
                                                        column=col_index)
    col_index += 1
    if col_index > 4:
        row_index += 1
        col_index = 0
window.mainloop()

# 2. 페인트 프로그램

from tkinter import *
from tkinter.colorchooser import askcolor

DEFAULT_PEN_SIZE = 1.0
DEFAULT_COLOR = "black"

mode = "pen"
old_x = None
old_y = None
mycolor = DEFAULT_COLOR
erase_on = False

def use_pen():
    global mode
    mode = "pen"
    
def use_brush():
    global mode
    mode = "brush"
    
def choose_color():
    global mycolor
    mycolor = askcolor(color=mycolor)[1]
    
def use_erase():
    global mode
    mode = "erase"
    
def paint(event):
    global var, erase_on, mode, old_x, old_y
    fill_color = 'white' if mode == "erase" else mycolor
    if old_x and old_y:
        canvas.create_line(old_x, old_y, event.x, event.y,
                           capstyle=ROUND, width=var.get(), fill=fill_color)
        
    old_x = event.x
    old_y = event.y

def reset(event):
    global old_x, old_y
    old_x, old_y = None, None
    
def clear_all():
    global canvas
    canvas.delete('all')
    
window = Tk()
var = DoubleVar()

penButton = Button(window, text="펜", command=use_pen)
penButton.grid(row=0, column=0, sticky=W+E)

brushButton = Button(window, text="브러쉬", command=use_brush)
brushButton.grid(row=0, column=1, sticky=W+E)

colorButton = Button(window, text="색상선택", command=choose_color)
colorButton.grid(row=0, column=2, sticky=W+E)

eraseButton = Button(window, text="지우개", command=use_erase)
eraseButton.grid(row=0, column=3, sticky=W+E)

clearButton = Button(window, text="모두 삭제", command=clear_all)
clearButton.grid(row=0, column=4, sticky=W+E)

scale = Scale(window, variable=var, orient=VERTICAL)
scale.grid(row=0, column=5, sticky=W+E)

canvas = Canvas(window, bg='white', width=600, height=400)
canvas.grid(row=0, columnspan=5)

canvas.bind('<B1-Motion>', paint)
canvas.bind('<ButtonRelease-1>', reset)

# 3. bouncing_ball3.py - 공 애니메이션

from tkinter import *
import time
import random

window = Tk()

canvas = Canvas(window, width=600, height=400)
canvas.pack()

class Ball():
    def __init__(self, color, size):
        self.id=canvas.create_oval(0, 0, size, size, fill=color)
        self.dx=random.randint(1,10)
        self.dy=random.randint(1,10)

    def move(self):
        canvas.move(self.id, self.dx, self.dy)
        x0, y0, x1, y1 = canvas.coords(self.id)
        if y1 > canvas.winfo_height() or y0 < 0:
            
            self.dy = -self.dy
        if x1 > canvas.winfo_width() or x0 < 0:
            
            self.dx = -self.dx
            
colors = ["red", "orange", "yellow", "green", "blue", "indigo", "violet"]
ballList = []
for i in range(30):
    ballList.append(Ball(random.choice(colors), 60))
    
while True:
    for i in range(30):
        ballList[i].move()
    window.update()
    time.sleep(0.05)
    
window.mainloop()