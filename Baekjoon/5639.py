import sys
sys.setrecursionlimit(100000)
input = sys.stdin.readline

pre_order = []
while True:
    try:
        num = int(input())
    except:
        break
    pre_order.append(num)


def post_order(tree):
    if not tree:
        return
    root = tree[0]
    if len(tree) > 1:
        idx = 0
        for i in range(1, len(tree)):
            num = tree[i]
            if num > root:
                idx = i
                break
        if idx == 0:
            left = tree[1:]
            right = []
        else:
            left = tree[1:idx]
            right = tree[idx:]
        post_order(left)
        post_order(right)

    print(root)


post_order(pre_order)
