#2024-03-19 python class
#chapter 2 실습문제

#1 atm.py (p.107)

##
# 이 프로그램은 자판기에서 거스름돈을 계산한다
#
itemPrice = int(input("물건 값을 입력하시오: "))
print("===입력금액===")
note = int(input("1000원 지폐개수: "))
coin500 = int(input("500원 동전개수: "))
coin100 = int(input("100원 동전개수: "))

change = note*1000 + coin500*500 + coin100*100 - itemPrice

#거스름돈(500원) 계산한다
nCoin500 = change//500
change = change%500

#거스름돈(100원) 계산한다
nCoin100 = change//100
change = change%100

#거스름돈(10원) 계산한다
nCoin10 = change//10
change = change%10

#거스름돈(1원) 계산한다
nCoin1 = change

print("===거스름돈 출력===")
print("500원=",nCoin500, "100원=",nCoin100, "10원=", nCoin10, "1원=", nCoin1)


#2 실습문제 07번 (p.111)
# 두 점의 좌표를 입력받아 두 점 사이의 거리를 계산하는 프로그램을 작성하라.
# 1) 좌표 두개를 입력받는다.
# 1-1) 배열로 값을 받는다?
# 2) 두 좌표의 공식값을 입력받는다
# 3) 결과값을 출력한다.

class Point2D:
    def __init__(self, x, y):
        self.x = x
        self.y = y
 
x1 = int(input("1번 x좌표: ")) 
y1 = int(input("1번 y좌표: "))  
x2 = int(input("2번 x좌표: "))  
y2 = int(input("2번 y좌표: "))  
 
 
p1 = Point2D(x=x1, y=y1)    # 점1
p2 = Point2D(x=x2, y=y2)    # 점2
 
distance = ((x1-x2)**2 + (y1-y2)**2) ** 0.5
 
print('p1: {} {}'.format(p1.x, p1.y))    # 30 20
print('p2: {} {}'.format(p2.x, p2.y))    # 60 50

print('두 점 사이의 거리: ',distance)



#3 실습문제 09번
number = int(input("정수를 입력해주세요: "))
print('각 자리수의 합', number // 1000 + (number % 1000 - number % 100) // 100 + (number % 100 - number % 10) // 10 + number % 10)
