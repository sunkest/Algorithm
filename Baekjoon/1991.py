import sys
from collections import defaultdict

input = sys.stdin.readline

n = int(input())
tree = defaultdict(lambda: [])
for _ in range(n):
    node, *children = input().split()
    for child_node in children:
        tree[node].append(child_node)

pre_order = ""
in_order = ""
post_order = ""


def dfs(node: str):
    global pre_order, in_order, post_order
    left_node, right_node = tree[node]
    pre_order += node
    if left_node != '.':
        dfs(left_node)
    in_order += node
    if right_node != '.':
        dfs(right_node)
    post_order += node


dfs('A')
print(pre_order)
print(in_order)
print(post_order)
