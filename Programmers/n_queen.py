answer = 0


def dfs(n, row, board):
    global answer
    if check_available(row, board):
        if row == n:
            answer += 1
            return
        for i in range(1, n + 1):
            board[row + 1] = i
            dfs(n, row + 1, board)


def check_available(row, board):
    for k in range(1, row):
        if board[row] == board[k] or abs(board[row] - board[k]) == row - k:
            return False
    return True


def solution(n):
    global answer

    board = [-1 for _ in range(n+1)]
    dfs(n, 0, board)

    return answer


print(solution(3))
