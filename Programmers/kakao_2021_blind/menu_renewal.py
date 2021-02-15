# kakao_2021_blind #2
# 완전탐색, 조합
# Counter 사용시 코드 간결해짐
from itertools import combinations


def solution(orders, course):
    answer = []
    combination_pool = {num: set() for num in course}
    for order in orders:
        order = sorted(order)
        for num in course:
            comb = combinations(order, num)
            for c in comb:
                combination_pool[num].add(c)

    for num in course:
        max_ordered = 0
        max_courses = []
        for comb in combination_pool[num]:
            ordered = 0
            for order in orders:
                flag = True
                for menu in comb:
                    if menu not in order:
                        flag = False
                        break
                if flag:
                    ordered += 1
            if ordered >= 2:
                if ordered == max_ordered:
                    max_courses.append(''.join(sorted(list(comb))))
                elif ordered > max_ordered:
                    max_ordered = ordered
                    max_courses = [''.join(sorted(list(comb)))]
        answer.extend(max_courses)
    answer.sort()

    return answer


orders_ = ["XYZ", "XWY", "WXA"]
course_ = [2, 3, 4]
print(solution(orders_, course_))
