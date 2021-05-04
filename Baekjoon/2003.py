import sys
input = sys.stdin.readline

n, m = map(int, input().split())
arr = list(map(int, input().split()))

l, r = 0, 0
current_sum = arr[l]
count = 0
while True:
    if current_sum < m:
        r += 1
        if r > n - 1:
            break
        current_sum += arr[r]
    else:
        if current_sum == m:
            count += 1
        current_sum -= arr[l]
        l += 1
        if l > n - 1:
            break

print(count)
