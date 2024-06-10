# chapter_6 자료구조1 - 리스트
"""
리스트를 생성하고 초기화할 수 있다. 
리스트의 요소를 참조하는 방법을 학습한다. 
리스트를 함수에 전달하는 방법을 학습한다. 
리스트에서 항목 검색, 정렬, 항목 삽입 및 항목 제거와 같은 연산을 할 수 있다. 
리스트에서 슬라이싱의 개념을 이해하고 활용할 수 있다. 
리스트 함축을 이해하고 사용할 수 있다. 
2차원 리스트를 사용할 수 있다.
"""

# 1. LAB 성적 처리 프로그램

STUDENTS = 5 
lst = [] 
count=0
for i in range(STUDENTS):
    value = int(input("성적을 입력하시요: "))
    lst.append(value)
print("\n성적 평균=", sum(lst) / len(lst))
print("최대점수=", max(lst))
print("최소점수=", min(lst))
for score in lst:
    if score >= 80:
        count += 1
print("80점 이상=", count)

# 2. Lab: 리스트에서 2번째로 큰 수 찾기

list1 = [1, 2, 3, 4, 15, 99] 
# 리스트를 정렬한다. 
list1.sort() 
 
# 뒤에서 두 번째 요소를 출력한다. 
print("두 번째로 큰 수=", list1[-2]) 

list1 = [1, 2, 3, 4, 15, 99] 
# 제일 큰 수는 삭제한다. 
list1.remove(max(list1)) 
# 그 다음으로 큰 수를 출력한다. 리스트는 변경되었다. 
print("두 번째로 큰 수=", max(list1)) 

scores = [10.0, 9.0, 8.3, 7.1, 3.0, 9.0]
print("제거전", scores)
scores.remove(max(scores))
scores.remove(min(scores))
print("제거후", scores)

# 3. Lab: 리스트로 스택 흉내내기

stack = []
for i in range(3) :
    f = input("과일을 입력하시오: ")
    stack.append(f)
for i in range(3) :
    print( stack.pop() )

# 4. Lab: 친구 관리 프로그램

menu = 0
friends = []
while menu != 9:
 print("--------------------")
 print("1. 친구 리스트 출력")
 print("2. 친구추가")
 print("3. 친구삭제")
 print("4. 이름변경")
 print("9. 종료")
 menu = int(input("메뉴를 선택하시오: "))
 if menu == 1:
     print(friends)
 elif menu== 2:
     name = input("이름을 입력하시오: ")
     friends.append(name)
 elif menu == 3:
     del_name = input("삭제하고 싶은 이름을 입력하시오: ")
 if del_name in friends:
     friends.remove(del_name) 
 elif menu == 4:
     old_name = input("변경하고 싶은 이름을 입력하시오: ")
     if old_name in friends:
         index = friends.index(old_name)
         new_name = input("새로운 이름을 입력하시오: ")
         friends[index] = new_name
     else:
         print("이름이 발견되지 않았음")

# 5. Lab: 리스트 슬라이싱

numbers = [ 1, 2, 3, 4, 5, 6, 7, 8, 9, 10 ]
reversed = numbers[::-2]
print(reversed)

numbers = [ 1, 2, 3, 4, 5, 6, 7, 8, 9, 10 ]
numbers[1:] = [ ]
print(numbers)

# 6. Lab: 리스트 변경 함수

salaries = [200, 250, 300, 280, 500]
def modify(values, factor) :
    for i in range(len(values)) :
        values[i] = values[i] * factor
print("인상전", salaries)
modify(salaries, 1.3)
print("인상후", salaries)

# 7. Lab: 리스트 함축 사용하기

numbers = [x for x in range(100) if x % 2 == 0 and x % 3 == 0]
print(numbers)

# 8. Lab: 누적값 리스트 만들기

list1=[10, 20, 30, 40, 50]
list2=[sum(list1[0:x+1]) for x in range(0, len(list1))]
print("원래 리스트: ",list1)
print("새로운 리스트: ",list2)

# 9. Lab: 피타고라스 삼각형

[(x,y,z) for x in range(1,30) for y in range(x,30) for z in range(y,30) if
x**2 + y**2 == z**2]

new_list = []
for x in range(1, 30):
for y in range(x, 30):
for z in range(y, 30):
 if x**2+y**2==z**2:
 new_list.append((x, y, z))
print(new_list)


# 10. Lab: 전치 행렬 계산

transposed = []
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print("원래 행렬=", matrix)
# 열의 개수만큼 반복한다. 
for i in range(len(matrix[0])):
 transposed_row = []
 for row in matrix: # 행렬의 각 행에 대하여 반복
transposed_row.append(row[i])# i번째 요소를 row에 추가한다. 
 transposed.append(transposed_row)
print("전치 행렬=", transposed)

# 11. Lab: Tic-Tac-Toe

board= [[' ' for x in range (3)] for y in range(3)]
while True:
 # 게임 보드를 그린다.
 for r in range(3):
 print(" " + board[r][0] + "| " + board[r][1] + "| " 
+ board[r][2])
 if (r != 2):
 print("---|---|---")
 # 사용자로부터 좌표를 입력받는다. 
 x = int(input("다음 수의 x좌표를 입력하시오: "))
 y = int(input("다음 수의 y좌표를 입력하시오: "))
 
 # 사용자가 입력한 좌표를 검사한다. 
 if board[x][y] != ' ':
 print("잘못된 위치입니다. ")
 continue
 else:
 board[x][y] = 'X'
 #컴퓨터가 놓을 위치를 결정한다. 첫 번째로 발견하는 비어있는 칸에 놓는다. 
 done =False
 for i in range(3): 
 for j in range(3): 
 if board[i][j] == ' ' and not done:
 board[i][j] = 'O';
 done=True
 break;

"""
 리스트는 일련의 값을 저장하는 컨테이너이다.
 리스트의 각 요소는 인덱스라는 정수로 접근된다. 예를 들어서 i번째 요소
는 mylist[i]가 된다.
 ____메소드를 사용하여 리스트의 임의 위치에 새로운 요소를 삽입할 수
있다.
 pop() 메소드를 사용하여 리스트의 임의 위치에서 요소를 제거할 수 있다.
 ______ 메소드를 사용하여 리스트에서 원하는 요소를 제거할 수 있다.
 + 연산자를 사용하여 두 리스트를 연결할 수 있다.
 슬라이스 연산자 (:)를 사용하여 부분 리스트를 만들 수 있다.
 리스트 함축은 기존 리스트를 기반으로 새로운 리스트를 작성하는 우아한
방법이다.
"""


