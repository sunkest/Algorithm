from collections import deque


def bfs(graph, root):
    visit = []
    dq = deque([root])
    while dq:
        node = dq.popleft()
        if node not in visit:
            visit.append(node)
            dq.extend(graph[node])
    return visit


def solution(n, computers):
    graph_list = {}
    for i in range(n):
        l = []
        for j in range(n):
            if computers[i][j] == 1 and j != i:
                l.append(j)
        graph_list[i] = l

    v = list(range(n))
    answer = 0
    while v:
        result = bfs(graph_list, v[0])
        for r in result:
            v.remove(r)
        answer += 1

    return answer


n = 3
computers = [[1, 1, 0], [1, 1, 1], [0, 1, 1]]
print(solution(n, computers))