import heapq
import sys

input = sys.stdin.readline
INF = int(1e9)

n, m = map(int, input().split())  # 노드개수, 간선개수
start = int(input())  # 시작노드
graph = [[] for _ in range(n + 1)]
distance = [INF] * (n + 1)  # 0번 인덱스는 padding


for _ in range(m):  # 간선 입력, a에서 b까지 비용c
    a, b, c = map(int, input().split())
    graph[a].append((b, c))


def dijkstra(start):
    queue = []
    heapq.heappush(queue, (0, start))
    distance[start] = 0
    while queue:
        dist, node = heapq.heappop(queue)
        if distance[node] < dist:
            continue
        for new_node, cost in graph[node]:
            new_cost = cost + dist
            if new_cost < distance[new_node]:
                distance[new_node] = new_cost
                heapq.heappush(queue, (new_cost, new_node))


dijkstra(start)
print(distance)

# 입력 예시
# 6 11
# 1
# 1 2 2
# 1 3 5
# 1 4 1
# 2 3 3
# 2 4 2
# 3 2 3
# 3 6 5
# 4 3 3
# 4 5 1
# 5 3 1
# 5 6 2
