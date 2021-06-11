# BOJ 5569 출근 경로 # Gold 5
# DP

w, h = map(int, input().split())
dp = [[[[0, 0], [0, 0]] for _ in range(h)] for _ in range(w)]

for i in range(w):
    dp[i][0][0][0] = 1
for j in range(h):
    dp[0][j][1][1] = 1
dp[0][0] = [[0, 0], [0, 0]]

for i in range(1, w):
    for j in range(1, h):
        dp[i][j][0][0] = dp[i - 1][j][0][0] + dp[i - 1][j][1][0]
        dp[i][j][1][0] = dp[i - 1][j][1][1]
        dp[i][j][0][1] = dp[i][j - 1][0][0]
        dp[i][j][1][1] = dp[i][j - 1][1][1] + dp[i][j - 1][0][1]

answer = 0
for p in range(2):
    for q in range(2):
        answer += dp[w-1][h-1][p][q]
print(answer % 100000)
