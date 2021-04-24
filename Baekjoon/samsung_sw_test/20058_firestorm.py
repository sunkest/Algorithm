import sys
from collections import deque

input = sys.stdin.readline

n, q = map(int, input().split())
size = 2 ** n
board = [[0] * (size + 2) for _ in range(size + 2)]
for i in range(1, size + 1):
    row = list(map(int, input().split()))
    for j in range(1, size + 1):
        board[i][j] = row[j - 1]

levels = list(map(int, input().split()))


def rotate_zip_clockwise(arr):  # 시계방향 90
    rotated = list(map(list, zip(*arr[::-1])))
    return rotated


dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

for level in levels:
    # divide, rotate
    if level > 0:
        p = 2 ** level
        for i in range(1, size + 1, p):
            for j in range(1, size + 1, p):
                to_rotate = [row[j:j + p] for row in board[i:i + p]]
                rotated = rotate_zip_clockwise(to_rotate)
                for r in range(p):
                    for c in range(p):
                        board[i + r][j + c] = rotated[r][c]

    # ice melts
    ices = [list(map(lambda x: x > 0, row)) for row in board]
    for r in range(1, size + 1):
        for c in range(1, size + 1):
            if board[r][c] == 0:
                continue
            ice_count = 0
            for i in range(4):
                nr, nc = r + dx[i], c + dy[i]
                if ices[nr][nc]:
                    ice_count += 1
            if ice_count < 3:
                board[r][c] -= 1

# sum
sum_ices = sum(map(lambda x: sum(x), board))

# bfs
visited = [[False] * (size + 2) for _ in range(size + 2)]
max_chunk = 0
for r in range(1, size + 1):
    for c in range(1, size + 1):
        if visited[r][c]:
            continue
        if board[r][c] == 0:
            continue
        queue = deque([(r, c)])
        visited[r][c] = True
        chunk = 1
        while queue:
            x, y = queue.popleft()
            for i in range(4):
                nx, ny = x + dx[i], y + dy[i]
                if visited[nx][ny]:
                    continue
                if board[nx][ny] == 0:
                    continue
                queue.append((nx, ny))
                visited[nx][ny] = True
                chunk += 1
        if chunk > max_chunk:
            max_chunk = chunk

print(sum_ices)
print(max_chunk)
