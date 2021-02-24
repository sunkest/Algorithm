# BOJ 18352 # Silver 2
# dfs/bfs
# 이것이 취업을 위한 코딩테스트다 - Part 3 - dfs/bfs
# 재귀없는 bfs 풀이
# BOJ 기준 input = sys.stdin.readline 안쓰면 시간초과남
import sys
from collections import deque

input = sys.stdin.readline

N, M, K, X = map(int, input().split())
graph = {n: [] for n in range(1, N+1)}
for _ in range(M):
    A, B = map(int, input().split())
    graph[A].append(B)

visit = [False for _ in range(N+1)]
queue = deque([(X, 0)])
visit[X] = True
answer = []

while queue:
    node, depth = queue.popleft()
    if depth == K:
        answer.append(node)
    for n in graph[node]:
        if visit[n]:
            continue
        queue.append((n, depth+1))
        visit[n] = True

answer.sort()
if answer:
    for a in answer:
        print(a)
else:
    print(-1)
