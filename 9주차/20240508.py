# 2024-05-08 파이썬 - gui 프로그래밍
"""
 tkinter를 이용하여 간단한 GUI 프로그램을 작성할 수 있다. 

 tkinter는 파이썬에서 그래픽 사용자 인터페이스(GUI: graphical 
    user interface)를 개발할 때 필요한 모듈
 
    GUI의 일반적인 구조를 이해할 수 있다. 
 배치 관리자를 사용할 수 있다. 
 위젯의 콜백 함수를 이용하여 이벤트를 처리할 수 있다. 
 캔버스에 다양한 도형을 그릴 수 있다. 
 애니메이션을 만들 수 있다.
"""
# 1. 레이블이 있는 윈도우 생성

from tkinter import * # tkinter 모듈을 포함

window = Tk() # 루트 윈도우를 생성
label = Label(window, text="Hello tkinter") # 레이블 위젯을 생성
label.pack() # 레이블 위젯을 윈도우에 배치
window.mainloop() # 윈도우가 사용자 동작을 대기

# 2. 버튼 위젯을 포함한 윈도우

from tkinter import *

window = Tk()
button = Button(window, text="클릭하세요!",
bg="yellow", fg="blue", # 전경색과 배경색 설정
 width=80, height=2 # 크기 설정
)
button.pack()
window.mainloop()

# 3. 엔트리 위젯

from tkinter import *

window = Tk()
entry = Entry(window, fg="black", bg="yellow", width=80)
entry.pack()
window.mainloop()

# 4. 압축 배치 관리자

from Tkinter import *

window = Tk()
Label(window, text="박스 #1", bg="red", fg="white").pack()
Label(window, text="박스 #2", bg="green", fg="black").pack()
Label(window, text="박스 #3", bg="blue", fg="white").pack()
window.mainloop()


# 왼쪽에서 오른쪽으로 배치하려면 side를 LEFT로 지정하며, side는
# LEFT, RIGHT, TOP, BOTTOM 지정가능

from Tkinter import *
window = Tk()
Button(window, text="박스 #1", bg="red", fg="white").pack(side=LEFT)
Button(window, text="박스 #2", bg="green", fg="black").pack(side=LEFT)
Button(window, text="박스 #3", bg="orange", fg="white").pack(side=LEFT)
window.mainloop()

# 격자 배치 관리자(grid geometry manager)는 위젯 (버튼, 레이블 등)
# 을 테이블 형태로 배치한다. 

from tkinter import *
window = Tk()
b1 = Button(window, text="박스 #1", bg="red", fg="white")
b2 = Button(window, text="박스 #2", bg="green", fg="white")
b3 = Button(window, text="박스 #3", bg="orange", fg="white")
b4 = Button(window, text="박스 #4", bg="pink", fg="white")
b1.grid(row=0, column=0) # 0행 0열
b2.grid(row=0, column=1) # 0행 1열
b3.grid(row=1, column=0) # 1행 0열
b4.grid(row=1, column=1) # 1행 1열
window.mainloop()

# 여러 배치 관리자 혼용하기

from tkinter import *
window = Tk()
f = Frame(window)
b1 = Button(f, text="박스 #1", bg="red", fg="white")
b2 = Button(f, text="박스 #2", bg="green", fg="black")
b3 = Button(f, text="박스 #3", bg="orange", fg="white")
b1.pack(side=LEFT)
b2.pack(side=LEFT)
b3.pack(side=LEFT)
l = Label(window, text="이 레이블은 버튼들 위에 배치된다.")
l.pack()
f.pack()
window.mainloop()

# 윈도우의 크기와 위젯의 크기 설정하기

from tkinter import *
window = Tk()
window.geometry("600x100") # Width x Height
Button(window, text="박스 #1", width=10, height=1).pack()
Button(window, text="박스 #2", width=10, height=1).pack()
Button(window, text="박스 #3", width=10, height=1).pack()
window.mainloop()

# Lab 1: 온도 변환기

from tkinter import *
window = Tk()
Label(window , text="화씨").grid(row=0, column=0)
Label(window, text="섭씨").grid(row=1, column=0)
e1 = Entry(window).grid(row=0, column=1)
e2 = Entry(window).grid(row=1, column=1)
Button(window, text="화씨->섭씨").grid(row=2, column=1)
window.mainloop()

# Lab 2: 격자 배치 관리자 실습

Sol: from tkinter import *
window = Tk()
Label(window, text="너비").grid(row=0)
Label(window, text="높이").grid(row=1)
e1 = Entry(window)
e2 = Entry(window)
e1.grid(row=0, column=1)
e2.grid(row=1, column=1)
photo = PhotoImage(file="d://fig3.png")
label = Label(window, image=photo)
label.grid(row=0, column=2, columnspan=2, rowspan=2)
Button(window, text='이미지 저장').grid(row=2, column=0, columnspan=2)
# 두 번째 버튼과 세 번째 버튼은 2열과 3열에 표시한다. 
Button(window, text='확대').grid(row=2, column=2)
Button(window, text='축소').grid(row=2, column=3)
window.mainloop( )

