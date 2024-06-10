# 2024-05-29 상속 

"""
⚫ 부모 클래스를 상속받아서 자식 클래스를 정의할 수 있다
⚫ 부모 클래스의 메소드를 자식 클래스에서 재정의할 수 있다.
⚫ Object 클래스를 이해할 수 있다. 
⚫ 메소드 오버라이딩을 이해하고 사용할 수 있다. 
⚫ 클래스 간의 관계를 파악할 수 있다.

이번 장에서 만들 프로그램
(1) 상속을 이용하여서 각 클래스에 중복된 정보를 부모 클래스로 모아
보자. 구체적인 예로 Car 클래스와 ElectricCar 클래스를 작성해보자. 
(2) 상속을 사용할 때, 자식 클래스와 부모 클래스의 생성자가 호출되는
순서를 살펴보자. 
(3) 부모 클래스의 함수를 오버라이딩(재정의)하여 자식 클래스의 기능
을 강력하게 하는 기법을 살펴보자.

"""

# Lab: Bank 클래스

class Bank(): 
	def getInterestRate(self):
		return 0.0

class BadBank(Bank):
	def getInterestRate(self):
		return 10.0;

class NormalBank(Bank):
	def getInterestRate(self):
		return 5.0;

class GoodBank(Bank):
	def getInterestRate(self):
		return 3.0;

b1 = BadBank()
b2 = NormalBank()
b3 = GoodBank()
print("BadBank의 이자율: " + str(b1.getInterestRate()))
print("NormalBank의 이자율: " + str(b2.getInterestRate()))
print("GoodBank의 이자율: " + str(b3.getInterestRate()))

# Lab: 직원과 매니저

class Employee:
	def __init__(self, name, salary):
		self.name = name
		self.salary = salary
 
	def getSalary(self):
		return salary

class Manager(Employee):
	def __init__(self, name, salary, bonus):
		super().__init__(name, salary)
		self.bonus =bonus

	def getSalary(self):
		salary = super().getSalary()
		return salary + self.bonus

	def __repr__(self):
		return "이름: "+ self.name+ "; 월급: "+ str(self.salary)+\
		"; 보너스: "+str(self.bonus)

kim = Manager("김철수", 2000000, 1000000)
print(kim)

# Lab: 은행 계좌

class BankAccount:
	def __init__(self, name, number, balance):

		self.balance = balance
		self.name = name
		self.number = number

	def withdraw(self, amount):
		self.balance -= amount
		return self.balance

	def deposit(self, amount):
		self.balance += amount
		return self.balance

class SavingsAccount(BankAccount) :
	def __init__(self, name, number, balance, rate):
		super().__init__( name, number, balance)
		self.interest_rate = rate # 예금 이율

	def deposit(self, amount):
		return BankAccount.deposit(self, amount)
 
	def add_interest(self):
		return self.balance + (self.balance * self.interest_rate)

class CheckingAccount(BankAccount) :
	def __init__(self, name, number, balance):
		super().__init__( name, number, balance)
		self.withdraw_charge = 10000 # 수표 발행 수수료

	def withdraw(self, amount):
		return BankAccount.withdraw(self, amount + self.withdraw_charge)

a1 = SavingsAccount("홍길동", 123456, 5000000, 0.05)
a1.deposit(10000)
print("저축예금의 잔액=", a1.balance)
sum = a1.add_interest()
print("저축예금 + 이자합산 금액 =", sum)

a2 = CheckingAccount("김철수", 123457, 2000000)
a2.withdraw(100000)
print("당좌예금의 잔액=", a2.balance)

# Lab: Card와 Deck

class Card:
	suitNames = ['클럽', '다이아몬드', '하트', '스페이드']
	rankNames = [None, '에이스', '2', '3', '4', '5', '6', '7', 
		'8', '9', '10', '잭', '퀸', '킹']

	def __init__(self, suit, rank):
		self.suit = suit
		self.rank = rank

	def __str__(self):
		return Card.suitNames[self.suit]+" "+\
			Card.rankNames[self.rank]

