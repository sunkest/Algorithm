# Floyd-Warshall
# BOJ 2610

INF = 10000000
N = int(input())
M = int(input())
graph = [[INF for _ in range(N)] for _ in range(N)]

for i in range(M):
    a, b = map(lambda x: int(x)-1, input().split())
    graph[a][b] = 1
    graph[b][a] = 1

for k in range(N):
    for u in range(N):
        for v in range(N):
            if graph[u][k] == INF or graph[k][v] == INF or u == v:
                continue
            graph[u][v] = min(graph[u][v], graph[u][k] + graph[k][v])

# group check
checked = [False for _ in range(N)]
representatives = []
for i in range(N):
    if checked[i]:
        continue
    group = [i]
    for j in range(N):
        dist = graph[i][j]
        if dist < INF:
            checked[j] = True
            group.append(j)

    rep = -1
    min_max_cost = 10000000
    for g in group:
        max_cost = -1
        for cost in graph[g]:
            if max_cost < cost < INF:
                max_cost = cost
        if min_max_cost > max_cost:
            rep = g
            min_max_cost = max_cost
    representatives.append(rep+1)
    # 결과에 index +1 해야 답

representatives.sort()
print(len(representatives))
for rep in representatives:
    print(rep)

