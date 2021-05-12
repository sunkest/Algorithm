from math import factorial


def get_kth_permutaion(arr, k):
    length = len(arr)
    if length == 1:
        return arr
    fact = factorial(length - 1)
    q = k // fact
    r = k % fact
    perm = [arr[q]]
    temp = arr[:]
    temp.pop(q)
    result = get_kth_permutaion(temp, r)
    perm.extend(result)
    return perm


def get_permutaion_index(perm, arr):
    length = len(arr)
    if length == 1:
        return 0
    fact = factorial(length - 1)
    answer = 0

    idx = arr.index(perm[0])
    answer += idx * fact
    temp = arr[:]
    temp.pop(idx)
    answer += get_permutaion_index(perm[1:], temp)

    return answer


n = int(input())
t, *args = map(int, input().split())

arr = [i for i in range(1, n + 1)]
if t == 1:
    [index] = args
    answer = get_kth_permutaion(arr, index - 1)
    print(*answer)
elif t == 2:
    answer = get_permutaion_index(args, arr)
    print(answer + 1)