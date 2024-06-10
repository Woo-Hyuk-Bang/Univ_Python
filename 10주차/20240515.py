# 2024-05-15 파일 처리
"""
 텍스트 파일 읽고 쓰기를 살펴본다. 
 이진 파일 읽고 쓰기를 살펴본다. 
 정규식을 사용하는 방법을 살펴본다. 
 CSV 파일 읽고 쓰기를 살펴본다. 
 예외를 처리하는 방법을 살펴본다.

"""

# 1. 매출 파일

infilename = input("입력 파일 이름: ");
outfilename = input("출력 파일 이름: ");
infile = open(infilename, "r")
outfile = open(outfilename, "w")
sum = 0
count = 0
line = infile.readline()
while line != "" :
	s = int(line)
	sum += s
	count += 1
	line = infile.readline()
	
outfile.write("총매출 = "+ str(sum)+"\n")
outfile.write("평균 일매출 = "+ str(sum/count ))
infile.close() 
outfile.close()

# 2. 행맨

import random
guesses = ''
turns = 10
infile = open("words.txt", "r")
lines = infile.readlines() 
word = random.choice(lines)
while turns > 0: 
	failed = 0 
	for char in word: 
		if char in guesses: 
			print(char, end="") 
		else:
			print("_", end="") 
			failed += 1 
	if failed == 0: 
		print("사용자 승리")
		break
		
	print("")
	guess = input("단어를 추측하시오: ") 
	guesses += guess 
	if guess not in word: 
		turns -= 1 
		print ("틀렸음!")
		print (str(turns)+ "기회가 남았음!") 
		if turns == 0: 
			print("사용자 패배 정답은 "+word)

infile.close()	

# 3. 각 문자 세기

filename = input("파일명을 입력하세요: ").strip()
infile = open(filename, "r") # 파일을 연다.

freqs = {}

# 파일의 각 줄에 대하여 문자를 추출한다. 각 문자를 사전에 추가한다. 
for line in infile:
	for char in line.strip(): # 양쪽 끝의 공백 문자를 제거한다. 
		if char in freqs: # 문자열 안의 각 문자에 대하여
			freqs[char] += 1 # 딕셔너리의 횟수를 증가한다. 
		else: # 처음 나온 문자이면
			freqs[char] = 1 # 딕셔너리의 횟수를 1로 초기화한다. 
			
print(freqs)
infile.close()

# csv 파일 불러오기

import csv

f = open('d://weather.csv') # CSV 파일을 열어서 f에 저장한다. 
data = csv.reader(f)
header = next(data) #헤더를 제거함
temp = 1000
for row in data:
	if temp > float(row[3]):
		temp = float(row[3])
print('가장 추웠던 날은', temp, '입니다')
f.close()

# 파일 암호화

key = 'abcdefghijklmnopqrstuvwxyz'

# 평문을 받아서 암호화하고 암호문을 반환한다. 
def encrypt(n, plaintext):
	result = ''
 
	for l in plaintext.lower():
		try:
			i = (key.index(l) + n) % 26
			result += key[i]
		except ValueError:
			result += l
			
return result.lower()

# 암호문을 받아서 복호화하고 평문을 반환한다. 
def decrypt(n, ciphertext):
	result = ''
 
	for l in ciphertext:
		try:
			i = (key.index(l) - n) % 26
			result += key[i]
		except ValueError:
			result += l

	return result
n = 3
text = 'The language of truth is simple.'
encrypted = encrypt(n, text)
decrypted = decrypt(n, encrypted)
print ('평문: ' , text)
print ('암호문: ', encrypted)
print ('복호문: ' , decrypted) 

"""

 파일을 읽을 때는 파일을 열고, 데이터를 읽은 후에, 파일을 닫는 절차가
필요하다. 
 파일 모드에서 “r”, “w”, “a”가 있다. 각각 읽기모드, 쓰기모드, 추가모드
를 의미한다. 
 파일은 텍스트 파일과 이진 파일로 나누어진다. 
 파일에서 데이터를 읽거나 쓰는 함수는 read()와 write() 함수이다. 텍스트
파일에서 한 줄을 읽으려면 for 루프를 사용한다. 
 예외 처리는 오류가 발생했을 때 프로그램을 우아하기 종료하는 방법이다. 
try 블록과 except 블록으로 이루어진다.

"""
"""
# 실습 문제

1. P 472~473 count_letters.py
2. P 474 csv.py 
3. P 475~476 cipher.py
4. P 482 binary_filecopy.py
5. P 484 pickl2.py 와 pickle2.py
6. P 488 password.py

"""

# count_letters.py

## 이 프로그램은 파일 안의 문자들의 개수를 센다

filename = input("파일명을 입력하세요: ").strip()
infile = open(filename, "r")

freqs = {}

# 파일의 각 줄에 대하여 문자를 추출한다.
for line in infile:
    for char in line.strip():
        if char in freqs:
            freqs[char] += 1
        else:
            freqs[char] = 1

print(freqs)
infile.close()

# csv.py

import csv

f = open('d://weather.csv')
data = csv.reader(f)
header = next(data)
temp = 1000
for row in data:
    if temp > float(row[3]):
        temp = flot(row[3])
print('가장 추웠던 날의 기온은', temp, '입니다')
f.close()

# cipher.py

# 파일 암호화

key = 'abcdefghijklmnopqrstuvwxyz'

# 평문을 받아서 암호화하고 암호문을 반환한다. 
def encrypt(n, plaintext):
	result = ''
 
	for l in plaintext.lower():
		try:
			i = (key.index(l) + n) % 26
			result += key[i]
		except ValueError:
			result += l
			
return result.lower()

# 암호문을 받아서 복호화하고 평문을 반환한다. 
def decrypt(n, ciphertext):
	result = ''
 
	for l in ciphertext:
		try:
			i = (key.index(l) - n) % 26
			result += key[i]
		except ValueError:
			result += l

	return result
n = 3
text = 'The language of truth is simple.'
encrypted = encrypt(n, text)
decrypted = decrypt(n, encrypted)
print ('평문: ' , text)
print ('암호문: ', encrypted)
print ('복호문: ' , decrypted) 

# binary_filecopy.py
infile = open("123.png", "rb")
outfile = open("kkk.png", "wb")

# 입력파일에서 1024 바이트씩 읽어서 출력 파일
while True:
    copy_buffer = infile.read(1024)
    if not copy_buffer:
        break
    outfile.write(copy_buffer)

infile.close()
outfile.close()
print("123.png를 kkk.png로 복사하였습니다.")