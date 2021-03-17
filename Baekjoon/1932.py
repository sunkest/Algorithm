# BOJ 1932 # 정수 삼각형 # Silver 1
# DP
# 기초적인 DP형태
import sys
from copy import deepcopy

input = sys.stdin.readline

n = int(input())
triangle = []
for _ in range(n):
    triangle.append(list(map(int, input().split())))

d = deepcopy(triangle)

for i in range(1, n):
    row = triangle[i]
    for j in range(len(row)):
        if j == 0:
            up_left = 0
        else:
            up_left = d[i - 1][j - 1]
        if j == len(row) - 1:
            up = 0
        else:
            up = d[i - 1][j]
        d[i][j] = max(up, up_left) + triangle[i][j]

print(max(d[n - 1]))
