
def solution(answers):
    answer = []
    pick = [(1, 2, 3, 4, 5), (2, 1, 2, 3, 2, 4, 2, 5), (3, 3, 1, 1, 2, 2, 4, 4, 5, 5)]
    score = [0, 0, 0]
    for i in range(3):
        p = pick[i]
        j = 0
        for an in answers:
            if an == p[j]:
                score[i] += 1
            j += 1
            if j == len(p):
                j = 0

    m = 0
    for i in range(3):
        if m <= score[i]:
            if m < score[i]:
                answer.clear()
            answer.append(i+1)
            m = score[i]

    return answer


a = [1, 3, 2, 4, 2]

print(solution(a))