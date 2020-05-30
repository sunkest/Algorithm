
def solution(clothes):
    answer = 1
    d = {}
    for a in clothes:
        if d.get(a[1]) is None:         #dict.get(key)은 없는 key에 대해 None return
            d[a[1]] = 1                 #dict[key]는 없는 key에 대해 ERROR발생
        else:
            d[a[1]] = d[a[1]] + 1

    keylist = d.keys()
    for key in keylist:
        answer *= (d[key] + 1)

    # 하나도 안입는 경우 제외
    answer -= 1

    return answer