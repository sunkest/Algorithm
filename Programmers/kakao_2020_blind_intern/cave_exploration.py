from collections import deque


def solution(n, path, order):
    keys = list(range(n))
    graph = {key: [] for key in keys}
    for a, b in path:
        graph[a].append(b)
        graph[b].append(a)

    # bfs
    directed_graph, indegrees = bfs(n, graph)

    # order 적용
    for a, b in order:
        directed_graph[a].append(b)
        indegrees[b] += 1

    # 위상정렬
    # answer = topological_sort(n, directed_graph, indegrees)

    # dfs
    answer = dfs(n, directed_graph)

    return answer


def bfs(n, graph):
    directed_graph = {key: [] for key in graph.keys()}
    visit = [True for _ in range(n)]
    queue = deque([0])
    indegrees = dict.fromkeys(graph.keys(), 0)

    while queue:
        current_node = queue.popleft()
        if visit[current_node]:
            visit[current_node] = False
            queue.extend(graph[current_node])
            child_nodes = list(filter(lambda child: visit[child], graph[current_node]))
            directed_graph[current_node].extend(child_nodes)
            for child in child_nodes:
                indegrees[child] += 1

    return directed_graph, indegrees


def topological_sort(n, graph: dict, indegrees: dict):
    queue = deque()
    result = []
    keys = list(indegrees.keys())
    num_of_nodes = n

    while len(result) < num_of_nodes:
        for key in keys:
            if indegrees[key] == 0:
                queue.append(key)
                keys.remove(key)

        if len(queue) == 0:
            return False

        popped_node = queue.popleft()
        result.append(popped_node)
        edges_to_delete = graph[popped_node]
        for edge in edges_to_delete:
            indegrees[edge] -= 1

    return True


path_ = [[0, 1], [0, 3], [0, 7], [8, 1], [3, 6], [1, 2], [4, 7], [7, 5]]
order_ = [[4, 1], [8, 7], [6, 5]]
print(solution(9, path_, order_))
