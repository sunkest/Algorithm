from itertools import permutations

# 이동 방향과는 상관 없이
# 직선으로 펴서 순서대로만 한방향으로 나열해도 모두 커버됨
# 단, 직선의 경우의 수는 모두 따져야함
def solution(n, weak, dist):
    dist_perm = []
    for i in range(1, len(dist)+1):
        perm_n = list(permutations(dist, i))
        dist_perm.extend(perm_n)

    answer = 100
    rotated_weak = weak[:]
    rotated_weaks = []
    for _ in range(len(weak)):
        rotated_weaks.append(rotated_weak[:])
        rotated_weak.append(rotated_weak[0] + n)
        rotated_weak = rotated_weak[1:]

    for _ in range(len(weak)):  # 직선으로 펼치며 시작점 조정
        for perm in dist_perm:
            perm_idx = 0
            current_spot = 0
            for weak_spot in rotated_weak:
                if perm_idx >= len(perm):
                    break
                if current_spot >= weak_spot:
                    continue
                current_spot = weak_spot + perm[perm_idx]
                if current_spot >= rotated_weak[-1]:
                    break
                perm_idx += 1
            if current_spot < rotated_weak[-1]:
                continue
            if answer > perm_idx + 1:
                answer = perm_idx + 1

        # 시작점 조정
        rotated_weak.append(rotated_weak[0] + n)
        rotated_weak = rotated_weak[1:]
    if answer == 100:
        return -1
    return answer


n_ = 12
weak_ = [1, 3, 4, 9, 10]
dist_ = [3, 5, 7]
print(solution(n_, weak_, dist_))
