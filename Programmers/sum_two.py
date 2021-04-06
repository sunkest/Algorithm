from itertools import combinations


def solution(numbers):
    result = set()
    comb = combinations(numbers, 2)
    for a, b in comb:
        result.add(a + b)
    answer = sorted(list(result))
    return answer


print(solution([2, 1, 3, 4, 1]))
