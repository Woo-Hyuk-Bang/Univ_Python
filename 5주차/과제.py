# -*- coding: utf-8 -*-
"""
Created on Wed Mar 27 09:37:50 2024

@author: User
"""

#[도전문제]
#
#1. p184  도전문제:  2개의 주사위를 컴푸터가 1,000 번 던져서(random number 활용) 두 수의 합이 6이 나오는 횟수를 세는 프로그램을 작성하라.
#
#    (이론적 적인 확률 5/36 와 비교하여 보라.)  


import random

trial = 1000
x = random.randint(1,6)
y = random.randint(1,6)
count = 0

for count in range(trial) :
    if x + y == 6:
        count += 1

rate = count / trial
rate_theory = 5 / 36

if rate == rate_theory:
    print("시도결과 : %d",rate)
    print("이론상 수치 : %d",rate_theory)        
    print("이론상으로 일치하였습니다")
else :
    print("시도결과 : %d",rate)
    print("이론상 수치 : %d",rate_theory)    
    print("이론상 수치와 맞지 않습니다")


#2. p188 도전문제: 1부터 100사이의 소수를 구하는 프로그램을 작성하라.

N_PRIMES = 100
number = 2
count = 0

while number < N_PRIMES :
     divisor = 2
     prime = True
     

     while divisor < number :
        if number % divisor == 0:
            prime = False
            break;
        divisor += 1
     if prime :
        count += 1
        print(number, end=" ")
     number += 1

#3. p190 도전문제:  phi =  3 + 4/(2*3*4) - 4/(4*5*6) + 4/(6*7*8) - 4/(8*9*10) + ....  

#cal_pi.py, 파이값 계산

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

#4. p194 도전문제: 도박사 문제에서 돈을 딸 확룰을 20%로 수정하여 프로그램을 작성하라.

#gambler.py 도박사 프로그램

import random

initial_money = 50
goal = 250
wins = 0

for i in range(100) :
    cash = initial_money
    while cash > 0 and cash < goal :
        number = random.randint(1,5)
        if number == 1:
            cash = cash + 1
        else :
            cash = cash - 1
    if cash == goal : wins = wins + 1

print("초기 금액 %d" % initial_money)
print("목표 금액 %d" % goal)
print("100번 중에서 %d번 성공" % wins)   
    
#[Programming 문제]

#5.   p198 3번 - 1부터 100사이 모든 3의 배수의 합을 계산하여 출력하는 프로그램을 반복구조로 작성하라

x = int(input("시작할 수를 입력해주세요: "))
y = int(input("마지막 수를 입력해주세요: "))
result = 0

for i in range(x, y+1):
    if i % 3 == 0:
        result += i

print("%d부터 %d사이의 모든 3의 배수의 합은 %d입니다." % (x, y, result))

#6.   p198 4번 사용자가 입력한 정수의 모든 약수를 화면에 출력하는 프로그램을 작성하라

num = int(input("정수를 입력하세요: "))

print("약수:", end=" ")

# 1부터 입력된 정수까지 반복하여 약수를 찾음
for i in range(1, num + 1):
    if num % i == 0:
        print(i, end=" ")

#7.   p199 8번 while 루프를 이용해서 n^2 > 500인 n 중에서 가장 작은 n을 찾는 프로그램

n = 1

while n**2 <= 500:
    n += 1

print("가장 작은 최소값은", n, "입니다.")

#8.   p199 10번 1^2 + 2^2 + 3^3 + 4^4

x = int(input("n의 값을 입력하시오"))
result = 0

for i in range(1, x) :
    result = result +  i * i
    
print("계산값은", result, "입니다")    

#9.   p200 13번 - 피보나치

n = int(input("몇 번째 항까지 구할까요? "))

# 첫 번째와 두 번째 항은 미리 정의
fibo = [0, 1]

# 피보나치 수열 계산
for i in range(2, n+1):
    next_fib = fibo[i-1] + fibo[i-2]
    fibo.append(next_fib)

# 피보나치 수열 출력
print("피보나치 수열:", end=" ")
for num in fibo:
    print(num, end=" ")

#10. p200 14번 2부터 20사이의 모든 소수를 찾는 프로그램을 작성하라

first = int(input("첫번째 수를 입력하세요 :"))
last = int(input("마지막 수를 입력하세요 :"))

number = 2
count = 0

while number < last :
     divisor = 2
     prime = True
     
     while divisor < number :
        if number % divisor == 0:
            prime = False
            break;
        divisor += 1
     if prime :
        count += 1
        print(number, end=" ")
     number += 1

#11. p200 15번

sum = 0

# 분자와 분모 초기값 설정
x = 1
y = 3

# 분자가 99가 될 때까지 반복
while x <= 99:
    sum += x / y
    x += 2
    y += 2

print(format(sum, ".14f"))


#12. p201 17번

for i in range(0, 10):  # 1부터 9까지 범위
    if (i % 3 == 0 and i % 5 == 0):  # 3과 5의 공배수인 경우
        print("fizzbuzz")
    elif (i % 3 == 0):  # 3의 배수인 경우
        print("fizz")
    elif (i % 5 == 0):  # 5의 배수인 경우
        print("buzz")
    else:
        print("*")  # 위 조건에 해당하지 않는 경우