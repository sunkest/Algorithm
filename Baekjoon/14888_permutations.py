# BOJ 14888 # 연산자 끼워 넣기 # Silver 1
# 삼성 SW 역량테스트
# dfs/bfs, Simulation
# 이것이 취업을 위한 코딩테스트다 - part 3 - dfs/bfs
# permutations 풀이, 시간은 5배걸림
import sys
from itertools import permutations

input = sys.stdin.readline
N = int(input())
numbers = list(map(int, input().split()))
operators = list(map(int, input().split()))

ops = []
for i in range(4):
    ops += [i] * operators[i]

sequences = set(permutations(ops, N-1))

maximum = -1e9
minimum = 1e9

for seq in sequences:
    num = numbers[0]
    for i, op in enumerate(seq):
        if op == 0:
            num += numbers[i+1]
        elif op == 1:
            num -= numbers[i+1]
        elif op == 2:
            num *= numbers[i+1]
        elif op == 3:
            num = int(num/numbers[i+1])

    maximum = max(maximum, num)
    minimum = min(minimum, num)

print(maximum)
print(minimum)
