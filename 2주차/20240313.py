#2024-03-13 python class
#chapter 2

# 예제_ 두 수의 합 계산하기

x = 100			# 변수 x를 생성하고 100을 저장한다.
y = 200			# 변수 y를 생성하고 200을 저장한다.
sum = x + y		# 변수 sum을 생성하고 x+y를 저장한다.
print("합은", sum)

# 예제_ 원의 면적 계산하기
# 알고리즘
#STEP #1. 사용자로부터 원의 반지름을 입력받는다. 
#STEP #2. 공식을 적용하여 면적을 계산한다.
#			area = radius * radius * p
#STEP #3. 면적을 화면에 출력한다. 

# 변수 radius에 값을 저장한다. 
radius = 10 	

# 공식을 적용하여 면적을 계산한다 
area = 3.14 * radius * radius

# 면적을 화면에 출력한다. 
print("반지름", radius, "인 원의 면적=", area)

# 변수는 어디에 유용한가?
import turtle
t = turtle.Turtle()
t.shape("turtle")

radius = 100
t.circle(radius) # 반지름이 100인 원이 그려 진다.
t.fd(30)
t.circle(radius) # 반지름이 100인 원이 그려 진다.
t.fd(30)
t.circle(radius) # 반지름이 100인 원이 그려 진다.

turtle.mainloop()
turtle.bye()	

# 파이썬에서는 변수에 어떤 자료형도 저장 가능, but 바람직하진 않음

>>> radius = 10
>>> radius = 10.003
>>> radius = "Unknown"

# type형
>>> type(12.30)		# float 형 
<class 'float'>

>>> type("hello")		# str(문자열) 형 
<class 'str'>


# LAB 2. 별까지의 거리 계산하기

##
#	이 프로그램은 프록시마 센토리까지 빛이 가는 시간을 계산한다. 
#
speed = 300000	.0			# 빛의 속도
distance = 40000000000000.0		# 거리

secs = distance / speed		# 걸리는 시간, 단위는 초	
light_year = secs / (60.0*60.0*24.0*365.0)	# 광년으로 변환

print(light_year, "광년")

# LAB 3. 원기둥의 부피 계산
##
#	이 프로그램은 원기둥의 부피를 계산한다. 
#
# 원주율을 나타내는 상수를 정의한다. 
PI = 3.14

# 변수를 정의한다. 
radius = 5
height = 10

# 부피를 계산한다. 
volume = PI * radius * radius * height

# 결과를 출력한다. 
print("반지름=", radius, "높이=", height, "원기둥의 부피=", volume)

# 할당 연산
x = y = z = 0		
x, y, z = 10, 20, 30	 # 한번에 여러 개의 변수 초기화
x, y = y, x		# x와 y의 값을 서로 교환한다. 

# 복합 연산자
x = 1000
print("초깃값 x=", x)
x += 2;
print("x += 2 후의 x=", x)
x -= 2;
print("x -= 2 후의 x=", x)

#LAB 4. 복리 계산
#code
init_money = 24
interest = 0.08
years = 382
print(init_money*(1+interest)**years)

#문자열의 함수

name = "Harry Parter"
lower_name = name.lower() 			# 'harry parter'

name = "Harry Parter"
new_name = name.replace("Parter", "Porter")	# Harry Porter

#LAB 5. 로봇기자 만들기
#code

print("Hello World!");
stadium = input("경기장은 어디입니까?\n")
winner = input("이긴 팀은 어디입니까?\n")
loser = input("?\n")
vip = input("경기장은 어디입니까?\n")
score = input("경기장은 어디입니까?\n")
x = input('x값을 입력하세요');
y = input('y값을 입력하세요');
z = x+y;
print(z); #결과는 문자열이기 때문에 정수형으로 바꿔줘야 합이 나온다.

#LAB 6. 대화하는 프로그램 만들기
##
#	이 프로그램은 사용자와 친근하게 대화한다. 
#
print("안녕하세요?")
name = input("이름이 어떻게 되시나요? ")
print("만나서 반갑습니다. " + name + "씨")

