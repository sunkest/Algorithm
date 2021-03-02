# BOJ 14888 # 연산자 끼워 넣기 # Silver 1
# 삼성 SW 역량테스트
# dfs/bfs, Simulation
# 이것이 취업을 위한 코딩테스트다 - part 3 - dfs/bfs
# dfs 풀이
import sys

maximum = -1e9
minimum = 1e9


def dfs(num, depth):
    global N, maximum, minimum, op
    if depth == N:
        maximum = max(maximum, num)
        minimum = min(minimum, num)
    else:
        if op[0] > 0:
            op[0] -= 1
            dfs(num + numbers[depth], depth + 1)
            op[0] += 1
        if op[1] > 0:
            op[1] -= 1
            dfs(num - numbers[depth], depth + 1)
            op[1] += 1
        if op[2] > 0:
            op[2] -= 1
            dfs(num * numbers[depth], depth + 1)
            op[2] += 1
        if op[3] > 0:     # 나눗셈시 // 연산말고 int(a/b)로 해야 C++과 똑같이나옴
            op[3] -= 1
            dfs(int(num/numbers[depth]), depth + 1)
            op[3] += 1


input = sys.stdin.readline
N = int(input())
numbers = list(map(int, input().split()))
op = list(map(int, input().split()))

dfs(numbers[0], 1)
print(maximum)
print(minimum)
