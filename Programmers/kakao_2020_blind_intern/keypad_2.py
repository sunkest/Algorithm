ASTERISK = 10
HASH = 11
keypad = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [ASTERISK, 0, HASH]]

coords = {}
for i in range(len(keypad)):
    for j in range(len(keypad[i])):
        coords[keypad[i][j]] = (i, j)

LEFT_KEYS = {1, 4, 7}
RIGHT_KEYS = {3, 6, 9}


def get_distance(x1, y1, x2, y2):
    return abs(x1 - x2) + abs(y1 - y2)


def solution(numbers, hand):
    left = coords[ASTERISK]
    right = coords[HASH]
    answer = ''
    for num in numbers:
        if num in LEFT_KEYS:
            answer += 'L'
            left = coords[num]
        elif num in RIGHT_KEYS:
            answer += 'R'
            right = coords[num]
        else:
            left_distance = get_distance(*left, *coords[num])
            right_distance = get_distance(*right, *coords[num])
            if left_distance < right_distance:
                answer += 'L'
                left = coords[num]
            elif right_distance < left_distance:
                answer += 'R'
                right = coords[num]
            else:
                if hand == "left":
                    answer += 'L'
                    left = coords[num]
                elif hand == "right":
                    answer += 'R'
                    right = coords[num]

    return answer


print(solution([1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5], "right"))
