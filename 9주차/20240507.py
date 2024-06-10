# 2024-05-01 파이썬 - 객체와 클래스
"""
 객체지향 프로그래밍을 간단히 이해합니다.
 객체의 개념을 이해합니다.
 객체와 클래스의 관계를 이해합니다.
 객체를 활용하여 프로그램을 작성해봅니다.

절차 지향 프로그래밍(proceduralprogramming)은 프로시저(procedure)를 
     기반으로 하는 프로그래밍 방법이다. 
객체 지향 프로그래밍(object-orientedprogramming)은
    데이터와 함수를 하나의 덩어리로 묶어서 생각하는 방법이다
    
 객체에 대한 설계도를 클래스(class)라고 한다. 
   클래스란 특정한 종류의 객체들을 찍어내는 형틀(template) 또는 
   청사진(blueprint)이라고도 할 수 있다. 
 클래스로부터 만들어지는 객체를 그 클래스의 인스턴스(instance)라고 한다.    

    거푸집을 클래스, 거푸집으로 만들어진 대량생산품 청동검 하나하나를 인스턴스

"""

# LAB 1. 원의 면적 구하기(클래스 활용) p.378

import math

# Circle 클래스를 정의한다. 
class Circle:
    def __init__(self, radius = 0):
        self.radius = radius
    def getArea(self):
        return math.pi * self.radius * self.radius
    def getPerimeter(self):
        return 2 * math.pi * self.radius
    
# Circle 객체를 생성한다. 
c = Circle(10)
print("원의 면적", c.getArea())
print("원의 면적", c.getPerimeter())

# LAB 2. 자동차 클래스 정의

class Car:
    def __init__(self, speed, color, model):
        self.speed = speed
        self.color = color
        self.model = model
    def drive(self):
        self.speed = 60

myCar = Car(0, "blue", "E-class")
print("자동차 객체를 생성하였습니다.")
print("자동차의 속도는", myCar.speed)
print("자동차의 색상은", myCar.color)
print("자동차의 모델은", myCar.model)
myCar.drive()
print("자동차의 속도는", myCar.speed)

'''
 인스턴스 변수값을 반환하는 접근자(getters)
 인스턴스 변수값을 설정하는 설정자(setters)
'''

# LAB 3. 접근자와 설정자 p.383

class Student:
    def __init__(self, name=None, age=0):
        self.__name = name
        self.__age = age
        
    def getAge(self):
        return self.__age
    
    def getName(self):
        return self.__name

    def setAge(self, age):
        self.__age=age

    def setName(self, name):
        self.__name=name
        
obj=Student("Hong", 20)
obj.getName()

# LAB 3. 은행계좌 p.384

class BankAccount:
    def __init__(self):
        self.__balance = 0  'private 인스턴스 변수
        
    def withdraw(self, amount):
        self.__balance -= amount
        print("통장에 ", amount, "가 입금되었음")
        return self.__balance
    
    def deposit(self, amount):
        self.__balance += amount
        print("통장에서 ", amount, "가 출금되었음")
        return self.__balance
    
a = BankAccount()
a.deposit(100)
a.withdraw(10)

# dog.py p.392

class Dog:
    kind = "bulldog"
    def __init__(self, name, age=0):
        self.name = name
        self.age = age
        
a = Dog("Baduk",2)
b = Dog("Marry",3)

print(a.kind)
print(b.kind)
print(Dog.kind)

print(a.name)
print(b.name)

# 특수메소드
# 파이썬에는 연산자(+,-,*,/)에 관련된 특수 메소드가 있다.
# 이들 메소드는 우리가 객체에 대하여 연산자와 같은 연산을 적용하면 자동으로 호출

class Circle:
        ...
        def __eq__(self, other):
                return self.radius == other.radius
c1 = Circle(10)
c2 = Circle(10)
if c1 == c2:
        print("원의 반지름은 동일합니다. ")

# vector.py 벡터를 클래스로 모델링

class Vector2D :
 def __init__(self, x, y):
 self.x = x
 self.y = y
 def __add__(self, other):
 return Vector2D(self.x + other.x, self.y + other.y)
 def __sub__(self, other):
 return Vector2D(self.x - other.x, self.y - other.y)
 def __eq__(self, other):
 return self.x == other.x and self.y == other.y
 def __str__(self):
 return '(%g, %g)' % (self.x, self.y)
u = Vector2D(0,1)
v = Vector2D(1,0)
w = Vector2D(1,1)
a = u + v
print( a)

# LAB 4. 주사위

from random import randint
class Dice :
 def __init__(self, x, y) :
 self._x = x
 self._y = y
 self._size = 30
 self._value = 1
 def read_dice(self) :
 return self._value
 def print_dice(self) :
 print("주사위의 값=", self._value)
 def roll_dice(self) :
 self._value = randint(1, 6)
d = Dice(100, 100)
d.roll_dice()
d.print_dice()

# p.401 사각형 rectangle 클래스 지정(미완성)

class Rectangle:
    def __init__(self, x1, y1, x2, y2):
        self.x1, self.y1 = x1, y1
        self.x2, self.y2 = x2, y2
    
    def overlap(self, other):
        if (self.x1 < other.x2 and self.x2 > other.x1 and 
            self.y1 < other.y2 and self.y2 > other.y1):
            print("r1과 r2는 서로 겹칩니다")
        else:
            print("r1과 r2는 겹치지 않습니다")

# rectangle 클래스의 객체 생성
r1 = Rectangle(0, 0, 100, 100)
r2 = Rectangle(10, 10, 100, 100)

# overlap 메소드 호출
r1.overlap(r2)



# 402p. 06 person 클래스 작성.

class Person:
    def __init__(self, name, mobile=None, office=None, email=None):
        self.name = name
        self.mobile = mobile
        self.office = office
        self.email = email
    
    def __str__(self):
        return f"Name: {self.name}, Mobile: {self.mobile}, Office: {self.office}, Email: {self.email}"
    
    def setName(self, name):
        self.name = name
    
    def getName(self):
        return self.name
    
    def setMobile(self, mobile):
        self.mobile = mobile
    
    def getMobile(self):
        return self.mobile
    
    def setOffice(self, office):
        self.office = office
    
    def getOffice(self):
        return self.office
    
    def setEmail(self, email):
        self.email = email
    
    def getEmail(self):
        return self.email

# Person 객체 생성
p1 = Person("Kim", office="1234567", email="kim@company.com")
p2 = Person("Park", office="2345678")

# setEmail 메소드를 사용하여 이메일 설정
p2.setEmail("park@company.com")

# 정보 출력
print(p1)
print(p2)
        
    

"""
이번 장 배운 내용

 ▷ 클래스는 속성과 동작으로 이루어진다. 속성은 인스턴스 변수로 표현
되고 동작은 메소드로 표현된다.
 ▷ 객체를 생성하려면 생성자 메소드를 호출한다. 생성자 메소드는
__init__() 이름의 메소드이다. 
 ▷ 인스턴스 변수를 정의하려면 생성자 메소드 안에서 self.변수이름 과
같이 생성한다. 

"""







