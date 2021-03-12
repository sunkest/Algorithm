# kakao_2021_blind #4 # 효율성포함
# 그래프, 경로
# Dijkstra, Floyd-Warshall 모두 가능
# 둘중에 어느게 빠를지는 구현에따라 조금씩 달라질듯? 이론상으로는 Floyd가 여기서는 빠름
# Floyd로 풀이
# 그래프가 방향에 관계없이 값이 비용이 같기때문에 전부다 볼 필요가 없음. - 전부다 보면 효율성 TC 하나 시간초과남..
# 2차원배열의 위쪽 반만 보면됨.
# 알고리즘이 준비가 되어있다는 가정하에는 시험때 생각보다 빨리 해결가능한 문제
import sys

input = sys.stdin.readline
INF = int(1e9)


def solution(n, s, a, b, fares):
    graph = [[INF] * (n + 1) for _ in range(n + 1)]  # 0번 인덱스는 padding
    for i in range(1, n + 1):
        graph[i][i] = 0

    for c, d, f in fares:
        graph[c][d] = f
        graph[d][c] = f

    for k in range(1, n + 1):
        for p in range(1, n + 1):
            for q in range(p, n + 1):
                graph[p][q] = min(graph[p][q], graph[p][k] + graph[k][q])
                graph[q][p] = graph[p][q]

    total_fare = INF
    for m in range(1, n + 1):
        total_fare = min(total_fare, graph[s][m] + graph[m][a] + graph[m][b])

    return total_fare


_n = 6
_s = 4
_a = 5
_b = 6
_fares = [[2, 6, 6], [6, 3, 7], [4, 6, 7], [6, 5, 11], [2, 5, 12], [5, 3, 20], [2, 4, 8], [4, 3, 9]]
print(solution(_n, _s, _a, _b, _fares))