class Deck:
	def __init__(self):
		self.cards = []

		for suit in range(4):
			for rank in range(1, 14):
				card = Card(suit, rank)
				self.cards.append(card)
	def __str__(self):
		lst = [str(card) for card in self.cards]
		return str(lst)

deck = Deck() # 덱 객체를 생성한다. 
print(deck) # 덱 객체를 출력한다. __str__()이 호출된다. 

# Lab: 학생과 강사

class Person:
	def __init__(self, name, number):
		self.name = name
		self.number = number

class Student(Person):
	UNDERGRADUATE=0
	POSTGRADUATE = 1

	def __init__(self, name, number, studentType ):
		super().__init__(name, number)
		self.studentType = studentType
		self.gpa=0
		self.classes = []

	def enrollCourse(self, course):
		self.classes.append(course)

 def __str__(self):
	return "\n이름="+self.name+ "\n주민번호="+self.number+\
		"\n수강과목="+ str(self.classes)+ "\n평점="+str(self.gpa)

class Teacher(Person):
	def __init__(self, name, number):
		super().__init__(name, number)
		self.courses = []
		self.salary=3000000

	def assignTeaching(self, course):
		self.courses.append(course)

	def __str__(self):
		return "\n이름="+self.name+ "\n주민번호="+self.number+\
			"\n강의과목="+str(self.courses)+ "\n월급="+str(self.salary)

hong = Student("홍길동", "12345678", Student.UNDERGRADUATE )
hong.enrollCourse("자료구조")
print(hong)

kim = Teacher("김철수", "123456790")
kim.assignTeaching("Python")
print(kim)


"""
 BankAccount 클래스는 다음과 같은 인스턴스 변수와 메소드를 가진다. 
➢ balance –- 잔액(정수형)
➢ name –- 소유자의 이름(문자열)
➢ name –- 통장 번호(정수형)
➢ withdraw() -- 출금 메소드
➢ deposit() - 저금 메소드
 BankAccount 클래스를 상속받아서 SavingsAccount 클래스(저축예금)를 작성한다. 
   SavingsAccount 클래스는 추가로 다음과 같은 인스턴스 변수와 메소드를 가진다. 
➢ interest_rate – 이자율(실수형)
➢ add_interest() - 호출될 때마다 예금에 이자를 더하는 메소드
 BankAccount 클래스를 상속받아서 CheckingAccount 클래스(당좌예금)를 작성한다. 
   CheckingAccount 클래스는 추가로 다음과 같은 인스턴스 변수와 메소드를 가진다. 
➢ withdraw_charge – 수표를 1회 발행할 때 수수료(정수형)
➢ withdraw() - 찾을 금액에 수수료를 더해서 출금한다. 
"""

# Lab: Vehicle와 Car, Truck

class Vehicle:
	def __init__(self, name): 
		self.name = name

	def drive(self): 
		raise NotImplementedError("이것은 추상메소드입니다. ")

 	def stop(self): 
		raise NotImplementedError("이것은 추상메소드입니다. ")

class Car(Vehicle):
	def drive(self):
		return '승용자를 운전합니다. '

	def stop(self):
		return '승용자를 정지합니다. '

class Truck(Vehicle):
	def drive(self):
		return '트럭을 운전합니다. '

	def stop(self):
		return '트럭을 정지합니다. '

cars = [Truck('truck1'), Truck('truck2'), Car('car1')]

for car in cars:
	print( car.name + ': ' + car.drive())

"""
 상속은 다른 클래스를 재사용하는 탁월한 방법이다. 객체와 객체간의 is-a 관계가 성립된다면 상속을 이용하도록 하자. 
 상속을 사용하면 중복된 코드를 줄일 수 있다. 공통적인 코드는 부모 클래스를 작성하여 한 곳으로 모으도록 하자. 
 상속에서는 부모 클래스의 메소드를 자식 클래스가 재정의할 수 있다. 
   이것을 메소드 오버라이딩이라고 한다.
"""