print("이름의 길이는 다음과 같군요:", len(name))

age = int(input("나이가 어떻게 되나요? "))
print("내년이면 "+ str(age+1) + "이 되시는군요.")

#LAB 7. 사각형 그리기
##
#	이 프로그램은 사용자로부터 크기를 받아서 사각형을 그린다.  
#
import turtle
t = turtle.Turtle()
t.shape("turtle")

# 사용자로부터 사각형의 크기를 받아서 size라는 변수에 저장한다. 
size = int(input("사각형의 크기는 얼마로 할까요? "))

# 사각형을 다음과 같은 코드로 그린다. 이때 변수 size를 사용하자. 
t.forward(size)	# size 만큼 거북이를 전진시킨다. 
t.right(90)		# 거북이를 오른쪽으로 90도 회전시킨다. 
t.forward(size)
t.right(90)
t.forward(size)
t.right(90)
t.forward(size)

turtle.mainloop()
turtle.bye()

#LAB 8. BMI 계산하기
##
#	이 프로그램은 BMI를 계산한다. 
#
weight = float(input("몸무게를 kg 단위로 입력하시오: "))
height = float(input("키를 미터 단위로 입력하시오: "))

bmi = (weight / (height**2)) 
print("당신의 BMI=",  bmi)

#LAB 9. 부피 계산하기
##
#	이 프로그램은  구의 부피를 계산한다. 
#

# 사용자에게 구의 반지름을 입력하도록 한다. 구의 반지름을 문자열에서 실수로 변환한다. 
r = float(input("반지름을 입력하시오: "))

# 구의 부피를 공식을 이용하여 계산한다. 
volume = (4.0/3.0) * 3.141592 * r**3

# 구의 부피를 화면에 출력한다. 
print("구의 부피=",volume)

#LAB 10. 자동판매기 프로그램
##
#	이 프로그램은 자판기에서 거스름돈을 계산한다.  
#
itemPrice = int(input("물건값을 입력하시오: "))
note = int(input("1000원 지폐개수: "))
coin500 = int(input("500원 동전개수: "))
coin100 = int(input("100원 동전개수: "))

change = note*1000 + coin500*500 + coin100*100 - itemPrice

# 거스름돈(500원 동전 개수)을 계산한다. 
nCoin500 = change//500
change = change%500

# 거스름돈(100원 동전 개수)을 계산한다. 
nCoin100 = change//100
change = change%100

# 거스름돈(10원 동전 개수)을 계산한다. 
nCoin10 = change//10
change = change%10

# 거스름돈(1원 동전 개수)을 계산한다. 
nCoin1 = change

print("500원=", nCoin500, "100원=", nCoin100, "10원=", nCoin10, "1원=", nCoin1) 

# 2장 정리
# 변수는 값을 저장하는 상자와 같은 것으로 저장된 값은 나중에 유용하게 사용될 수 있다. 
# 문자열은 큰따옴표(“...”)나 작은 따옴표(‘...’)을 사용할 수 있다. 
# 덧셈, 뺄셈, 곱셈, 나눗셈을 위하여 +, -, *, / 기호를 사용한다. 
# 지수 연산자는 _**__이다. 
# 나눗셈에서 정수로 몫을 계산하려면 // 연산자를 사용한다. 
# 나눗셈에서 나머지를 계산하려면 % 연산자를 사용한다. 
# 우선순위가 높은 연산자가 먼저 계산된다. 
# *와 /가 +와 –보다 우선순위가 높다. 
# 연산자의 우선 순서를 변경하려면 괄호를 사용한다. 
# input() 함수를 이용하여 사용자로부터 문자열을 받을 수 있다. 
# 문자열을 정수로 변경하려면 __int__함수를 사용한다. 
# 문자열을 실수로 변경하려면 float() 함수를 사용한다. 
# 정수나 실수를 문자열로 변경하려면 str()를 사용한다. 
# "\n"은 줄바꿈을 나타내는 특수 문자열이다. 
