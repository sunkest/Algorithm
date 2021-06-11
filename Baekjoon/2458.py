# BOJ 2458 # 키 순서
# floyd-warshall
from collections import deque
import sys

input = sys.stdin.readline

INF = int(1e9)
n, m = map(int, input().split())
graph = [[INF] * (n + 1) for _ in range(n + 1)]  # 0번 인덱스는 padding

# 간선 입력
for _ in range(m):
    # a에서 b까지 비용c
    a, b = map(int, input().split())
    graph[a][b] = 1

# Floyd-Warshall
for k in range(1, n + 1):
    for a in range(1, n + 1):
        for b in range(1, n + 1):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

answer = 0
for i in range(1, n + 1):
    count = 0
    for j in range(1, n + 1):
        if graph[i][j] < INF or graph[j][i] < INF:     # 유향그래프기 때문에 a에서 b로 갈 수 있는 거랑 b에서 a로 올 수 있는 것도 포함해야함
            count += 1
    if count == n - 1:
        answer += 1

print(answer)
