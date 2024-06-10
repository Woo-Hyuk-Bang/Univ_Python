#   반복문의 필요성을 이해한다. 
# for 문을 사용하여 정해진 횟수만큼 반복하는 방법을 학습한다. 
#   range() 함수를 이해하고 사용할 수 있다. 
# while 문을 사용하여 조건으로 반복하는 방법을 학습한다. 
# 중첩 반복문의 개념을 이해한다. 
# 무한 루프가 사용되는 환경을 이해한다.
#   횟수 반복(for 문): 정해진 횟수만큼 반복한다.(횟수를 알고 있을 때 사용)
# 조건 반복(while 문): 특정한 조건이 성립되는 동안 반복한다.

# 리스트 출력, # 인덱스는 0부터 시작한다.
list = [] # 공백 리스트를 생성한다. 
list.append(1) # 리스트에 정수 1을 추가한다. 
list.append(2) # 리스트에 정수 2을 추가한다. 
list.append(6) # 리스트에 정수 6을 추가한다. 
list.append(3) # 리스트에 정수 3을 추가한다. 
print(list) # 리스트를 출력한다. 

# 이때, 음수로도 인덱스를 표현하는데, 이때, 인덱스 0은 해당 리스트인덱스에서
# 가장 작은 값을 가진다 예) 개체수가 4일때, -4,-3,-2,-1로 인덱스를 가진다
# 즉, 가장 마지막 리스트가 -1을 가지며 가장 큰 값의 인덱스를 가진다.

slist = [ "영어", "수학", "사회", "과학" ]
slist[-1] = "컴퓨터"
print(slist)  # '과학'이 '컴퓨터'로 변경

# for 변수 in 리스트

for i in [1,2,3,4,5]:
    print("방문을 환영합니다")
    
for i in range(1, 6, 1):
    print(i, end=" ")

for i in range(10, 0, -1):
    print(i, end=" ")
    
# 팩토리얼 계산

n = int(input("정수를 입력하시오: "))
fact = 1
for i in range(1, n+1):
    fact = fact * i
print(n, "!은", fact, "이다.")

# n각형 그리기

import turtle
t = turtle.Turtle()
t.shape("turtle")
s = turtle.textinput("", "몇각형을 원하시나요?:")
n=int(s)
for i in range(n):
        t.forward(100)
        t.left(360/n)
turtle.mainloop()
turtle.bye()

# 방정식의 해 구하기

COUNT = 100
START = 1.0
END = 2.0
for i in range(COUNT):
    x = START + i*((END-START)/COUNT)
    f = (x**2 -x -1)
    if abs(f-0.0) < 0.01 :
        print("방정식의 해는 ", x)

# 투자금, 이자액
TARGET = 2000 # 목표 금액
money = 1000 # 초기 자금
year = 0 # 연도
rate = 0.07 # 이자율
# 현재 금액이 목표 금액보다 작으면 반복한다. 
while money < TARGET :
    money = money + money * rate
    year = year + 1
print(year, "년")

# 1부터 10까지 합 구하기
# 제어 변수를 선언한다. 
i = 1
sum = 0
# i 값이 10보다 작으면 반복
while i <= 10 :
    sum = sum + i
    i = i + 1
print("합계는", sum)

# else문
i = 0
while i < 3:
    print("루프 안쪽")
    i = i + 1
else:
    print("else 부분")

# 이 예제는 프로그램이 가지고 있는 정수를 사용자가 알아맞히는 
# 게임이다. 사용자가 답을 제시하면 프로그램은 자신이 저장한 정수와
# 비교하여 제시된 정수가 더 높은지 낮은지 만을 알려준다.

import random
tries = 0 # 시도 횟수
guess = 0 # 사용자의 추측값
answer = random.randint(1, 100) # 1과 100사이의 난수
print("1부터 100 사이의 숫자를 맞추시오")
while guess != answer:
    guess = int(input("숫자를 입력하시오: "))
    tries = tries + 1
    if guess < answer:
        print("너무 낮음!")
    elif guess > answer:
        print("너무 높음!")
if guess == answer:
 print("축하합니다. 시도횟수=", tries)
 print("정답은 ", answer) 

