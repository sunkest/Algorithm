def rotate_square_counterclockwise(arr: list): # 정사각형 n x n 2차원 배열에 대해 90도씩 세번 돌린 배열들 return
    size = len(arr)
    rotates = []
    rotates.append(arr[:])
    for n in range(3):
        new_arr = [[-1 for _ in range(size)] for _ in range(size)]
        before = rotates[n]
        center = (size-1)/2
        for x in range(size):
            for y in range(size):
                new_x = int(2*center - y)
                new_y = x
                new_arr[new_x][new_y] = before[x][y]
        rotates.append(new_arr)
    return rotates


def rotate_matrix_90_clockwise(arr:list):
    row_length = len(arr)
    column_length = len(arr[0])

    rotated_matrix = [[0 for _ in range(row_length)] for _ in range(column_length)]
    for row in range(row_length):
        for column in range(column_length):
            rotated_matrix[column][row_length - 1 - row] = arr[row][column]

    return rotated_matrix