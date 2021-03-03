# kakao 2019 blind #2 # 실패율
# 정렬, 구현
# 난이도 하


def solution(N, stages):
    on_stage = [0 for _ in range(N+2)]
    cleared = [0 for _ in range(N+2)]

    failure_rate = []
    length = len(stages)
    for i in range(1, N+1):
        count = stages.count(i)
        if length == 0:
            fail = 0
        else:
            fail = count / length

        failure_rate.append((fail, i))
        length -= count

    print(failure_rate)

    failure_rate.sort(key=lambda t: t[0], reverse=True)
    answer = list(map(lambda t: t[1], failure_rate))
    return answer


N_ = 4
stages_ = [4,4,4,4,4]
print(solution(N_, stages_))
