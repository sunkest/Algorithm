ASTERISK = 10
HASH = 11

keypad = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [ASTERISK, 0, HASH]]
coord = [[0, 0] for _ in range(12)]
for i in range(4):
    for j in range(3):
        coord[keypad[i][j]] = [i, j]

LEFT = [1, 4, 7]
RIGHT = [3, 6, 9]
CENTER = [2, 5, 8, 0]


def get_distance(current, target):
    return abs(current[0] - target[0]) + abs(current[1] - target[1])


def solution(numbers, hand):
    answer = ''
    left = coord[ASTERISK]
    right = coord[HASH]
    for n in numbers:
        if n in LEFT:
            left = coord[n]
            answer += 'L'
        elif n in RIGHT:
            right = coord[n]
            answer += 'R'
        else:
            dist_left = get_distance(left, coord[n])
            dist_right = get_distance(right, coord[n])
            if dist_left < dist_right:
                left = coord[n]
                answer += 'L'
            elif dist_left > dist_right:
                right = coord[n]
                answer += 'R'
            else:
                if hand == 'left':
                    left = coord[n]
                    answer += 'L'
                else:
                    right = coord[n]
                    answer += 'R'

    return answer


number = [1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5]
hand = "right"
print(solution(number, hand))
