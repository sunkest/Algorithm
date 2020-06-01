from math import sqrt


def solution(brown, yellow):
    answer = []
    dv = []
    for i in range(1, int(sqrt(yellow))+1):
        if yellow % i == 0:
            dv.append((int(yellow/i), i))

    for a, b in dv:
        if (a+2)*(b+2) == brown+yellow:
            answer = [a+2, b+2]

    return answer


print(solution(24, 24))
