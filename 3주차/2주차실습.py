# -*- coding: utf-8 -*-
"""
Created on Wed Mar 20 11:47:52 2024

@author: User
"""

# 1. P 125 도전문제에서 덧셈 뿐만 아니라 뺄셈과 곱셈 믄제도 출제할 수 있도록 프로그램을 수정하라.

import random
case = random.ranint(1,2,3)
x = random.randint(1,100)
y = random.randint(1,100)

if (case == 1) :
    answer = int(input(f"{x} + {y} = "))
    flag = (answer == (x+y))
elif (case == 2) :
    answer = int(input(f"{x} - {y} = "))
    flag = (answer == (x-y))
elif (case == 3) :
    answer = int(input(f"{x} * {y} = "))
    flag = (answer == (x*y))
    
#flag = (answer == (x+y)) # true or false
print(flag)

# 2. P 127 도전 문제 (1), (2)를 프로그램으로 작성하라. 
#1) 사용자로부터 받은 정수가 양수인지 음수인지 구별하는 프로그램을 작성하라, 0은 양수로 간주한다

x = int(input("정수를 입력해주세요 :"))

if (x >= 0):
    print("양수입니다")
elif (x < 0):
    print("음수입니다")

#2) 프로그램에서 사용자의 성적을 입력받는다. 60이상이면 합격입니다. 그렇지 않으면 불합격입니다를 출력하라

score = int(input("점수를 입력해주세요 :"))

if (score >= 60) :
    print("합격입니다")
else:
    print("불합격입니다")

# 3. P 133 도전문제를 프로그램으로 작성하라. 섭씨 = (화씨-32)*5/9
#-> 물의 상태 출력프로그램 사용자가 화씨 온도로도 입력할 수 있도록 프로그램을 변경하라

mode = int(input("섭씨온도는 1, 화씨온도는 2를 입력해주세요"))
temp = float(input("온도를 입력하시오: "))

if (mode==2):
    temp = (temp-32)*5/9

if temp <= 0 : 
    print("물의 상태는 얼음입니다.")
elif temp > 0 and temp < 100 : # 논리 연산자를 사용한다.
    print("물의 상태는 액체입니다.")
else : 
    print("물의 상태는 기체입니다.")

# 4. P 134 도전문제를 프로그램으로 작성하라. random.randrange(6) 이용
# 주사위 던지기 게임으로 변환해보자. 0~5까지의 정수를 랜덤하게 설명할 수 있다. -> 동전던지기 프로그램

import random
print("주사위 던지기 게임을 시작합니다.")
coin = random.randrange(6)
print(coin,"가 나왔습니다")
print("게임이 종료되었습니다.")

# 5. P 136 도전문제 (1), (2)를 프로그램으로 작성하라.
# 1) 사용자가 l또는 left를 입력하면 왼쪽 r, right를 입력하면 오른쪽으로 이동하도록 소스를 변경 -> 
# 2) 사용자가 quit, q를 입력시 프로그램을 종료하도록 변경
# LAB 거북이 제어하기
# l입력 -> 왼쪽으로, r입력 -> 오른쪽으로 이동하는 거북이

import turtle
t = turtle.Turtle()
t.shape("turtle")
t.width(3)

# 거북이를 3배 확대한다. 
t.shapesize(3, 3)

while True: 
 command = input("명령을 입력하시오: ")
 print("pass==001")    
 if command == "l" or command == "left" :  # 사용자가 “l“을 입력하였으면
     t.left(90)
     t.forward(100)
     print("pass==001-1")     
 print("pass==002")      
 if command == "r" or command == "right": # 사용자가 “r“을 입력하였으면
     t.right(90)
     t.forward(100)
     print("pass==002-1")       
 print("pass==003")    
 if command == "q" or command == "quit": # 사용자가 “q“을 입력하였으면
     print("pass==003-1")
     break  # 무한 루프를 빠져나간다. 
 print("pass==004")        
turtle.mainloop()
turtle.bye()


# 6. P 142 도전문제에서 몇가지 경우의 수를 추가한 프로그램을 작성하라. 
# 운세에서 나올 수 있는 몇가지 경우를 더 추가하라

import random
print("행운의 매직볼로 오늘의 운세를 출력합니다. ")
answers = random.randint(1, 8)
if answers == 1:
 print("확실히 이루어집니다.")
elif answers == 2:
 print("좋아 보이네요")
elif answers == 3:
 print("믿으셔도 됩니다.")
