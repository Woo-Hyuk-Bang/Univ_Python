## 조건문
## 제어문, if-else
## 관계연산자, 논리연산자
## 블록의 개념
## 중첩, 연속 if-else

#LAB : 산술 퀴즈 프로그램

import random

x = random.randint(1,100)
y = random.randint(1,100)

answer = int(input(f"{x} + {y} = "))

flag = (answer == (x+y)) # true or false
print(flag)

# 조건 연산자
# max_value = (x if x >y else y)
# x>y가 참일경우 x, 아닐경우, y
# shipping_cost = ( 0 if price >= 20000 else 3000)
# = price >= 20000일 경우, 0, 아니면 3000



# 논리 연산자 and, or, xor etc
# 드모르간 법칙
# p and q -> ~p or ~ q 
# p or q -> ~p and ~q

# LAB 물의 상태출력하기

#
# 이 프로그램은 온도에 따른 물의 상태를 출력한다.
#
temp = float(input("온도를 입력하시오: "))
if temp <= 0 : 
    print("물의 상태는 얼음입니다.")
elif temp > 0 and temp < 100 : # 논리 연산자를 사용한다.
    print("물의 상태는 액체입니다.")
else : 
    print("물의 상태는 기체입니다.")

# LAB 동전 던지기 게임

import random
print("동전 던지기 게임을 시작합니다.")
coin = random.randrange(2)
if coin == 0 :
    print("앞면입니다.")
else :
    print("뒷면입니다.")
    print("게임이 종료되었습니다.")

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
 if command == "l": # 사용자가 “l“을 입력하였으면
     t.left(90)
     t.forward(100)
 if command == "r": # 사용자가 “r“을 입력하였으면
     t.right(90)
     t.forward(100)
 if command == "q": # 사용자가 “q“을 입력하였으면
     break # 무한 루프를 빠져나간다. 

turtle.mainloop()
turtle.bye()

# 중첩 if문
# if 문 안에 또다른 if 문이 들어감
# 배송비 계산 프로그램

# 사용자로부터 상품의 가격을 입력받는다. 
country = input("배송지(현재는 korea와 us만 가능): ")
price = int(input("상품의 가격: "))

# 배송비를 결정한다. 
if country == "korea" :
        if price >= 20000 :
            shipping_cost = 0
        else :
            shipping_cost = 3000
else :
        if price >= 100000 :
            shipping_cost = 0
        else :
            shipping_cost = 8000
# 배송비를 출력한다. 
print("배송비 = ", shipping_cost)



# 학점 결정 예제 -> 연속 if문 ,elif

# 성적을 받아서 학점을 결정하는 프로그램
# score가 80 이상, 90 미만인 경우
score = int(input("성적을 입력하시오: "))
if score >= 90 : print("학점 A")
elif score >= 80 : print("학점 B")
elif score >= 70 : print("학점 C")
elif score >= 60 : print("학점 D")
else : print("학점 F")


# LAB 축구게임

##
# 이 프로그램은 축구 게임을 구현한다. 
#
import random
computer_choice = random.randint(1, 3)
user_choice = input("어디를 수비하시겠어요?(왼쪽: 1, 중앙: 2, 오른쪽: 3)")
if computer_choice == user_choice:
    print("수비에 성공하셨습니다. ")
else:
    print("페날티킥이 성공하였습니다. ")



# LAB: 도형 그리기
# 터틀 그래픽을 이용하여 도형을 그리기

##
# 이 프로그램은 사용자가 원하는 도형을 화면에 그린다. 
#
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
turtle.mainloop()
turtle.bye() 

# 올바른 삼각형 구분

a = int(input("삼각형의 한 변을 입력하시오: "))
b = int(input("삼각형의 한 변을 입력하시오: "))
c = int(input("삼각형의 한 변을 입력하시오: "))
if (a + b) > c and (b + c) > a and (a + c) > b :
print("올바른 삼각형")
else :
print("올바르지 않은 삼각형")

## 운세 프로그램
##
# 이 프로그램은 오늘의 운세를 출력한다. 
#
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
else: 
 print("다시 질문해주세요.")

## 햄버거 문제
##
# 이 프로그램은 사용자의 입력을 검증한다. 
#
print("========================")
print("메뉴 1번: 치즈 버거")
print("메뉴 2번: 치킨 버거")
print("메뉴 3번: 불고기 버거")
print("========================")
selection = int(input("메뉴를 선택하세요:"))
if selection >= 1 and selection <= 3 :
print("메뉴 ", selection)
else :
print("잘못 입력하셨습니다.")



# 문장의 실행 순서를 바꾸는 2가지 종류의 제어문은 조건문과 반복문이다. 
# if-else 문의 구조를 주석으로 설명하여 보시오.
# if( 조건식 )
# 문장1;
#//__________________________________
# else 
# 문장2;
#//__________________________________
# 조건에 따라서 실행되어야 하는 문장이 두개 이상이면 이들 문장을 들여쓰기 한다. 이것을 복합문(블록)이라고 한다. 
# if-else 문 안에 다른 if-else 문이 포함될 수 있다.
