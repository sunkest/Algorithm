# BOJ 14502 # 연구소 # Gold 5
# 삼성 SW 역량테스트
# dfs/bfs, 완전탐색
# 이것이 취업을 위한 코딩테스트다 - part 3 - dfs/bfs
# 책 답안대로 내면 시간초과
# 아래 코드는 통과
import sys
from collections import deque
from itertools import combinations

input = sys.stdin.readline
N, M = map(int, input().split())

lab = [[1 for _ in range(M+2)] for _ in range(N+2)]
initial_virus = []
initial_safety = []
for i in range(1, N+1):
    row = list(map(int, input().split()))
    for j in range(M):
        lab[i][j+1] = row[j]
        if row[j] == 2:
            initial_virus.append((i, j+1))
        elif row[j] == 0:
            initial_safety.append((i, j+1))
initial_safety_count = len(initial_safety)

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

wall_combinations = list(combinations(initial_safety, 3))

max_safety = 0
for new_walls in wall_combinations:
    temp = [row[:] for row in lab]
    for wx, wy in new_walls:
        temp[wx][wy] = 1

    safety_count = initial_safety_count - 3
    #bfs
    for vx, vy in initial_virus:
        queue = deque([(vx, vy)])
        while queue:
            x, y = queue.popleft()
            for i in range(4):
                new_x = x + dx[i]
                new_y = y + dy[i]
                if temp[new_x][new_y] == 0:
                    queue.append((new_x, new_y))
                    temp[new_x][new_y] = 2
                    safety_count -= 1

    max_safety = max(max_safety, safety_count)

print(max_safety)