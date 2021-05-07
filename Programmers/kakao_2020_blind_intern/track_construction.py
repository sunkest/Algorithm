from collections import deque

INF = 1e9


def solution(board):
    n = len(board)
    padded_board = [[1 for _ in range(n + 2)]]
    padded_board.extend(list(map(lambda row: [1] + row + [1], board)))
    padded_board.append([1 for _ in range(n + 2)])
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]

    queue = deque([(1, 1, 1, 0), (1, 1, 2, 0)])
    result = [[INF for _ in range(n + 2)] for _ in range(n + 2)]
    result[1][1] = 0
    while queue:
        x, y, d, cost = queue.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if nx == x and ny == y:  # 왔던 칸
                continue
            if padded_board[nx][ny] == 1:
                continue
            if d == i:  # 직진
                new_cost = cost + 100
            else:  # 회전
                new_cost = cost + 600
            if result[nx][ny] < new_cost:
                continue
            result[nx][ny] = new_cost
            queue.append((nx, ny, i, new_cost))

    answer = result[n][n]
    for row in result:
        for value in row:
            print('{: >12}'.format(value), end=' ')
        print()
    print()
    return answer


print(solution([[0, 0, 0, 0, 0, 0, 0, 1], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 1, 0, 0], [0, 0, 0, 0, 1, 0, 0, 0],
                [0, 0, 0, 1, 0, 0, 0, 1], [0, 0, 1, 0, 0, 0, 1, 0], [0, 1, 0, 0, 0, 1, 0, 0],
                [1, 0, 0, 0, 0, 0, 0, 0]]))
