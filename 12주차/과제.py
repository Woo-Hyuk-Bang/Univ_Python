# -*- coding: utf-8 -*-
"""
Created on Wed Mar 27 09:37:50 2024

@author: User
"""

# [5장]
'''
P245 Exercise 07번
다음 코드의 실행 결과를 보이시오
'''

def sub(a=2, b=3):
    print(a, b)
    
sub()
sub(a=10)
sub(5, 6)
sub(b=10)
'''
P245 Exercise 08번
다음 코드의 실행 결과를 보이시오
'''

def sub(a, b):
    return a+b, a-b
    
x, y = sub(10, 20)
print(x,y)

'''
P245 Exercise 09번
다음 코드에서 오류가 발생한 이유는?
'''

global2 = 0
def sub():
    local = 1
    print(global2)
    print(local)
    
sub()
print(global2)
print(local)

'''
P246 Programming  04번
성적이 90점 이상이면 A, 80점 이상이면 B, 70점 이상이면 C, 60점 이상이면 D,
그 외에는 F를 반환하는 함수 getGrade(score)를 작성하고 테스트하라.
'''
x = int(input("점수를 입력하세요"))
y = None
if (x >= 90) : 
    y = 'A'
elif (x >= 80) :
    y = 'B' 
elif (x >= 70) :
    y = 'C'      
elif (x >= 60) :
    y = 'D'   
else : 
    y = 'F'         
print("점수는" + y + "입니다")

'''
P247 Programming  06번
사용자로부터 2개의 정수를 받아서 수학 문제를 만들어서 화면에 출력하는 함수를 작성하고
테스트하시오.
'''

x = int(input("첫 번째 정수를 입력하시오: "))
y = int(input("두 번재 정수를 입력하시오: "))
print("정수", x, "+" , y, "의 합은? ")
print(x+y)

'''
P247 Programming  09번
사용자로부터 두 개의 정수를 입력받아서 최대 공약수를 찾는 함수를 작성하라.
가장 간단한 알고리즘을 생각하라
'''

x = int(input("첫 번째 정수: "))
y = int(input("두 번째 정수: "))
gcd = 1
if (x > y):    
    for i in range(y, 0, -1):
        if x % i == 0 and y % i == 0:
            gcd = i
            break

print(gcd)
    

'''
P248 Programming  12번
2개의 정수를 크기 순으로 반환하는 함수 getSorted(x, y)를 작성하고 테스트하라.
파이썬의 다중값 반환하기 기능을 활용하라.
'''

def getSorted(x, y):
    if x > y:
        return y, x
    else:
        return x, y

x = int(input("첫 번째 정수: "))
y = int(input("두 번째 정수: "))

getSorted(x, y)

#[6장]

'''
P298 Exercise 04번
다음 코드의 출력은 무엇인가?
'''
aList = [10, 20, 30, 40, 50]
print(aList[-2])
print(aList[-3:-1])

'''
P298 Exercise 06번
다음 코드의 출력은 무엇인가?
'''

aList = [x+y for x in ['hello ', 'Good '] for y in ['world', 'Bye']]
print(aList)

'''
P299 Exercise 09번
다음 코드의 출력은 무엇인가?
'''

aList = [1, 2, 3, 4, 5, 6, 7]
bList = [2 * x for x in aList]
print(bList)

'''
P300 Exercise 13번
다음 코드의 출력은 무엇인가?
'''

values = [ 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
result = 0
for i in range(0, len(values), 2) :
    result = result + values[i]
print(result)

'''
P300 Exercise 14번
다음 코드에서 잘못된 점은 무엇인가?
'''

values = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for i in range(0, 11, 1):
    values[i] = i * i

'''
P301 Programming  02번
2. 1부터 100 사이의 난수 10개를 생성하여 리스트 values를 채우는 반복 루프를 작성
'''
import random
alist = []
for i in range(10):
    alist.append(random.randint(1, 100)) 
print(alist)

'''
P302 Programming  08번
다음과 같은 2개의 리스트가 있다. 2개의 리스트에 공통적인 요소를 추출하는
리스트 함축 코드를 작성해보자.
'''
a = [1, 2, 3, 4, 5]
b = [1, 3, 3, 4, 5, 6, 7 ]
result = []

for i in range(min(len(a), len(b))):
    if a[i] == b[i]:
        result.append(a[i])

print("a=",a)
print("b=",b)
print("결과",result)

'''
[7장]
P359 Programming  02번
(x, x*x) 형식의 숫자 (1과 10 사이)를 포함하는 딕셔너리를 생성하고 출력하는 프로그램을 작성해보자
'''

dict = {}

for x in range(1, 11):
    dict[x] = x*x

print(dict)

'''
P359 Programming  05번
딕셔너리에 쇼핑몰에서 구입한 상품의 가격이 저장되어 있다. 딕셔너리에 있는 모든 상품 가격의 합계를 계산하는 프로그램을 작성해보자
'''

myDict = {"옷": 100, "컴퓨터": 2000, "모니터": 320}

total_price = sum(myDict.values())

print("총합계 =", total_price)

'''
P360 Programming  09번
2개의 문자열을 받아서, 이들 문자열에 모두 포함된 글자를 반환하는 프로그램을 작성해보자
'''

def common_characters(str1, str2):
    set1 = set(str1)
    set2 = set(str2)
    
    common_chars = set1.intersection(set2)
    return common_chars

str1 = input("첫 번째 문자열: ")
str2 = input("두 번째 문자열: ")

result = common_characters(str1, str2)
print("모두 포함된 글자:", result)

'''
P361 Programming  13번
문자열을 받아서 글자의 개수와 숫자의 개수를 계산하여 딕셔너리로 작성하는 프로그램을 작성하라.
'''

def count_function(string1):
    char_count = sum(1 for x in string1 if x.isalpha())
    digit_count = sum(1 for x in string1 if x.isdigit())
    return {"LETTERS": char_count, "DIGITS": digit_count}

string1 = input("문자열을 입력하세요: ")

result = count_function(string1)
print(result)

'''
P362 Programming  15번
딕셔너리에 키-값 쌍으로 저장된 학생의 국적 리스트가 있다.
딕셔너리에서 이름과 국적을 꺼내서 다음과 같이 학생의 태그를 출력하는 프로그램을 작성해보자.
딕셔너리에서 값을 꺼낼때, myDic[key]를 사용한다.
'''

my_dict = {"Park": "Korea",
           "Sam": "USA",
           "Sakura":"Japan"
           }

for name in my_dict:
    nationality = my_dict[name]
    tag = f"Hi! I'm {name}, and I'm from {nationality}."
    print(tag)