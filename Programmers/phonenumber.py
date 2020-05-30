a = ['12', '567', '88', '5']


def solution(phone_book):
    phone_book = sorted(phone_book, key=lambda n: len(n))
    answer = True
    d = {}

    for num in phone_book:
        for i in range(len(num)):
            print(num[:i+1])
            if d.get(num[:i+1]) is not None:
                return False
        d[num] = 1
        print(d)

    return answer


print(solution(a))