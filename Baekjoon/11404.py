# BOJ 11404 # 플로이드 # Gold 4
# Floyd-Warshall
# 이것이 취업을 위한 코딩테스트다 - Part 3 - 최단경로문제
import sys

input = sys.stdin.readline

n = int(input())
m = int(input())
graph = [[1e9] * (n+1) for _ in range(n+1)]
for _ in range(m):
    a, b, c = map(int, input().split())
    if c < graph[a][b]:
        graph[a][b] = c

for a in range(1, n+1):
    graph[a][a] = 0

for k in range(1, n+1):
    for a in range(1, n+1):
        for b in range(1, n+1):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

for a in range(1, n + 1):
    for b in range(1, n + 1):
        if graph[a][b] == 1e9:
            print(0, end=' ')
        else:
            print(graph[a][b], end=' ')
    print()