# Lab 3: 카운터 만들기

from tkinter import *
window = Tk()
counter = 0
def clicked():
    global counter
    counter += 1
label['text'] = '버튼 클릭 횟수: ' + str(counter)
label = Label(window, text="아직 눌려지지 않음")
label.pack()
button = Button(window, text="증가", command=clicked).pack()
window.mainloop()

# Lab 4: 온도 변환기 #2

from tkinter import *
# 이벤트 처리 함수를 정의한다. 
def process():
tf = float(e1.get()) # e1에서 문자열을 읽어서 부동소수점형으로 변경
 tc = (tf-32.0)*5.0/9.0 # 화씨 온도를 섭씨 온도로 변환한다. 
e2.delete(0, END) # 처음부터 끝까지 지운다.
e2.insert(0, str(tc)) # tc 변수의 값을 문자열로 변환하여 추가한다.
window = Tk()
Label(window , text="화씨").grid(row=0, column=0)
Label(window, text="섭씨").grid(row=1, column=0)
e1 = Entry(window)
e2 = Entry(window)
e1.grid(row=0, column=1)
e2.grid(row=1, column=1)
Button(window, text="화씨->섭씨", command=process).grid(row=2, column=1)
window.mainloop()

# Lab 5 :

from tkinter import *
import random
answer = random.randint(1,100) # 정답을 1에서 100 사이의 난수로 설정한다.
def guessing():
guess = int(guessField.get()) # 텍스트 필드에서 사용자가 입력한 값을 가져온다.
if guess > answer:
msg = "높음!"
elif guess < answer:
msg = "낮음!"
else:
msg = "정답!"
resultLabel["text"] = msg # 메시지를 출력한다.
guessField.delete(0, 5)
    
def reset(): # 정답을 다시 설정한다.
global answer
answer = random.randint(1,100)
resultLabel["text"] = "다시 한번 하세요!"
window = Tk()
window.configure(bg="white")
window.title("숫자를 맞춰보세요!")
window.geometry("500x80")
titleLabel = Label(window, text="숫자 게임에 오신 것을 환영합니다!",
bg="white")
titleLabel.pack()

guessField = Entry(window)
guessField.pack(side="left")
tryButton = Button(window, text="시도", fg="green", bg="white",
command=guessing )
tryButton.pack(side="left")
resetButton = Button(window, text="초기화", fg="red", bg="white",
command=reset)
resetButton.pack(side="left")
resultLabel = Label(window, text="1부터 100사이의 숫자를 입력하시오.",
bg="white")
resultLabel.pack(side="left")
window.mainloop()

# 가위바위보 게임

import random
from tkinter import *
window = Tk()
Label(window, text="선택하세요", font=("Helvetica", "16")).pack()
frame = Frame(window)
# 이미지를 d 드라이브로 복사하여 주세요!
rock_image = PhotoImage(file="d:\\rock.png")
paper_image = PhotoImage(file="d:\\paper.png")
scissors_image = PhotoImage(file="d:\\scissors.png")
# 교재 오타!!
def pass_s():
decide("가위")
def pass_r():
decide("바위")
def pass_p():
decide("보")
rock = Button(frame, image=rock_image, command=pass_r)
rock.pack(side="left")
paper = Button(frame, image=paper_image, command=pass_p)
paper.pack(side="left")
scissors = Button(frame, image=scissors_image, command=pass_s)
scissors.pack(side="left")
frame.pack()
Label(window, text="컴퓨터는 다음을 선택하였습니다.", font=("Helvetica", "16")).pack()
computer_image = Label(window, image=rock_image)
computer_image.pack()
output = Label(window, text="", font=("Helvetica", "16"))
output.pack()

