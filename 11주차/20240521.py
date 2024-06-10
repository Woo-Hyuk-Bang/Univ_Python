# 2024-05-21 파이썬 - 실습코드
"""
    1. count_letters.py p.472~473
    2. csv.py p.474
    3. cipher.py 475~476
    4. binary_filecopy.py
    5. pickle2.py
    6. password.py
    
"""

# 1.

filename = input("파일명을 입력하세요: ").strip()
infile = open(filenmae, "r")

freqs = {}

# 각 줄에서 문자를 추출하는 코드
for line in infile:
    for char in line.strip():
        if char in freqs:
            freqs[char] += 1
        else:
            freqs[char] = 1
            
print(freqs)
infile.close()

# 2. csv

import csv

f = open('d://weather.csv')
data = csv.reader(f)
header = next(data)
temp = 1000
for row in data:
    if temp > float(row[3]):
        temp = float(row[3])
print('가장 추웠던 날의 기온은', temp, '입니다')
f.close()

# 3. 평문을 받아서 암호화하고 암호문을 반환한다. 
def encrypt(n, plaintext):
	result = ''
 
	for l in plaintext.lower():
		try:
			i = (key.index(l) + n) % 26
			result += key[i]
		except ValueError:
			result += l
			
return result.lower()

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

# 4. pickle.py 1,2

# 4-1 파일 저장

import pickle

gameOption = {
        "sound":8,
        "VideoQuality":"HIGH"
        "Money" : 100000,
        "WeaponList":["gun", "missile", "knife" ]
}

file = open( "save.p", "wb")
pickle.dump( gameOption, file)
file.close()

# 4-2. 파일 로드
import pickle

file = open( "save.p" , "rb" )
obj = pickle.load( file )
print(obj)

# password.py

import re
password = input("패스워드를 입력하세요");
flag = 0
while True:
    if (len(password)<8):
        flag = -1
        break
    elif not re.search("[a-z]", password):
        flag = -1
        break
    elif not re.search("[A-Z]", password):
        flag = -1
        break        
    elif not re.search("[0-9]", password):
        flag = -1
        break        
    elif not re.search("[_@$]", password):
        flag = -1
        break        
    else:
        flag = 0
        print("유효한 패스워드")
        break

if  flag == -1:
    print("유효한 패스워드가 아닙니다.")
        