elif answers == 4:
 print("저의 생각에는 no입니다.")
elif answers == 5:
 print("복권사세요") 
elif answers == 6:
 print("주식을 풀매수하세요") 
elif answers == 7:
 print("오늘 도박장에 가면 좋은 일이 있을 것입니다") 
elif answers == 8:
 print("아닌 것 같습니다")
else: 
 print("다시 질문해주세요.")

# 7. P 143 도전문제를 프로그램으로 작성하라. - 버거 주문 프로그램 활용
# 패스트푸드 점포에서 흔히 볼 수 있는 자동 주문 기계처럼, 디저트, 음료도 선택할 수 있도록 프로그램을 확장하라.

##
# 이 프로그램은 사용자의 입력을 검증한다. 
#
print("========================")
print("메뉴 1번: 치즈 버거")
print("메뉴 2번: 치킨 버거")
print("메뉴 3번: 불고기 버거")
print("메뉴 4번: 코카콜라")
print("메뉴 5번: 감자튀김")
print("메뉴 6번: 돈가스 버거")
print("========================")
selection = int(input("메뉴를 선택하세요:"))
if selection >= 1 and selection <= 6 :
    print("메뉴 ", selection)
else :
    print("잘못 입력하셨습니다.")


# 8. P 144 도전문제를 프로그램으로 작성하라. -> 축구게임 소스
# 사용자의 입력이 1에서 3 사이인지를 검사하는 문장을 추가하라

import random
computer_choice = random.randint(1, 3)
user_choice = int(input("어디를 수비하시겠어요?(왼쪽: 1, 중앙: 2, 오른쪽: 3)"))
if computer_choice == user_choice:
    print("수비에 성공하셨습니다. ")    
else:
    print("페날티킥이 성공하였습니다. ")
if user_choice > 0 or user_choice > 3:
    print("다시 입력해주세요")

# 9. P 145 도전문제를 프로그램으로 작성하라.
# 위의 프로그램에서 사각형만을 지원하고 있다. 삼각형, 원인 경우에 도형을 그리는 코드를 추가하라

import turtle
t = turtle.Turtle()
t.shape("turtle")
s = turtle.textinput("", "도형을 입력하시오: ")
if s == "사각형" :
 w = int(turtle.textinput("","가로: "))
 h = int(turtle.textinput("","세로: "))
 t.forward(w)
 t.left(90)
 t.forward(h)
 t.left(90)
 t.forward(w)
 t.left(90)
 t.forward(h)
else s == "삼각형" : 
    
else s == "원" :    
 
turtle.mainloop()
turtle.bye() 

# 10. P 146 도전문제를 프로그렘으로 작성하라. 
# 삼각형의 내각을 받아서 내각의 합이 180도 인지를 검사하도록 코드를 추가하라

a = int(input("삼각형의 한 변을 입력하시오: "))
b = int(input("삼각형의 한 변을 입력하시오: "))
c = int(input("삼각형의 한 변을 입력하시오: "))
if (a + b) > c and (b + c) > a and (a + c) > b :
print("올바른 삼각형")
else :
print("올바르지 않은 삼각형")

# 11. P 151 Programming 문제 06번 프로그렘 작성
# 가위바위보 프로그램을 작성하라. 컴퓨터는 사용자에게 알리지 않고 가위,바위,보중에서 임의로 하나 선택.
# 사용자는 3개중 하나를 선택한다. 사용자의 선택이 끝나면 컴퓨터는 누가 무엇을 선택하였고, 승패를 보여준다.

# 12. p 152 Programing 문제 10번 프로그램 작성
#다음과 같이 정의되는 함수의 함수값을 계산하여 보자. 사용자로부터 x값을 받아 함수 값을 계산하여 화면에 출력한다.
# f(x) - x^2-9x+2 (x<=0)
# f(x) - 7x+2 (x>0)
# 이때, 자료형은 실수를 사용한다. x의 3제곱은 x*x*x 수식으로 계산한다.

a = float(input("실수를 입력해주세요"))
if (a<=0):
    result = a^2-9*a+2

if (a>0) :
    result = 7*a+2

print (result)

# Home Work: Programing 문제 13번 프로그램을 작성하라.

year = int(input("연도를 입력하시오. : "))
if (year % 4 == 0) or (year % 100 !=0) or (year % 400 == 0):
    print("윤년입니다")
else : print("윤년이 아닙니다")  
  