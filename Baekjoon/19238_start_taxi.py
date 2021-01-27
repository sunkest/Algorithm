# 표준 입력 예제
'''
a = int(input())                        정수형 변수 1개 입력 받는 예제
b, c = map(int, input().split())        정수형 변수 2개 입력 받는 예제
d = float(input())                      실수형 변수 1개 입력 받는 예제
e, f, g = map(float, input().split())   실수형 변수 3개 입력 받는 예제
h = input()                             문자열 변수 1개 입력 받는 예제
'''

# 표준 출력 예제
'''
a, b = 6, 3
c, d, e = 1.0, 2.5, 3.4
f = "ABC"
print(a)                                정수형 변수 1개 출력하는 예제
print(b, end = " ")                     줄바꿈 하지 않고 정수형 변수와 공백을 출력하는 예제
print(c, d, e)                          실수형 변수 3개 출력하는 예제
print(f)                                문자열 1개 출력하는 예제
'''

'''
N: map 사이즈
M: 승객 수
fuel: 연료량
'''
from collections import deque
import copy
dx = [1,-1,0,0]
dy = [0,0,1,-1]
TARGET = 10000
VISITED = -10000

def bfs_to_passenger(grid, start, fuel):
    queue = deque()
    if 0 < grid[start[0]][start[1]] < 10000:
        return start + [grid[start[0]][start[1]], 0]
    visit = copy.deepcopy(grid)  # 방문을 기록해도 됨. # 첫 방문 이외에는 최단거리가 아님.
    queue.append(start)
    dist = 0
    while queue:
        length = len(queue)
        found = []
        for _ in range(length):
            x, y = queue.popleft()
            visit[x][y] = VISITED
            if 0 < grid[x][y] < 10000:
                found.append([x, y, grid[x][y]])
            if found:
                continue
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if grid[nx][ny] == -1:
                    continue
                if visit[nx][ny] == VISITED:
                    continue
                else:
                    queue.append([nx, ny])

        if found:
            found.sort(key=lambda c: 100*c[0] + c[1])
            grid[found[0][0]][found[0][1]] = 0
            return found[0] + [dist]  # [x, y, 승객번호, 거리]

        dist += 1
        if dist > fuel:
            return None

    return None


def bfs_to_dest(grid, start, target, fuel):  # target: [x, y, 승객번호, _]
    queue = deque()
    queue.append(start)
    visit = [[-1 for _ in range(len(grid))] for _ in range(len(grid))]
    visit[start[0]][start[1]] = 0
    while queue:
        x, y = queue.popleft()
        if visit[x][y] >= fuel:
            return None
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if grid[nx][ny] == -1:
                continue
            if visit[nx][ny] != -1:
                continue
            queue.append([nx, ny])
            visit[nx][ny] = visit[x][y] + 1
            if grid[nx][ny] == TARGET + target[2]:
                grid[nx][ny] = 0
                return [nx, ny, visit[nx][ny]]

    return None


def solution():
    # 입력, grid박싱, grid에 승객위치표시//////////////////////////////////////////////////////////
    N, M, fuel = map(int, input().split())
    grid = []
    passengers = []  # 승객 [출발행, 출발열, 도착행, 도착열]
    for i in range(N):
        grid.append(list(map(lambda x: -int(x), input().split())))
    grid = list(map(lambda arr: [-1] + arr + [-1], grid))
    minus_ones = [-1] * (N+2)
    grid.append(minus_ones)
    grid.insert(0, minus_ones)
    start = list(map(int, input().split()))
    for i in range(M):
        p = list(map(int, input().split()))
        passengers.append(p)
        grid[p[0]][p[1]] = i + 1
        grid[p[2]][p[3]] = TARGET + i + 1
    # //////////////////////////////////////////////////////////////
    for _ in range(M):
        result_p = bfs_to_passenger(grid, start, fuel)
        if result_p is None:
            return -1
        px, py, p_num, fuel_to_passenger = result_p # [x, y, 승객번호, 거리]
        fuel -= fuel_to_passenger

        result_d = bfs_to_dest(grid, [px, py], result_p, fuel)  # [dest_x, dest_y, dist]
        if result_d is None:
            return -1
        fuel = fuel + result_d[2]

        start = [result_d[0], result_d[1]]

    return fuel

import sys
sys.stdin = open("input.txt", "r")

print(solution())
