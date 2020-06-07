
def solution(n, costs):
    answer = 0
    costs.sort()
    visited = set()
    visited.add(costs[0][0])
    for i in range(n-1):
        pool = []
        for c in costs:
            if c[0] in visited or c[1] in visited:
                if c[0] in visited and c[1] in visited:
                    continue
                pool.append(c)
        pool.sort(key=lambda x: x[2])
        answer += pool[0][2]
        visited.add(pool[0][0])
        visited.add(pool[0][1])
        costs.remove(pool[0])

    return answer


print(solution(4, [[0, 1, 1], [0, 2, 2], [1, 2, 5], [1, 3, 1], [2, 3, 8]]))
