answer = 0

def dfs(r, n, depth, length, target, numbers):
    global answer
    if depth == length - 1:
        if r + n == target:
            answer += 1
        return
    else:
        depth += 1
        dfs(r + n, numbers[depth], depth, length, target, numbers)
        dfs(r + n, -numbers[depth], depth, length, target, numbers)


def solution(numbers, target):
    global answer
    dfs(0, numbers[0], 0, len(numbers), target, numbers)
    dfs(0, -numbers[0], 0, len(numbers), target, numbers)

    return answer


numbers = [1,1,1,1,1]
target = 3
print(solution(numbers, target))