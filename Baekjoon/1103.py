import sys
sys.setrecursionlimit(1000000)
input = sys.stdin.readline

n, m = map(int, input().split())
board = []

for i in range(n):
    string = input()
    row = []
    for j in range(m):
        if string[j] == 'H':
            row.append(-1)
        else:
            row.append(int(string[j]))
    board.append(row)

memo = [[-1] * m for _ in range(n)]
visited = [[False] * m for _ in range(n)]
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

visited[0][0] = True
loop = False


def dfs(x, y, depth):
    global loop
    if loop:
        return -1
    if memo[x][y] >= 0:
        return depth + memo[x][y]

    value = board[x][y]
    maximum = -1
    for i in range(4):
        nx = x + dx[i] * value
        ny = y + dy[i] * value
        if nx < 0 or ny < 0 or nx > n - 1 or ny > m - 1:
            continue
        if visited[nx][ny]:
            loop = True
            return -1
        if board[nx][ny] < 0:
            continue
        visited[nx][ny] = True
        result = dfs(nx, ny, depth + 1)
        visited[nx][ny] = False
        if result > maximum:
            maximum = result

    if loop:
        return -1

    if maximum < 0:
        memo[x][y] = 1
        return depth + 1

    memo[x][y] = maximum - depth
    return maximum


answer = dfs(0, 0, 0)

print(answer)
