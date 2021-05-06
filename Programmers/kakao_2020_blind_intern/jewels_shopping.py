from collections import defaultdict


def solution(gems):
    total_gems = defaultdict(lambda: 0)
    for gem in gems:
        total_gems[gem] += 1
    types = len(total_gems)

    left = 0
    right = 0
    current_gems = defaultdict(lambda: 0)
    current_gems[gems[left]] = 1
    gem_count = 1
    result = []
    while True:
        if gem_count < types:
            right += 1
            if right > len(gems) - 1:
                break
            gem = gems[right]
            if current_gems[gem] == 0:
                gem_count += 1
            current_gems[gem] += 1
        else:
            result.append((left, right))
            gem = gems[left]
            current_gems[gem] -= 1
            if current_gems[gem] == 0:
                gem_count -= 1
            left += 1
            if left > len(gems) - 1:
                break

    result.sort(key=lambda x: x[1] - x[0])
    return [result[0][0] + 1, result[0][1] + 1]


print(solution(["DIA", "RUBY", "RUBY", "DIA", "DIA", "EMERALD", "SAPPHIRE", "DIA"]))
