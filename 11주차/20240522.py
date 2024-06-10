# 2024-05-16 11장 내장함수, 람다식, 제너레이터, 모듈

"""
⚫ 파이썬에 내장된 내장 함수들을 살펴본다. 
⚫ 람다식을 살펴본다. 
⚫ 제너레이터를 시용하여 반복 가능한 객체를 작성할 수 있다. 
⚫ 모듈의 개념을 살펴본다. 
⚫ 유용한 모듈을 사용할 수 있다.
"""

# Lab: 내장 함수 예제

invitations = ["Kim", "Lee", "Park", "Choi"]
persons = [1, 3, 0, 6]
sum(persons)
10
# 파티에 한 사람이라도 오는 지를 확인해보자. 이것은 any() 함수로 가능하다. 
any(persons)
True
# 이번에는 모든 초대받은 그룹이 전부 오는 지는 확인해보자. 이것은 all() 함수로 가능하다. 
all(persons)
False
# 가장 많이 오는 그룹에는 몇 사람이나 있는지를 알아보자. max()로 가능하다. 
max(persons)

# Lab: 키를 이용한 정렬 예제

class Person(object):
    def __init__(self, name, age):
    self.name = name
    self.age = age
    def __repr__(self):
    return "<이름: %s, 나이: %s>" % (self.name, self.age)
def keyAge(person):
    return person.age
people = [Person("홍길동", 20), Person("김철수", 35), Person("최자영", 38)]
print(sorted(people, key = keyAge))

# Lab: 람다식으로 온도 변환하기

def celsius(T):
    return (5.0/9.0)*(T-32.0)
f_temp = [0, 10, 20, 30, 40, 50]
c_temp = map(celsius, f_temp)
print(list(c_temp))

# Lab: 람다식으로 데이터 처리하기(lambda2.py)

##
# 이 프로그램은 람다식을 이용하여 주문을 처리한다. 
#
orders = [ ["1", "재킷", 5, 120000], 
    ["2", "셔츠", 6, 24000], 
    ["3", "바지", 3, 50000],
    ["4", "코트", 6, 300000] ]
result = list(map(lambda x: (x[0], x[2] * x[3]), orders))
print(result)

# iterator1.py
class MyCounter(object):
    # 생성자 메소드를 정의한다.
    def __init__(self, low, high):
        self.current = low
        self.high = high

    # 이터레이터 객체로서 자신을 반환
    def __iter__(self):
        return self
    
    def __next__(self):
        # current가 high보다 크면 StopIteration 예외 발생
        # current가 high보다 작으면 다음 값을 반환하다.
        if self.current > self.high:
            raise StopIteration
        else:
            self.current += 1
            return self.current - 1

# Lab: 피보나치 이터레이터

class FibIterator:
    def __init__(self, a=1, b=0, maxValue=50):
        self.a = a 
        self.b = b
        self.maxValue = maxValue
    def __iter__(self):
        return self 

    def __next__(self):
        n = self.a + self.b
        if n > self.maxValue:
            raise StopIteration()
            self.a = self.b
            self.b = n
        return n

for i in FibIterator():
    print(i, end=" ")

# Lab: Book 클래스
##
# 이 프로그램은 연산자 중복을 사용하여 Book 객체의 len() 연산을 구현한다. 
#
class Book:
    title = ''
    pages = 0

def __init__(self, title='', pages=0):
# Book 객체끼리의 + 연산을 정의한다. 
    self.title = title
    self.pages = pages

def __str__(self):
    return self.title

def __gt__(self, other):
    return self.pages > other.pages

# Lab: 동전 던기지 게임

import random
myList = [ "head", "tail" ]

while (True):
        response = input("동전 던지기를 계속하시겠습니까?( yes, no) ");
        if response == "yes":
                coin = random.choice(myList)
                print (coin)
        else :
                break
            
"""
 파이썬에는 어떤 객체에도 적용이 가능한 내장 함수가 있다. len()나 max()
와 같은 함수들을 잘 사용하면 프로그래밍이 쉬워진다.
 클래스를 정의할 때 (self)와 (self) 메소드만 정의하면 이터레이터가 된다. 
이터레이터는 for 루프에서 사용할 수 있다.
 연산자 오버로딩은 +나 –와 같은 연산자들을 클래스에 맞추어서 다시 정
의하는 것이다. 연산자에 해당되는 메소드(예를 들어서 __add__(self, 
other))를 클래스 안에서 정의하면 된다.

"""