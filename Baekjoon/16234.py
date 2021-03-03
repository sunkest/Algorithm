# BOJ 16234 # 인구 이동 # Gold 5
# 삼성 SW 역량테스트
# dfs/bfs, Simulation
# 이것이 취업을 위한 코딩테스트다 - part 3 - dfs/bfs
# PyPy로 내도 1424ms, Python 으로 내면 시간초과
import sys
from collections import deque
input = sys.stdin.readline

N, L, R = map(int, input().split())
population = [[500] * (N+2) for _ in range(N+2)]
for i in range(N):
    row = list(map(int, input().split()))
    population[i+1][1:-1] = row

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

count = 0
while True:
    visited = [[False] * (N+2) for _ in range(N+2)]
    unions = []
    for i in range(1, N+1):
        for j in range(1, N+1):
            if visited[i][j]:
                continue
            # bfs
            queue = deque([(i, j)])
            union_total = population[i][j]
            union_members = [(i, j)]
            visited[i][j] = True
            while queue:
                x, y = queue.popleft()
                for r in range(4):
                    nx = x + dx[r]
                    ny = y + dy[r]
                    if visited[nx][ny]:
                        continue
                    if L <= abs(population[nx][ny] - population[x][y]) <= R:
                        queue.append((nx, ny))
                        visited[nx][ny] = True
                        union_total += population[nx][ny]
                        union_members.append((nx, ny))
            if len(union_members) > 1:
                unions.append((union_total, union_members))

    if len(unions) == 0:
        print(count)
        break

    for total_pop, members in unions:
        avg_pop = int(total_pop/len(members))
        for x, y in members:
            population[x][y] = avg_pop
    count += 1
