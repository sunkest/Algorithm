import sys

input = sys.stdin.readline


def rotate_square_counterclockwise(arr: list):  # 정사각형 n x n 2차원 배열에 대해 90도씩 세번 돌린 배열들 return
    size = len(arr)
    rotates = []
    rotates.append(arr[:])
    for n in range(3):
        new_arr = [[-1 for _ in range(size)] for _ in range(size)]
        before = rotates[n]
        center = (size - 1) / 2
        for x in range(size):
            for y in range(size):
                new_x = int(2 * center - y)
                new_y = x
                new_arr[new_x][new_y] = before[x][y]
        rotates.append(new_arr)
    return rotates


def getOrder(n):
    c = n // 2
    start = (c, c, 0)
    result = [start]
    # 0, 1, 2, 3
    # 좌,하,우,상
    dx = [0, 1, 0, -1]
    dy = [-1, 0, 1, 0]
    d = 0
    moves = 1
    move_count = 0
    while True:
        lx, ly, _ = result[-1]
        if lx == 0 and ly == -1:
            result.pop()
            break
        for _ in range(moves):
            nx = lx + dx[d]
            ny = ly + dy[d]
            result.append((nx, ny, d))
            lx, ly, _ = result[-1]
        d = (d + 1) % 4
        move_count += 1
        if move_count == 2:
            move_count = 0
            moves += 1
    return result


n = int(input())
sand = []
for _ in range(n):
    sand.append(list(map(int, input().split())))

portion_left = [[0, 0, 0.02, 0, 0], [0, 0.1, 0.07, 0.01, 0], [0.05, -1, 0, 0, 0], [0, 0.1, 0.07, 0.01, 0],
                [0, 0, 0.02, 0, 0]]
portions = rotate_square_counterclockwise(portion_left)

orders = getOrder(n)
answer = 0
for r, c, d in orders:

    s = sand[r][c]
    except_alpha = 0
    ar = 0
    ac = 0
    for i in range(5):
        for j in range(5):
            p = portions[d][i][j]
            nr = r + i - 2
            nc = c + j - 2
            if p < 0:
                ar = nr
                ac = nc
                continue
            elif p == 0:
                continue
            else:
                moved_sand = int(s * p)
                except_alpha += moved_sand

            if nr < 0 or nr > n - 1 or nc < 0 or nc > n - 1:
                answer += moved_sand
            else:
                sand[nr][nc] += moved_sand

    if ar < 0 or ar > n - 1 or ac < 0 or ac > n - 1:
        answer += s - except_alpha
    else:
        sand[ar][ac] += s - except_alpha

    sand[r][c] = 0

print(answer)
