import sys
from collections import deque

input = sys.stdin.readline

r, c = map(int, input().split())
ground = [[-1] * (c + 2) for _ in range(r + 2)]
start = [0, 0]
water = []
for i in range(1, r + 1):
    string = input()
    for j in range(1, c + 1):
        ch = string[j - 1]
        if ch == 'S':
            start = [i, j]
            ground[i][j] = 0
        elif ch == '.':
            ground[i][j] = 0
        elif ch == '*':
            water.append((i, j))
            ground[i][j] = 1
        elif ch == 'X':
            ground[i][j] = -1
        elif ch == 'D':
            ground[i][j] = 5


dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]
visited = [[False] * (c + 2) for _ in range(r + 2)]
visited[start[0]][start[1]] = True
start = (start[0], start[1], 0)
queue = deque([start])
INF = 1e9
answer = -1
for t in range(2500):
    temp_water = []
    for x, y in water:
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if ground[nx][ny] != 0:
                continue
            ground[nx][ny] = 1
            temp_water.append((nx, ny))
    water.extend(temp_water)
    while queue and queue[0][2] == t:
        x, y, depth = queue.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if ground[nx][ny] == 0 and not visited[nx][ny]:
                queue.append((nx, ny, t + 1))
                visited[nx][ny] = True
            elif ground[nx][ny] == 5:
                answer = t + 1
                break
    if not queue:
        break

    if answer > 0:
        break

if answer < 0:
    print('KAKTUS')
else:
    print(answer)
