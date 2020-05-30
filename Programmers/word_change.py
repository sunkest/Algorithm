from collections import deque
def dfs(graph, root, target_num, depth):
    visit = []
    dq = deque([root])
    node_num = dict()   # 층별 노드수
    node_num[0] = 1
    count = 0
    while dq:
        node = dq.popleft()
        count += 1
        if node == target_num:
            return depth
        if node not in visit:
            visit.append(node)
            dq.extend(graph[node])
            if node_num.get(depth+1) is None:
                node_num[depth + 1] = len(graph[node])
            else:
                node_num[depth + 1] += len(graph[node])
        if count == node_num[depth]:
            depth += 1
            count = 0
    return -1


def comp(a,b):
    count = 0
    for i in range(len(a)):
        if not a[i] == b[i]:
            count += 1
    return count


def solution(begin, target, words):
    answer = 0
    graph = {}
    li = []
    target_num = -1
    for i in range(len(words)):
        if target == words[i]:
            target_num = i
        if comp(begin, words[i]) == 1:
            li.append(i)
    graph[-1] = li
    for i in range(len(words)):
        li = []
        for j in range(len(words)):
            if i != j and comp(words[i], words[j]) == 1:
                li.append(j)
        graph[i] = li

    if target_num == -1:
        return 0
    else:
        v = dfs(graph, -1, target_num, 0)
        if v == -1:
            return 0
        else:
            return v


begin = 'hit'
target = 'cog'
words = ['hot', 'dot', 'dog', 'lot', 'log', 'cog']
print(solution(begin, target, words))
