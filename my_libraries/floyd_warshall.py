import sys

input = sys.stdin.readline

INF = int(1e9)
n, m = map(int, input().split())
graph = [[INF] * (n + 1) for _ in range(n + 1)]  # 0번 인덱스는 padding

# 자기 자신으로 가는 비용 0으로 초기화
for a in range(1, n + 1):
    for b in range(1, n + 1):
        if a == b:
            graph[a][b] = 0

# 간선 입력
for _ in range(m):
    # a에서 b까지 비용c
    a, b, c = map(int, input().split())
    graph[a][b] = c

# Floyd-Warshall
for k in range(1, n + 1):
    for a in range(1, n + 1):
        for b in range(1, n + 1):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

print(graph)

# 입력 예시
# 4 7
# 1 2 4
# 1 4 6
# 2 1 3
# 2 3 7
# 3 1 5
# 3 4 4
# 4 3 2
