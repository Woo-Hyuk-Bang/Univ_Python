#2024-03-12 python class
# chapter 1.

#1) 문자열 출력하기
＂나의 ＂ + ＂고양이＂

#2) 문자열 반족하기
"Hello" * 10


#code

print("Hello World!");

x = input('x값을 입력하세요');
y = input('y값을 입력하세요');
z = x+y;
print(z); #결과는 문자열이기 때문에 정수형으로 바꿔줘야 합이 나온다.

#2) 정수형 입력
x = 100;
y = 200;
print(x,"와 ", y, "의 합=",x+y);


# lab 1. print 실습
print("파이썬에 오신 것을 환영합니다.")
print("파이썬은 쉽습니다.")
print("파이썬으로 빅데이터, 인공지능 프로그램을 작성할 수 있습니다.")

# lab 2. 간단한 계산
print("2+3=", 2+3)
print("2-3=", 2-3)
print("2*3=", 2*3)
print("2/3=", 2/3)

# 터틀그래픽 시작
import turtle # (1)

t = turtle.Turtle() # (2)
t.shape("turtle") # (3)

t.forward(100) # (4)
t.left(90) # (5)
t.forward(50)

turtle.mainloop() # (6)
turtle.bye()

# LAB 3. 삼각형 그리기
import turtle
t = turtle.Turtle()

t.shape("turtle")
t.forward(100)
t.left(120)
t.forward(100)
t.left(120)
t.forward(100)

turtle.mainloop()
turtle.bye()


# 정리노트
# 인터프리터 모드는 코드가 복잡해지면 번거롭게 된다.
# 스파이더에서 대화형 모드와 스크립트 모드가 존재한다.
# 대화형 모드(interactive mode): 콘솔에서 문장을 한 줄씩 입력하여 실행
# 스크립트 모드(script mode): 파일을 만들어서 저장한 후에 파이썬 인터프리터가 이 파일을 읽어서 한 번에 전부 실행
# 프로그램은 컴퓨터에 내리는 _____로 이루어지는 작업 지시서이다. 
# 고급 언어는 컴퓨터가 이해할 수 있는 언어이다. 
# 다양한 종류의 프로그래밍 언어가 있고 파이썬도 프로그래밍 언어의 일종이다. 
# 파이썬으로 프로그램을 작성하기 위한 개발 환경인 _____는  https://www.anaconda.com/distribution/ 웹사이트에서 다운받아서 설치할 수 있다. 
# IPython 콘솔에서는 프롬프트 다음에 코드를 입력하고 󰎠를 누르면 코드가 실행된다. 
# 산술 계산을 하는 파이썬 연산자에는 +, -, *, /가 있다. 
# _____는 화면에 문자열이나 계산 결과를 출력할 때 사용하는 함수이다. 
# 스크립트 모드를 사용하면 코드를 파일에 저장하였다가 한꺼번에 실행할 수 있다. 

