def solution(key, lock):
    M = len(key)
    N = len(lock)
    pad = M-1
    padded_lock = [[2 for _ in range(N+2*pad)] for _ in range(N+2*pad)]
    num_zeros = 0
    for i in range(N):
        for j in range(N):
            padded_lock[i + pad][j + pad] = lock[i][j]
            if lock[i][j] == 0:
                num_zeros += 1

    rotated_keys = rotate_counterclockwise(key)
    for rotated_key in rotated_keys:
        for top_left_x in range(N+pad):
            for top_left_y in range(N+pad):
                filled = 0
                flag_wrong = False
                for dx in range(M):
                    for dy in range(M):
                        x = top_left_x + dx
                        y = top_left_y + dy
                        if padded_lock[x][y] == 2:
                            continue
                        elif padded_lock[x][y] + rotated_key[dx][dy] > 1:
                            flag_wrong = True
                            break
                        elif padded_lock[x][y] == 0 and rotated_key[dx][dy] == 1:
                            filled += 1
                if flag_wrong:
                    continue
                else:
                    if num_zeros == filled:
                        return True

    return False


def rotate_counterclockwise(arr: list):
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

key_ = [[0, 0, 0], [1, 0, 0], [0, 1, 1]]
lock_ = [[1, 1, 1], [1, 1, 0], [1, 0, 1]]
print(solution(key_, lock_))
