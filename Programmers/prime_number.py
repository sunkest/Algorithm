from itertools import permutations
from math import sqrt


def prime(x):
    if x == 1:
        return False
    for i in range(2, int(sqrt(x)) + 1):
        if x % i == 0:
            return False
    return True

def solution(numbers):
    answer = 0
    arr = []
    perm = []
    for n in numbers:
        arr.append(n)
    for i in range(len(arr)):
        pp = permutations(arr, i+1)
        perm.extend(pp)
    perm = set(perm)
    for p in perm:
        if p[0] == '0':
            continue
        num = int(''.join(p))
        if prime(num):
            answer += 1

    return answer


inp = "17"
print(solution(inp))
