# 2024-04-17 파이썬 - 자료구조2
"""
튜플을 이해하고 사용할 수 있다. 
세트를 이해하고 활용할 수 있다. 
딕셔너리를 이해하고 활용할 수 있다. 
문자열의 각종 연산을 이해하고 활용할 수 있다.

리스트와 튜플(tuple)은 아주 유사하다. 하지만 리스트와는 다르게 튜
플은 변경이 불가능하다.

<주의할 점>
>>> single_tuple = ("apple",) # 쉼표가 끝에 있어야 한다. 
>>> single_tuple
("apple",) 
>>> no_tuple = ("apple") # 쉼표가 없으면 튜플이 아니라 수식이 된다. 
>>> no_tuple
"apple" 

튜플 연산자 교재에서 정리해놓을 것.
세트 연산자 교재에서 정리해놓을 것.
딕셔너리
"""

# LAB 1. 문자열의 공통문자
s1=input("첫 번째 문자열:")
s2=input("두 번째 문자열:")
list1 = list( set(s1) & set(s2) ) # 세트로 만들고 교집합 연산을 한다. 
print("\n공통적인 글자:", end=" ")
for i in list1:
    print(i, end=" ")

# 2)
txt = input("입력 텍스트: ")
words = txt.split(" ")
unique = set(words) # 집합으로 만들면 자동적으로 중복을 제거한다. 

print("사용된 단어의 개수= ", len(unique))
print(unique)

# 항목 추가하기

capitals ={}
capitals["Korea"]="Seoul"
capitals["USA"]="Washington"
capitals["UK"]="London"
capitals["France"]="Paris"
print(capitals)


# LAB 2. 영한사전
english_dict ={} # 공백 딕셔너리를 생성한다. 

english_dict["one"]="하나" # 딕셔너리에 단어와 의미를 추가한다. 
english_dict["two"]="둘'"
english_dict["three"]="셋"

word =input("단어를 입력하시오: ");
print (english_dict[word])

# LAB 3. 학생 성적 처리
def main():
 address_book ={} # 공백 딕셔너리를 생성한다. 
 while True :
 user = display_menu();
 if user ==1 :
 name, number = get_contact()
 address_book[name]= number # name과 number를 추가한다. 
 elif user ==2 :
 name, number = get_contact()
 address_book.pop(name) # name을 키로 가지고 항목을 삭제한다. 
 elif user ==3 :
 pass # 도전 문제 참조
elif user ==4 :
 for key in sorted(address_book):
 print(key,"의 전화번호:", address_book[key])
 else :
 break

# 이름과 전화번호를 입력받아서 반환한다. 
def get_contact():
 name =input("이름: ")
 number =input("전화번호:")
 return name, number # 튜플로 반환한다. 
# 메뉴를 화면에 출력한다. 
def display_menu() :
 print("1. 연락처 추가") 
 print("2. 연락처 삭제") 
 print("3. 연락처 검색") 
 print("4. 연락처 출력") 
 print("5. 종료") 
 select = int(input("메뉴 항목을 선택하시오: "))
 return select
main()

score_dic = { 
"Kim":[99,83,95],
"Lee":[68,45,78],
"Choi":[25,56,69]
}

score_dic = { 
 "Kim":[99,83,95],
 "Lee":[68,45,78],
 "Choi":[25,56,69]
}
for name, scores in score_dic.items():
 print(name,"의 평균성적=",sum(scores)/len(scores))


# LAB 4. 단어 카운터 만들기
# 1)
text_data ="Create the highest, grandest vision possible for your life, because 
you become what you believe"
word_dic = {} # 단어들과 출현 횟수를 저장하는 딕셔너리를 생성
for w in text_data.split(): # 텍스트를 단어들로 분리하여 반복한다. 
 if w in word_dic: # 단어가 이미 딕셔너리에 있으면
word_dic[w] += 1 # 출현 횟수를 1 증가한다. 
 else: # 처음 나온 단어이면 1로 초기화한다. 
 word_dic[w] = 1 
for w, count in sorted(word_dic.items()): # 키와 값을 정렬하여 반복 처리한다. 
 print(w, "의 등장횟수=", count)

# 2)
from collections import Counter
text_data ="Create the highest, grandest vision possible for your life, because 
you become what you believe"
a = Counter(text_data.split())
print(a)

# 문자열 연산

# LAB 5. 회문 검사하기
s = input("문자열을 입력하시오: ")
s1 = s[::-1] # 문자열을 거꾸로 만든다. 
if( s == s1 ):
 print("회문입니다.")
else:
 print("회문이 아닙니다.")

# 문자열 대소문자 변환
>>> s = "i am a student."
>>> s.capitalize()
"I am a student."
>>> s = "Breakfast At Tiffany""
>>> s.lower()
"breakfast at tiffany""
>>> s.upper()
"BREAKFAST AT TIFFANY""

# LAB 6. 머리 글자어 만들기
phrase = input("문자열을 입력하시오: ")
 
acronym = ""
# 대문자로 만든 후에 단어들로 분리한다. 
for word in phrase.upper().split():
acronym += word[0] # 단어를 첫 글자만을 acronym에 추가한다. 
 
print( acronym )

# LAB 7. 이메일 주소 분석
address=input("이메일 주소를 입력하시오: ")
(id, domain) = address.split("@")
print(address)
print("아이디:"+id)
print("도메인:"+domain)

# LAB 7. 문자열 분석

sentence = input("문자열을 입력하시오: ")
table ={"alphas":0,"digits":0,"spaces":0 }
for i in sentence:
 if i.isalpha():
 table["alphas"]+=1
 if i.isdigit():
 table["digits"]+=1
 if i.isspace():
 table["spaces"]+=1
print(table)

# LAB 7. 트위터 메시지 처리
t = "Python is very easy and powerful!"
length = len(t.split(" "))
print(length)


# LAB 8. OTP 생성
import random
 
s = "0123456789" # 대상 문자열
passlen = 4 # 패스워드 길이
sample()은 주어진 개수만큼의 글자를 문자열 s에서 임의로 선택한다. join()은 이들 글자들을 결합한다. 
p = "".join(random.sample(s, passlen ))
print(p)

"""
이번 장 배운 내용
 튜플은 변경 불가능한 항목들을 모아둔 곳이다. 
 ()을 이용하여 공백 튜플을 만들 수 있다. 
 딕셔너리는 키와 값으로 이루어진다. 
 딕셔너리에서 [] 연산자를 사용하여 키와 관련된 값을 액세스할 수 있다. 
 딕셔너리에서 pop 메소드를 사용하여 항목을 제거한다. 
 세트는 고유한 값들을 저장한다. 
 세트는 set() 함수를 사용하여 생성할 수 있다. 
 세트의 add() 메소드를 사용하여 새 요소를 추가할 수 있다.
"""







