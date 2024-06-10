# 20240403 5장_함수
# 목표
# 함수의 개념을 학습합니다. 
# 함수를 작성하는 방법을 학습합니다. 
# 함수를 호출하여 사용하여 방법을 학습합니다. 

# 함수 정의
# 함수(function)는 우리가 반복적으로 사용하는 코드를 묶은 것으로
# 프로그램의 빌딩 블록과 같다. 
# 객체(object)는 서로 관련 있는 변수와 함수를 묶는 방법이다. 
# 모듈(module)은 함수나 객체들을 소스 파일 안에 모은 것이다

# 함수 정의

# def function(매개변수1, 매개변수2, ...):
        # 명령문
def get_area(radius):
        area = 3.14 * radius ** 2
        return area
    
# 함수의 특징
# 1. 일단 작성되면 몇 번이라도 호출이 가능하다.
# 서로 다른 인수로 인출될 수 있다.(같은 프로그램 내에서 다른 인수를 활용하여 재사용 가능)
# 7장에서 학습하는 튜플을 통하여 여러 개의 값을 반환할 수 있다.
# 함수의 몸체는 나중에 작성할 수 있다.
# 인터프리트 언어이기 때문에 함수의 순서가 중요하다.
# 함수 내에서는 아직 정의되지 않은 함수를 호출할 수 있다.

# LAB 1. 피자 크기

def main() : 
 print("20cm 피자 2개의 면적:", get_area(20)+get_area(20))
 print("30cm 피자 1개의 면적:", get_area(30))
## 원의 면적을 계산한다.
# @param radius 원의 반지름
# @return 원의 면적
#
def get_area(radius) :
    if radius > 0 :
        area = 3.14*radius**2
    else :
        area = 0
    return area

main()


# 서로 다른 인수들로 호출 될 수 있다

def get_sum(start, end):
    sum = 0
    for i in range(start, end+1):
        sum += i
    return sum


# 1과 10이 get_sum()의 인수가 된다. 
x = get_sum(1, 10) 


# 1과 20이 get_sum()의 인수가 된다. 
y = get_sum(1, 20);

# 디폴트 함수 : 파이썬에서는 함수의 매개 변수가 기본값을 가질 수 있다. 
# 이것을 디폴트 인수(default argument)라고 한다

def greet(name, msg="별일없죠?"):
        print("안녕 ", name + ', ' + msg)

greet("영희")

# 파이썬에서는 가변 인수도 허용한다.

def varfunc(*args ): 
        print (args)
        
print("하나의 값으로 호출")
varfunc(10)

print("여러 개의 값으로 호출")
varfunc(10, 20, 30)

# 매개 변수 이름 앞에 이중 별표(**)를 사용하여 가변 길이 키워드 인수를 나타낸다.
# 인수는 딕셔너리 형태로 전달된다

def myfunc(**kwargs):
        result = ""
        for arg in kwargs.values():
            result += arg
        return result

print(myfunc(a="Hi!", b="Mr.", c="Kim"))


# Lab : 여러개의 값 변환

##
# 이 프로그램은 사용자로부터 이름과 나이를 받아서 다시 출력한다. 
#
def get_info():
        name = input("이름:")
        age = int(input("나이:"))
        return name, age # 2개의 값을 반환한다. 
 
st_name, st_age = get_info() # 반환된 값을 풀어서 변수에 저장한다.
print("이름은 ", st_name, "이고 나이는 ", st_age, "살입니다.")

# Lab: 사각형을 그리는 함수 작성하기

import turtle 
t = turtle.Turtle()
t.shape("turtle")

def square(length): # length는 한변의 길이
    t.down()
    for i in range(4):
        t.forward(length)
        t.left(90)
    t.up()
    
square(100); # square() 함수를 호출한다. 
t.forward(120)
square(100);
t.forward(120)
square(100);

turtle.mainloop()
turtle.bye() 

# Lab: 구조화 프로그래밍 실습

def menu() :
    print("1. 섭씨 온도->화씨 온도")
    print("2. 화씨 온도->섭씨 온도")
    print("3. 종료")
    selection = int(input("메뉴를 선택하세요: "))
    return selection
def ctof(c) :
    temp = c*9.0/5.0 + 32
    return temp

def ftoc(f) :
    temp = (f-32.0)*5.0/9.0
    return temp

def input_f() :
    f = float(input("화씨 온도를 입력하시오: "))
    return f

def input_c() :
 c = float(input("섭씨 온도를 입력하시오: "))
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

# 팩토리얼 계산 프로그램

def factorial(n):
    if n == 1 :
        return(1)
    else:
        return n * factorial(n-1)
    
n = eval(input("정수를 입력하시오:"))
print(n, "!= ", factorial(n))

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

# 지역 변수는 함수마다 동일한 이름을 사용할 수 있다.

def myfunc() :
    x = 200
    print(x)
def main() :
    x = 100
    print(x)
myfunc()
main()

# 함수 안에서 전역 변수 변경하기

gx = 100
def myfunc() : 
    gx = 200 # 변경되지 않는다! -> 함수, 안에서 변수에 값을 저장하면 새로운 지역 변수가 생성된다.
    print(gx)
myfunc()
print(gx)

# Lab: 함수 그리기

import turtle 
t = turtle.Turtle()
t.shape("turtle")
t.speed(0)

def f(x):
    return x**2+1

t.goto(200, 0)
t.goto(0, 0)
t.goto(0, 200)
t.goto(0, 0)

for x in range(150):
        t.goto(x, int(0.01*f(x)))
        
turtle.mainloop()
turtle.bye()

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

# 이번 장에서 배운 것

# 함수가 무엇인지를 학습하였다. 
#인수와 매개변수가 무엇인지를 학습하였다. 
#어떻게 함수로 인수를 전달할 수 있는지를 학습하였다.
#여러 개의 인수를 함수로 전달하는 방법을 학습하였다. 
#함수가 값을 반환하는 방법을 학습하였다.
#지역변수와 전역변수의 차이점에 대하여 학습하였다.
#global 키워드를 사용하여서 함수 안에서 전역변수를 사용하는 방법을 학습하였다.

