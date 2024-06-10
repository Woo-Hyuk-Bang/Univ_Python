# 6. Lab: 리스트 변경 함수

salaries = [200, 250, 300, 280, 500]
def modify(values, factor) :
    for i in range(len(values)) :
        values[i] = values[i] * factor
print("인상전", salaries)
modify(salaries, 1.3)
print("인상후", salaries)

# 도전과제 위의 함수에서 modify()를 다음과 같이 변경하면 실행 결과는?
"""
def modify(values, factor) :
    for e in values :
        e = e * factor
        
인상전 [200, 250, 300, 280, 500]
인상후 [200, 250, 300, 280, 500]        

-> 즉, e의 값만 바뀌고 있으며, 리스트의 값들은 변하지 않는다
"""

# 7. Lab: 리스트 함축 사용하기

numbers = [x for x in range(100) if x % 2 == 0 and x % 3 == 0]
print(numbers)

# 도전문제 : 0부터 9까지의 정수 중에서 짝수면 "짝수"를 리스트에 추가, 
# 홀수이면 "홀수"를 리스트에 추가하는 함축

result = ["짝수" if x % 2 == 0 else "홀수" for x in range(10)]
print(result)

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

board = [[' ' for x in range(3)] for y in range(3)]
while True:
    # 게임 보드를 그린다.
    for r in range(3):
        print("  " + board[r][0] + "|  " + board[r][1] + "|  " + board[r][2])
        if r != 2:
            print("---|---|---")
    
    # 사용자로부터 좌표를 입력받는다.
    while True:
        x = int(input("다음 수의 x좌표를 입력하시오: "))
        y = int(input("다음 수의 y좌표를 입력하시오: "))
        
        # 사용자가 입력한 좌표를 검사한다.
        if x < 0 or x > 2 or y < 0 or y > 2 or board[x][y] != ' ':
            print("잘못된 위치입니다. 다시 입력하세요.")
        else:
            board[x][y] = 'X'
            break

    # 컴퓨터가 놓을 위치를 결정한다. 첫 번째로 발견하는 비어있는 칸에 놓는다.
    done = False
    for i in range(3):
        if done:
            break
        for j in range(3):
            if board[i][j] == ' ':
                board[i][j] = 'O'
                done = True
                break