from math import sqrt
K = int(input())

MAX = 400000
m = [0] * MAX
m[1] = 1

for i in range(1, MAX):
    j = 2*i
    while j < MAX:
        m[j] -= m[i]
        j += i

l = 1
r = 2000000000

while l < r:
    mid = (l+r)//2
    cur = 0
    for i in range(1, int(sqrt(mid)) + 1):
        cur += m[i] * (mid // (i**2))
    if cur < K:
        l = mid + 1
    elif cur > K:
        r = mid - 1
    else:
        r = mid

print(l)

