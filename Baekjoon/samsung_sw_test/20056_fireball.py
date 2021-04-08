import sys

# 시간초과남 다시생각

input = sys.stdin.readline

N, M, K = map(int, input().split())

board = [[[] for _ in range(N)] for _ in range(N)]
fireballs = []
count = M

for i in range(M):
    r, c, m, s, d = map(int, input().split())
    fireballs.append([r - 1, c - 1, m, s, d])
    board[r - 1][c - 1].append(i)

dr = [-1, -1, 0, 1, 1, 1, 0, -1]
dc = [0, 1, 1, 1, 0, -1, -1, -1]
for k in range(K):
    merge = set()
    for i in range(count):
        r, c, m, s, d = fireballs[i]
        if d < 0:
            continue
        nr = (r + dr[d] * s) % N
        nc = (c + dc[d] * s) % N
        board[r][c].remove(i)
        board[nr][nc].append(i)
        if len(board[nr][nc]) >= 2:
            merge.add((nr, nc))
        fireballs[i] = [nr, nc, m, s, d]

    for r, c in list(merge):
        balls = board[r][c]
        if len(balls) < 2:
            continue

        odds = list(filter(lambda x: fireballs[x][4] % 2 == 1, balls))
        if len(odds) == 0 or len(odds) == len(balls):  # 0246
            directions = [0, 2, 4, 6]
        else:  # 1357
            directions = [1, 3, 5, 7]

        mass_sum = 0
        speed_sum = 0
        for i in balls:
            mass_sum += fireballs[i][2]
            speed_sum += fireballs[i][3]
            fireballs[i][4] = -1

        new_mass = int(mass_sum / 5)
        new_speed = int(speed_sum / len(balls))
        if new_mass == 0:
            board[r][c] = []
            continue

        temp_balls = []
        for n in range(4):
            temp_balls.append(count + n)
        board[r][c] = temp_balls
        count = count + 4

        temp_info = list(map(lambda x: [r, c, new_mass, new_speed, x], directions))
        fireballs.extend(temp_info)

answer = 0
for r in range(N):
    for c in range(N):
        balls = board[r][c]
        for i in balls:
            answer += fireballs[i][2]

print(answer)
