x, y = map(int, input().split())
z = int((y * 100) / x)
if z >= 99:
    print(-1)
else:
    l = 1
    r = 1000000000
    while l <= r:
        mid = (l + r) // 2
        nx, ny = x + mid, y + mid
        value = int(100 * ny / nx)
        if value > z:
            r = mid - 1
        else:
            l = mid + 1
    print(r + 1)
