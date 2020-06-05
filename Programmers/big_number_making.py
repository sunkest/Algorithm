
def solution(number, k):
    answer = ''
    # 앞에서부터 하나씩 넣으면서 꽉찼을 때에는 앞에서부터 가장 먼저 증가한곳 뺌
    temp = []
    for i, num in enumerate(number):
        while temp and temp[-1] < num and k > 0:
            temp.pop()
            k -= 1
        if k == 0:
            temp += number[i:]
            break
        temp.append(num)
    temp = temp[:-k] if k > 0 else temp
    answer = ''.join(temp)
    return answer


print(solution('1231234', 3))
