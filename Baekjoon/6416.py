import sys
from collections import defaultdict

input = sys.stdin.readline


def is_tree(children: defaultdict, parent: defaultdict, nodes: set):
    count = 0
    root = -1
    for node in nodes:
        if node not in parent:
            count += 1
            root = node

    if count != 1:
        return False

    for node in parent.keys():
        parent_nodes = parent[node]
        if len(parent_nodes) != 1:
            return False

    stack = [root]
    visited = defaultdict(lambda: 0)
    visited[root] += 1
    while stack:
        node = stack.pop()
        child_nodes = children[node]
        for child in child_nodes:
            if visited[child] > 0:
                return False
            visited[child] += 1
            stack.append(child)

    unvisited = list(filter(lambda x: visited[x] < 1, visited.keys()))
    if len(unvisited) > 0:
        return False

    return True


k = 1
t_flag = True
while t_flag:
    children = defaultdict(lambda: [])
    parent = defaultdict(lambda: [])
    nodes = set()
    u_flag = True
    while u_flag:
        buf = input().rstrip().split("  ")
        if buf[0] == '':
            continue
        for pair in buf:
            u, v = map(int, pair.split())
            if u == 0:
                u_flag = False
                break
            elif u < 0:
                t_flag = False
                u_flag = False
                break

            children[u].append(v)
            parent[v].append(u)
            nodes.add(u)
            nodes.add(v)

    if not t_flag:
        break

    if len(nodes) == 0:
        print(f"Case {k} is a tree.")
        k += 1
        continue

    answer = is_tree(children, parent, nodes)
    if answer:
        print(f"Case {k} is a tree.")
    else:
        print(f"Case {k} is not a tree.")

    k += 1
