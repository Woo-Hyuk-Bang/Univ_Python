# 2024-05-16 11장 내장함수, 람다식, 제너레이터, 모듈

# 6. P 543 Programming 02번
eval() 함수를 사용하여 사용자가 어떤 문자열을 입력하더라도 오류를 일으키지 않고
정수나 실수로 변환하는 코드

def test_eval(input_str):
    try:
        return eval(input_str, {"__builtins__": None}, {})
    except:
        return None


# 7. P 543 Programming 04번
data = [('국어', 88), ('수학', 90), ('영어', 99), ('자연', 82)]
sorted_data = sorted(data, key=lambda x: x[1])

print("정렬된 리스트 :")
print(sorted_data)

# 8. P 544 Programming 06번

# factorial.py
def fact(n):
    if n == 0:
        return 1
    else:
        return n * fact(n - 1)

# main.py
from factorial import fact

# 9. P 544 Programming 08번

def infinite_counter(start=0):
    while True:
        yield start
        start += 1


# 10.P 544 Programming 10번
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# 각 요소의 제곱
squares = list(map(lambda x: x ** 2, numbers))

# 11.P 544 Programming 11번

class Circle:
    def __init__(self, radius):
        self.__radius = radius
    
    @property
    def radius(self):
        return self.__radius

    def __add__(self, other):
        return Circle(self.radius + other.radius)

    def __gt__(self, other):
        return self.radius > other.radius

    def __lt__(self, other):
        return self.radius < other.radius

    def __repr__(self):
        return f"Circle(radius={self.radius})"
    
# 12.P 544 Programming 12번

import random

words = ['학습', '컴퓨터', '마우스', '키보드', '모니터', '프로그래밍', '언어']

selected_words = random.sample(words, 3)
