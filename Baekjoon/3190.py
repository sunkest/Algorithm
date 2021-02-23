# BOJ 3190 # 뱀 # Gold 5
# 삼성전자 SW 역량테스트
# Simulation, queue
# 이것이 취업을 위한 코딩테스트다 - part 3 - 구현
from collections import deque

N = int(input())
K = int(input())
board = [[1 for _ in range(N+2)] for _ in range(N+2)]   # padding(벽) 포함

for i in range(1, N+1):
    for j in range(1, N+1):
        board[i][j] = 0     # padding 제외 0

board[1][1] = 1     # 초기 뱀 위치

for _ in range(K):      # 사과 입력
    row, col = map(int, input().split())
    board[row][col] = 4

L = int(input())
turns = deque()
for _ in range(L):
    x, C = input().split()
    X = int(x)
    turns.append((X, C))


dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
snake = deque()
snake.append((1, 1))
direction = 0   # 0 우, 1 하, 2 좌, 3 상    # 우회전: +1 % 4, 좌회전: -1 % 4
t = 0
while True:
    if len(turns) > 0 and turns[0][0] == t:
        X, C = turns.popleft()
        if C == 'D':
            direction += 1
        elif C == 'L':
            direction -= 1
        direction %= 4

    next_x = snake[0][0] + dx[direction]
    next_y = snake[0][1] + dy[direction]
    next_box = board[next_x][next_y]
    snake.appendleft((next_x, next_y))
    if next_box == 1:
        break
    elif next_box == 0:
        tail_x, tail_y = snake.pop()
        board[tail_x][tail_y] = 0

    board[next_x][next_y] = 1
    t += 1

print(t+1)