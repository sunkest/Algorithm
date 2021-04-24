def flip_zip_diagonal(arr):  # 좌상-우하 대각선 기준 대칭
    rotated = list(map(list, zip(*arr[::1])))
    return rotated


def rotate_zip_clockwise(arr):  # 시계방향 90
    rotated = list(map(list, zip(*arr[::-1])))
    return rotated


arr = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 1, 2, 3, 4, 5, 6, 7, 8, 0], [0, 8, 7, 6, 5, 4, 3, 2, 1, 0],
       [0, 1, 2, 3, 4, 5, 6, 7, 8, 0], [0, 8, 7, 6, 5, 4, 3, 2, 1, 0], [0, 1, 2, 3, 4, 5, 6, 7, 8, 0],
       [0, 8, 7, 6, 5, 4, 3, 2, 1, 0], [0, 1, 2, 3, 4, 5, 6, 7, 8, 0], [0, 8, 7, 6, 5, 4, 3, 2, 1, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