def decide(human):
computer = random.choice(["가위", "바위", "보"])
if computer == "바위":
computer_image["image"] = rock_image
elif computer == "보":
computer_image["image"] = paper_image
else:
computer_image["image"] = scissors_image
if (computer == "바위" and human == "보") or (computer == "보" and human == "가위
")\
or (computer == "가위" and human == "바위"):
result = "인간 승리!"
elif computer == human:
result = "비겼습니다."
else:
result = "컴퓨터 승리!"
output.config(text="인간: " + human + " 컴퓨터:" + computer + " " + result)
window.mainloop() 

# tic-tac-toc 게임

from tkinter import *
# i번째 버튼을 누를 수 있는지 검사한다. 누를 수 있으면 X나 O를 표시한다. 
def checked(i):
    global player
button = list[i] # 리스트에서 I번째 버튼 객체를 가져온다. 
# 버튼이 초기 상태가 아니면 이미 누른 버튼이므로 아무것도 하지 않고 리턴
if button["text"] != " ":
    return
    button["text"] = " " + player+" "
    button["bg"] = "yellow"
if player=="X":
    player = "O"
    button["bg"] = "yellow"
else :
    player = "X"
    button["bg"] = "lightgreen"

indow = Tk() # 윈도우를 생성한다. 
player="X" # 시작은 플레이어 X이다. 
list = []
# 9개의 버튼을 생성하여 격자 형태로 윈도우에 배치한다. 
for i in range(9):
    b = Button(window, text=" ", command=lambda k=i: checked(k))
    b.grid(row=i//3, column=i%3)
list.append(b) # 버튼 객체를 리스트에 저장한다. 
window.mainloop()

# 마우스 이벤트 처리 1

from tkinter import *
window = Tk()
window.geometry("600x200") 
def callback(event):
print(event.x, event.y, "에서 마우스 이벤트 발생")
window.bind("<Button-1>", callback)
window.mainloop()


# 마우스 이벤트 처리 2

from tkinter import *
window = Tk()
def key(event):
print ( repr(event.char), "가 눌렸습니다. ")
def callback(event):
frame.focus_set()
print(event.x, event.y, "에서 마우스 이벤트 발생")
frame = Frame(window, width=100, height=100)
frame.bind("<Key>", key)
frame.bind("<Button-1>", callback)
frame.pack()
window.mainloop()


# Lab: 그림판 프로그램 만들기

penButton = Button(window, text='펜', command=use_pen)
penButton.grid(row=0, column=0, sticky=W+E)
brushButton = Button(window, text='브러쉬', command=use_brush)
brushButton.grid(row=0, column=1, sticky=W+E)
colorButton = Button(window, text='색상선택', command=choose_color)
colorButton.grid(row=0, column=2, sticky=W+E)
eraseButton = Button(window, text='지우개', command=use_eraser)
eraseButton.grid(row=0, column=3, sticky=W+E)
clearButton = Button(window, text='모두삭제', command=clear_all)
clearButton.grid(row=0, column=4, sticky=W+E)


var = DoubleVar()
...
scale = Scale(window, variable=var, orient=VERTICAL)
scale.grid(row=1, column=5, sticky=N+S)

canvas.bind('<B1-Motion>', paint)
canvas.bind('<ButtonRelease-1>', reset)
각 마우스 이벤트가 발생하면 다음과 같은 함수들이 호출된다. 
def paint(event):
global var, erase_on, mode, old_x, old_y
fill_color = "white" if mode == "erase" else mycolor
if old_x and old_y:
canvas.create_line(old_x, old_y, event.x, event.y,
capstyle=ROUND, width=var.get(), fill=fill_color)
old_x = event.x
old_y = event.y
def reset(event):
global old_x, old_y
old_x, old_y = None, None

def use_pen(): # 펜 버튼이 선택되면 모드를 ”pen"으로 바꾼다. 
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

# Lab: 공 애니메이션 I

from tkinter import *
import time
import random
window = Tk()
canvas=Canvas(window, width=600,height=400)
canvas.pack()

class Ball():
def __init__(self,color,size): 
self.id=canvas.create_oval(0, 0, size, size,fill=color)
self.dx=random.randint(1,10)
self.dy=random.randint(1,10)
def move(self):
canvas.move(self.id,self.dx,self.dy)
x0, y0, x1, y1 = canvas.coords(self.id)
if y1 > canvas.winfo_height() or y0 < 0: # 원이 위쪽이나 아래쪽으로 벗어났으면
 self.dy = -self.dy # dy의 부호를 반전시킨다. 
if x1 > canvas.winfo_width() or x0 < 0: # 원이 왼쪽이나 오른쪽으로 벗어났으면
 self.dx = -self.dx # dx의 부호를 반전시킨다.

ball1=Ball("blue", 60)
ball2=Ball("green",100)
ball3=Ball("orange",80)
while True:
ball1.move()
ball2.move()
ball3.move()
window.update()
time.sleep(0.05)
window.mainloop()

# 공 애니메이션 2 

class Ball():
def __init__(self,color,size): 
self.id=canvas.create_oval(0, 0, size, size,fill=color)
self.dx=random.randint(1,10)
self.dy=random.randint(1,10)
from tkinter import *
import time
import random
window = Tk()
canvas=Canvas(window, width=600,height=400)
canvas.pack()

def move(self):
canvas.move(self.id,self.dx,self.dy)
x0, y0, x1, y1 = canvas.coords(self.id)
if y1 > canvas.winfo_height() or y0 < 0: # 원이 위쪽이나 아래쪽으로 벗어났으면
 self.dy = -self.dy # dy의 부호를 반전시킨다. 
if x1 > canvas.winfo_width() or x0 < 0: # 원이 왼쪽이나 오른쪽으로 벗어났으
면
 self.dx = -self.dx # dx의 부호를 반전시킨다. 

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


"""
이번 장 배운 내용

 tkinter에서는 먼저 루프 윈도우를 생성하고 레이블이나 버튼을 생성할 때
첫 번째 인수로 윈도우를 넘기면 된다.
 파이썬은 3종류의 배치 관리자를 제공한다. 배치 관리자, 격자(grid) 배치
관리자. 절대(place) 배치 관리자가 바로 그것이다.
 위젯에 이벤트를 처리하는 함수를 연결하려면 bind() 메소드를 사용한다. 
예를 들면 widget.bind(‘<Button-1>’, sleft)와 같이 하면 된다.

"""







