# 1.주급 계산 프로그램(p.223)

##
# 주급 계산 프로그램
#


def weeklyPay(rate, hour):
    money = 0
    if (hour > 30):
        money = rate*30 + 1.5*rate*(hour-30)
    else :
        money = rate*hour
    return money

rate = int(input("시급을 입력하십시오:"))
hour = int(input("근무 시간을 입력하시오:"))
print("주급은 "+ str(weeklyPay(rate, hour)))

# 도전과제
# 1) 시급이 주어지지 않을 경우, 최저 시급 10000을 가정한다.

def weeklyPay(rate, hour):
    money = 0
    if (hour > 30):
        money = rate*30 + 1.5*rate*(hour-30)
    else :
        money = rate*hour
    return money

rate = input("시급을 입력하십시오:")
if rate == "":
    rate = 10000
else:
    rate = int(rate)
hour = int(input("근무 시간을 입력하시오:"))
print("주급은 "+ str(weeklyPay(rate, hour)))

# 2) 키워드 인수 방식으로 함수로 값을 전달하라

def weeklyPay(rate, hour):
    money = 0
    if hour > 30:
        money = rate * 30 + 1.5 * rate * (hour - 30)
    else:
        money = rate * hour
    return money

rate = int(input("시급을 입력하십시오:"))
hour = int(input("근무 시간을 입력하시오:"))
print("주급은 " + str(weeklyPay(rate=rate, hour=hour)))

# 사각형을 그리는 프로그램
#
# 이 프로그램은 사각형을 그리는 함수를 작성 및 사용
#

import turtle
t = turtle.Turtle()
t.shape("turtle")

def square(length):
    t.down()
    for i in range(4):
        t.forward(length)
        t.left(90)
    t.up()
    
square(100);
t.forward(120)
square(100);
t.forward(120)
square(100);

turtle.mainloop()
turtle.bye()

# 1) 6각형을 그리는 함수를 작성, 일반적인 n각형을 그리는 함수는?

import turtle
t = turtle.Turtle()
t.shape("turtle")

n = turtle.textinput("그리고자 하는 도형의 각의 개수는?", "그리고자 하는 각을 입력")
k = int(n)

def drawing(length):
    t.down()
    angle = 360 / k
    for i in range(k):
        t.forward(length)
        t.left(angle)
    t.up()

drawing(50);
t.forward(60)
drawing(50);
t.forward(60)
drawing(50);

turtle.mainloop()
turtle.bye()

# 몇 가지의 색상을 리스트에 저장하고 번갈아 사용해서 사각형을 채울 수 있는가?

import turtle

t = turtle.Turtle()
t.shape("turtle")

# 사용할 색상 리스트
colors = ["red", "green", "blue", "orange", "purple"]

def draw_filled_square(length, color):
    t.color(color)  # 색상 설정
    t.begin_fill()  # 채우기 시작
    for _ in range(4):
        t.forward(length)
        t.left(90)
    t.end_fill()    # 채우기 끝

# 사각형을 번갈아가며 그리기
for i in range(5):
    draw_filled_square(100, colors[i % len(colors)])  # 색상을 리스트에서 순환하면서 선택

turtle.mainloop()
turtle.bye()

# 온도를 변환하는 프로그램

def menu() :
    print("1. 섭씨 온도-> 화씨 온도")
    print("2. 화씨 온도-> 섭씨 온도")
    print("3. 종료")
    selection = int(input("메뉴를 선택하세요: "))
    return selection

def ctof(c):
    temp = c*9.0/5.0 + 32
    return temp

def ftoc(f):
    temp = (f-32.0)*5.0/9.0
    return temp

def input_f():
    f = float(input("화씨 온도를 입력하시오: "))
    return f

def input_c():
    c = float(input("섭씨 온도를 입력하시로: "))
    return c

def main() :
    while True:
        index = menu()
        if index == 1 :
            t = input_c()
            t2 = ctof(t)
            print("화씨 온도 = ", t2, "\n")
        elif index == 2 :
            t = input_f()
            t2 = ftoc(t)
            print("섭씨 온도 = ", t2, "\n")
        else :
            break

main()

# Lab: 프랙탈 그래픽

import turtle

def drawTree(branch,t):
    if branch > 5:
        t.forward(branch)
        t.right(20)
        drawTree(branch-15,t) # 순환 호출
        t.left(40)
        drawTree(branch-15,t) # 순환 호출
        t.right(20)
        t.backward(branch)
        
def main():
    t = turtle.Turtle()
    window = turtle.Screen()
    t.left(90)
    t.up()
    t.backward(200)
    t.down()
    t.color("green")
    drawTree(100, t)
    window.exitonclick()
    
main() 

# 도전과제 - 나무의 길이에 난수를 지정해주기

import turtle
import random

def drawTree(branch, t):
    if branch > 5:
        t.forward(branch)
        t.right(20)
        drawTree(branch - random.randint(10, 20), t)  # 난수를 이용하여 가지의 길이를 결정
        t.left(40)
        drawTree(branch - random.randint(10, 20), t)  # 난수를 이용하여 가지의 길이를 결정
        t.right(20)
        t.backward(branch)

def main():
    t = turtle.Turtle()
    window = turtle.Screen()
    t.left(90)
    t.up()
    t.backward(200)
    t.down()
    t.color("green")
    drawTree(100, t)
    window.exitonclick()

main()

# Lab: 막대 그래프 그리기

import turtle
def drawBar(height):
    t.begin_fill() 
    t.left(90)
    t.forward(height)
    t.write(str(height), font = ('Times New Roman', 16, 'bold'))
    t.right(90)
    
    t.forward(40)
    t.right(90)
    t.forward(height)
    t.left(90)
    t.end_fill() 

data = [120, 56, 309, 220, 156, 23, 98] 

t = turtle.Turtle() 
t.color("blue")
t.fillcolor("red")

t.pensize(3)

for d in data:
    drawBar(d)
    
turtle.mainloop()
turtle.bye()
