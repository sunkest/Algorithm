def solution(n, build_frame):
    columns = [[0 for _ in range(n + 2)] for _ in range(n + 2)]
    beams = [[0 for _ in range(n + 2)] for _ in range(n + 2)]

    for x, y, a, b in build_frame:
        if a == 0 and b == 1:  # 기둥 설치
            if check_valid_column(columns, beams, x, y):
                columns[x][y] = 1

        elif a == 1 and b == 1:  # 보 설치  # 이 경우 y=0이나, x=n은 주어지지 않음
            if check_valid_beam(columns, beams, x, y):
                beams[x][y] = 1

        elif a == 0 and b == 0:  # 기둥 삭제
            columns[x][y] = 0
            if beams[x][y + 1] == 1:  # 바로 위 보 점검  # y=n은 주어지지 않음
                if check_valid_beam(columns, beams, x, y + 1) is False:
                    columns[x][y] = 1
                    continue
            if beams[x - 1][y + 1] == 1:  # 위 왼쪽 보 점검  # y=n은 주어지지 않음  # x=0이면 항상 0
                if check_valid_beam(columns, beams, x - 1, y + 1) is False:
                    columns[x][y] = 1
                    continue
            if columns[x][y + 1] == 1:  # 위 기둥 점검  # y=n은 주어지지 않음
                if check_valid_column(columns, beams, x, y + 1) is False:
                    columns[x][y] = 1
                    continue

        elif a == 1 and b == 0:  # 보 삭제
            beams[x][y] = 0
            if columns[x][y] == 1:  # 같은 자리 기둥 점검
                if check_valid_column(columns, beams, x, y) is False:
                    beams[x][y] = 1
                    continue
            if columns[x + 1][y] == 1:  # 오른쪽 기둥 점검  # x=n인 경우 주어지지 않음
                if check_valid_column(columns, beams, x + 1, y) is False:
                    beams[x][y] = 1
                    continue
            if beams[x - 1][y] == 1:  # 왼쪽 보 점검  # x=0인 경우 항상 0
                if check_valid_beam(columns, beams, x - 1, y) is False:
                    beams[x][y] = 1
                    continue
            if beams[x + 1][y] == 1:  # 오른쪽 보 점검  # x=n인 경우 항상 0
                if check_valid_beam(columns, beams, x + 1, y) is False:
                    beams[x][y] = 1
                    continue

    answer = []
    for x in range(n + 1):
        for y in range(n + 1):
            if columns[x][y] == 1:
                answer.append([x, y, 0])
            if beams[x][y] == 1:
                answer.append([x, y, 1])
    return answer


def check_valid_column(columns, beams, x, y):
    if y == 0:  # 바닥
        return True
    if columns[x][y - 1] == 1:  # 기둥 위
        return True
    if beams[x][y] == 1:
        return True
    if beams[x - 1][y] == 1:  # 보의 한쪽 끝  # x=0일때 beams[-1][y]가 됨 = beams[n][y] = 항상 0
        return True
    return False


def check_valid_beam(columns, beams, x, y):
    if columns[x][y - 1] == 1 or columns[x + 1][y - 1] == 1:
        return True
    if beams[x - 1][y] == 1 and beams[x + 1][y] == 1:  # # x=0일때 beams[-1][y]가 됨 = beams[n][y] = 항상 0
        return True
    return False


# 벽면을 벗어나게 기둥, 보를 설치하는 경우는 없습니다.
# 바닥에 보를 설치 하는 경우는 없습니다.
# 구조물이 겹치도록 설치하는 경우와, 없는 구조물을 삭제하는 경우는 입력으로 주어지지 않습니다.

print(solution(5, [[0,0,0,1],[2,0,0,1],[4,0,0,1],[0,1,1,1],[1,1,1,1],[2,1,1,1],[3,1,1,1],[2,0,0,0],[1,1,1,0],[2,2,0,1]]))
