# kakao 2020 blind #4 가사검색
# by 이진탐색 - 프로그래머스 기준 효율성테스트 111/138/130/6/5 ms
from bisect import *


def solution(words, queries):
    answer = []
    array = [[] for _ in range(10001)]
    reversed_array = [[] for _ in range(10001)]
    for word in words:
        array[len(word)].append(word)
        reversed_array[len(word)].append(word[::-1])

    for i in range(10001):
        array[i].sort()
        reversed_array[i].sort()

    for query in queries:
        length = len(query)
        if query[0] != '?':
            left = bisect_left(array[length], query.replace('?', 'a'))
            right = bisect_right(array[length], query.replace('?', 'z'))
            answer.append(right - left)
        else:
            left = bisect_left(reversed_array[length], query.replace('?', 'a')[::-1])
            right = bisect_right(reversed_array[length], query.replace('?', 'z')[::-1])
            answer.append(right - left)
    return answer


words_ = ["frodo", "front", "frost", "frozen", "frame", "kakao"]
queries_ = ["fro??", "????o", "fr???", "fro???", "pro?"]
print(solution(words_, queries_))