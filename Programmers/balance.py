
def solution(weight):
    answer = 0
    weight.sort()
    s = 0
    for w in weight:
        if s+1 < w:
            break
        s += w
    answer = s+1
    return answer


print(solution([3, 1, 6, 2, 7, 30, 1]))
