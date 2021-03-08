# BOJ 1715 카드 정렬하기 # Gold 4
# 그리디 # 정렬 # 우선순위 큐
# 이것이 취업을 위한 코딩테스트다 - part 3 - 정렬

from heapq import *
import sys
input = sys.stdin.readline

N = int(input())
pq = []
for _ in range(N):
    heappush(pq, int(input()))

total = 0
while len(pq) > 1:
    a1 = heappop(pq)
    a2 = heappop(pq)
    heappush(pq, a1+a2)
    total += a1+a2

print(total)