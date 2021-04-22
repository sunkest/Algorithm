import sys

input = sys.stdin.readline

n = int(input())
l = int(input())
recommendations = list(map(int, input().split()))

candidates = {}
for i, r in enumerate(recommendations):
    if candidates.get(r) is not None:
        candidates[r][0] += 1
        continue
    if len(candidates) < n:
        candidates[r] = [0, i]
    else:
        s = sorted(map(lambda x: [x, *candidates[x]], candidates.keys()), key=lambda x: x[1] * 10000 + i)
        least = s[0][0]
        candidates.pop(least)
        candidates[r] = [0, i]

print(*sorted(candidates.keys()))