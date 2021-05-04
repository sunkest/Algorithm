import sys
INF = 1e9

input = sys.stdin.readline

n, s = map(int, input().split())
arr = list(map(int, input().split()))

min_range = INF
l, r = 0, 0
current_sum = arr[l]
while True:
    if current_sum >= s:
        min_range = min(min_range, r - l + 1)
        current_sum -= arr[l]
        l += 1
        if l > n - 1:
            break
    else:
        r += 1
        if r > n - 1:
            break
        current_sum += arr[r]


if min_range == INF:
    min_range = 0
print(min_range)
