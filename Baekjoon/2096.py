import sys

input = sys.stdin.readline

n = int(input())

# 메모리 제한이 빡세서 dp배열 크게하면 초과
# 슬라이딩 윈도우 해야함
row = list(map(int, input().split()))
dp_max = row[:]
dp_min = row[:]

for i in range(1, n):
    row = list(map(int, input().split()))
    max_temp = [0, 0, 0]
    min_temp = [0, 0, 0]
    for j in range(3):
        max_candi = []
        min_candi = []
        for k in range(-1, 2):
            if 0 <= j + k <= 2:
                max_candi.append(dp_max[j + k])
                min_candi.append(dp_min[j + k])
        max_temp[j] = max(max_candi) + row[j]
        min_temp[j] = min(min_candi) + row[j]
    dp_max = max_temp
    dp_min = min_temp

print(max(dp_max), min(dp_min))
