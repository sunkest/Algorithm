# BOJ 1717 집합의 표현 # Gold 4
# 서로소 집합 Disjoint Set # Union Find

import sys

sys.setrecursionlimit(100000)
input = sys.stdin.readline


def find(parent, x):
    if parent[x] != x:
        parent[x] = find(parent, parent[x])
    return parent[x]


def union(parent, a, b):
    a = find(parent, a)
    b = find(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b


n, m = map(int, input().split())
parents = [i for i in range(n + 1)]

for _ in range(m):
    t, a, b = map(int, input().split())
    if t == 0:
        union(parents, a, b)
    elif t == 1:
        if find(parents, a) == find(parents, b):
            print("YES")
        else:
            print("NO")
