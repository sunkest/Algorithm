import sys
from collections import defaultdict

input = sys.stdin.readline

count = 0
trees = defaultdict(lambda: 0)
while True:
    tree = input().rstrip()
    if not tree:
        break
    trees[tree] += 1
    count += 1

tree_names = sorted(trees.keys())
for tree in tree_names:
    print(tree, "{:.4f}".format(trees[tree] * 100 / count))
