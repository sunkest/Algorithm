# kakao_2021_blind #6
# 구현, Simulation, 완전탐색
# 모든 방문순서마다 최단거리는 bfs로 계산하면서 완전탐색해도 시간내 가능
from itertools import permutations
from collections import deque
from copy import deepcopy

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]


def bfs(board, x1, y1, x2, y2):
    if x1 == x2 and y1 == y2:
        return 0
    queue = deque([(x1, y1, 0)])
    while queue:
        x, y, depth = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx == x2 and ny == y2:
                return depth + 1
            if nx < 0 or ny < 0 or nx > 3 or ny > 3:
                continue
            else:
                queue.append((nx, ny, depth+1))
        for i in [0, 2]:  # 가로 ctrl
            for n in range(1, 4):
                nx = x + n*dx[i]
                if nx > 3 or nx < 0:
                    break
                if nx == 3 or nx == 0 or board[nx][y] > 0:
                    if nx == x2 and y == y2:
                        return depth + 1
                    queue.append((nx, y, depth+1))
                    break
        for i in [1, 3]:  # 세로 ctrl
            for n in range(1, 4):
                ny = y + n*dy[i]
                if ny > 3 or ny < 0:
                    break
                if ny == 3 or ny == 0 or board[x][ny] > 0:
                    if x == x2 and ny == y2:
                        return depth + 1
                    queue.append((x, ny, depth+1))
                    break


def solution(board, r, c):
    cards = [[] for _ in range(7)]
    nums = set()
    for i in range(4):
        for j in range(4):
            card = board[i][j]
            if card == 0:
                continue
            nums.add(card)
            cards[card].append([i, j])

    orders = list(permutations(nums))
    answer = 10000

    for order in orders:
        temp_board = deepcopy(board)
        records = [(0, r, c)]

        for num in order:
            temp = []
            [x1, y1], [x2, y2] = cards[num]
            for count, cx, cy in records:
                # print(cx, cy, x1, y1, bfs(temp_board, cx, cy, x1, y1))
                # print(x1, y1, x2, y2, bfs(temp_board, x1, y1, x2, y2))
                # print(cx, cy, x2, y2, bfs(temp_board, cx, cy, x2, y2))
                # print(x2, y2, x1, y1, bfs(temp_board, x2, y2, x1, y1))
                route_ab = bfs(temp_board, cx, cy, x1, y1) + 1 + bfs(temp_board, x1, y1, x2, y2) + 1
                route_ba = bfs(temp_board, cx, cy, x2, y2) + 1 + bfs(temp_board, x2, y2, x1, y1) + 1
                temp.append((count+route_ab, x2, y2))
                temp.append((count+route_ba, x1, y1))
                records = temp[:]
            temp_board[x1][y1] = 0
            temp_board[x2][y2] = 0

        result = min(records)[0]
        if result < answer:
            answer = result
    return answer


_board = [[1, 0, 0, 3], [2, 0, 0, 0], [0, 0, 0, 2], [3, 0, 1, 0]]
_r = 1
_c = 0
print(solution(_board, _r, _c))
