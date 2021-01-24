from collections import deque


def topological_sort(graph: dict, indegrees: dict):
    queue = deque()
    result = []
    keys = list(indegrees.keys())
    num_of_nodes = len(keys)

    while len(result) < num_of_nodes:
        for key in keys:
            if indegrees[key] == 0:
                queue.append(key)
                keys.remove(key)

        if len(queue) == 0:
            return ['Impossible']

        popped_node = queue.popleft()
        result.append(popped_node)
        edges_to_delete = graph[popped_node]
        for edge in edges_to_delete:
            indegrees[edge] -= 1

    return result


# graph는 모두 입력받았고, 입력 과정에서 indegree도 체크했다고 가정
g = {'A': ['B', 'C'], 'B': ['D', 'E'], 'C': ['E', 'F'], 'D': [], 'E': [], 'F': ['B']}
ind = {'A': 0, 'B': 2, 'C': 1, 'D': 1, 'E': 2, 'F': 1}

print(topological_sort(g, ind))
