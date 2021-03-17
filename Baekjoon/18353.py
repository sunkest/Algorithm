# BOJ 18353 # 병사 배치하기 # Silver 2
# DP # LIS(Longest Increasing Subsequence, 최장 증가 부분 수열)
# DP 개념을 사용하는 대표적인 알고리즘인 LIS 문제

import sys
from bisect import bisect_left

input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
arr.reverse()

lis = [arr[0]]
for i in range(1, len(arr)):
    index = bisect_left(lis, arr[i])
    if index == len(lis):
        lis.append(arr[i])
    else:
        lis[index] = arr[i]

print(n - len(lis))