# 초등학생들을 위하여 산수 문제를 발생시키는 프로그램을 작성해보자.
# 한 번이라도 틀리면 반복을 중단한다
##
# 이 프로그램은 산수 문제를 출제한다. 
#
import random
flag = True
while flag:
 x = random.randint(1, 100)
 y = random.randint(1, 100)
 answer = int(input(f"{x} + {y} = "))
if answer == x + y:
    print("잘했어요!!")
else:
    print("틀렸어요. 하지만 다음번에는 잘할 수 있죠?")
flag = False

# 패스워드
password = ""
while password != "pythonisfun":
    password = input("암호를 입력하시오: ")
print("로그인 성공")

## 별반복

for y in range(5) :
    for x in range(10) :
        print("*", end="" )
    print("")

for y in range(1, 6) :
        for x in range(y) :
            print("*", end=" " )
        print("")

adj = ["small", "medium", "large"]
nouns = ["apple", "banana", "grape"]
for x in adj:
    for y in nouns:
        print(x, y)
        
##
# 이 프로그램은 주사위 2개의 합이 6인 경우를 전부 출력한다. 
#
for a in range(1, 7) :
        for b in range(1, 7) :
                if a + b == 6 :
                            print(f"첫 번째 주사위={a} 두 번째 주사위={b}" )


# 2부터 시작하여 50개의 소수를 찾는 프로그램을 작성해보자.
# 집중분석 코드!

N_PRIMES = 50 # 찾아야 하는 소수의 개수
number = 2 # 2부터 시작한다.
count = 0
while count < N_PRIMES :
    divisor = 2 # 나누는 수는 2부터 시작하여 하나씩 증가한다.
    prime = True
    while divisor < number :
        if number % divisor == 0: # 나누어지면 소수가 아니다.
                prime = False
                break;
        divisor += 1
    if prime: # 소수이면 소수 개수를 증가하고 출력한다.
        count += 1
        print(number, end=" ")
    number += 1 # 다음 수로 간다.

# 파이를 계산하는 것은 무척 시간이 많이 걸리는 작업으로 주로 수퍼
# 컴퓨터의 성능을 시험하는 용도로 사용된다. 지금은 컴퓨터의 도움
# 으로 10조개의 자리수까지 계산할수 있다. 파이를 계산하는 가장 고
# 전적인 방법은 Gregory-Leibniz 무한 수열을 이용하는 것이다.

divisor = 1.0
divident = 4.0
sum = 0.0
loop_count = int(input("반복횟수:"))
while(loop_count > 0) :
        sum = sum + divident / divisor
        divident = -1.0 * divident
        divisor = divisor + 2
        loop_count = loop_count - 1;
print("Pi = %f" % sum)

# 거북이 랜덤 워크
##
# 이 프로그램은 터틀 그래픽으로 랜덤 워크를 구현한다. 
#
import turtle
import random
t = turtle.Turtle()
t.shape("turtle")

for i in range(30):
 length = random.randint(1, 100)
 t.forward(length)
 angle = random.randint(-180, 180)
 t.right(angle) 
 
turtle.mainloop()
turtle.bye()

# 거북이 스파이럴 그리기

import turtle

t = turtle.Turtle()
t.shape("turtle")

for i in range(200):
        t.forward(2+i/4) # 반복에 따라 조금씩 증가시킨다. 
        t.left(30-i/12) # 반복에 따라 조금씩 감소시킨다. 
        
turtle.mainloop()
turtle.bye()

# 도박상의 확률
# 집중 코드 분석

import random
initial_money = 50
goal = 250
wins = 0

for i in range(100) : # 라스베가스에 100번 간다.
 cash = initial_money
 while cash > 0 and cash < goal : # 돈이 0이거나 250불을 따면 반복 중단
     number = random.randint(1, 2)
     if number == 1 : # 딸 확률 0.5
         cash = cash + 1 # $1을 딴다.
     else :
         cash = cash - 1 # $1을 잃는다.
    if cash == goal : wins = wins + 1 
 
print("초기 금액 $%d" % initial_money)
print("목표 금액 $%d" % goal)
print("100번 중에서 %d번 성공" % wins) 

#  문장들을 반복 실행하려면 for 문이나 while 문을 사용한다. 
# 반복 실행되는 문장들을 들여쓰기 하여야 한다. 
# for 문은 반복 회수를 정해져있을 때 유용하다. 
# while 문은 반복 조건이 정해져 있을 때 유용하다. 
# 반복문의 초입에서 조건식은 검사된다. 

