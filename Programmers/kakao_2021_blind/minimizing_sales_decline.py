# kakao_2021_blind #7 # 난이도 상
# Tree # DP
# DP일 것 같다는 발상 자체까지는 할 수 있지만
# DP가 이루어지는 아이디어는 상당히 까다로움

# dp[i][0]: i가 root인 subtree에서 i번이 참석하지 않는 최적해
# dp[i][1]: i가 root인 subtree에서 i번이 참석하는 최적해

# 점화식
# dp[i][1] = sales[i] + sum(i의 모든 child node k에 대한 min(dp[k][0], dp[k][1]))
# dp[i][0]는 min(i의 모든 child node k에 대한 (dp[k][1] - dp[k][0]))의 값이
# 양수인 경우 dp[i][0] = sum(i의 모든 child node k에 대한 min(dp[k][0], dp[k][1])값 ) + 윗줄식값(차의 최소값)
# 음수인 경우 dp[i][0] = sum(i의 모든 child node k에 대한 min(dp[k][0], dp[k][1])값 )
# leaf node 의 경우 dp[i][0] = 0, dp[i][1] = sales[i]
# 구하고자 하는 값은 root node인 1번노드에 대해 min(dp[1][0], dp[1][1])
INF = 1000000000


def get_dp(node, ptc, tree, dp, sales):
    if dp[node][ptc] != 0:
        return dp[node][ptc]

    if len(tree[node]) == 0:  # leaf node
        if ptc == 0:
            dp[node][0] = 0
            return dp[node][0]
        elif ptc == 1:
            dp[node][1] = sales[node]
            return dp[node][1]
    else:  # 팀장 node
        children = tree[node]
        child_sum = 0
        for child in children:
            child_sum += min(get_dp(child, 0, tree, dp, sales), get_dp(child, 1, tree, dp, sales))
        if ptc == 0:
            k = -1
            minimum = INF
            for child in children:
                sub = get_dp(child, 1, tree, dp, sales) - get_dp(child, 0, tree, dp, sales)
                if sub < minimum:
                    minimum = sub
                    k = child
            if minimum < 0:
                minimum = 0
            dp[node][0] = child_sum + minimum
            return dp[node][0]
        elif ptc == 1:
            dp[node][1] = sales[node] + child_sum
            return dp[node][1]


def solution(sales, links):
    n = len(sales)
    sales = [0] + sales
    tree = [[] for _ in range(n + 1)]
    for a, b in links:
        tree[a].append(b)

    dp = [[0, 0] for _ in range(n + 1)]
    answer = min(get_dp(1, 0, tree, dp, sales), get_dp(1, 1, tree, dp, sales))
    get_dp(1, 0, tree, dp, sales)
    get_dp(1, 1, tree, dp, sales)
    return answer


_sales = [10, 10, 1, 1]
_links = [[3, 2], [4, 3], [1, 4]]
print(solution(_sales, _links))
