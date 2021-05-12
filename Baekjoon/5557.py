# BOJ 5557 1학년 # Gold 5
import sys

input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
target = arr[-1]

dp = [[0] * 21 for _ in range(n)]
dp[0][arr[0]] = 1

for i in range(1, n - 1):
    current = arr[i]
    for k in range(21):
        if k + current <= 20:
            dp[i][k + current] += dp[i - 1][k]
        if k - current >= 0:
            dp[i][k - current] += dp[i - 1][k]

print(dp[n - 2][target])
