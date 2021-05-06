import sys

sys.setrecursionlimit(1000000)


def set_directed_graph(graph, directed_graph, node, parent_node):
    for next_node in graph[node]:
        # 트리로 주어지는 조건이라 이렇게 가능, 보통은 dfs로 visited 해서 해야할듯?
        if next_node == parent_node:
            continue
        directed_graph[node].append(next_node)
        set_directed_graph(graph, directed_graph, next_node, node)


def dfs(directed_graph, visited, node):
    if visited[node] >= 0:
        if visited[node] == 0:
            return False
        return True

    visited[node] = 0
    for next_node in directed_graph[node]:
        if not dfs(directed_graph, visited, next_node):
            return False

    visited[node] = 1
    return True


def solution(n, path, order):
    directed_graph = [[] for _ in range(n)]
    graph = [[] for _ in range(n)]
    keys = list(range(n))
    for a, b in path:
        graph[a].append(b)
        graph[b].append(a)

    set_directed_graph(graph, directed_graph, 0, -1)
    for a, b in order:
        directed_graph[a].append(b)

    # cycle 확인
    visited = [-1] * n
    return dfs(directed_graph, visited, 0)


n = 9
path = [[0, 1], [0, 3], [0, 7], [8, 1], [3, 6], [1, 2], [4, 7], [7, 5]]
order = [[8, 5], [6, 7], [4, 1]]
print(solution(n, path, order))
