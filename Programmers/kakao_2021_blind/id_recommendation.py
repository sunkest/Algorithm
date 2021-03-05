# kakao_2020_blind 1번
# 단순 구현 - 정규식 사용시 구현은 편리
# 한단계씩 문자열 수정해도 정답, 앞에서부터 보면서 answer에 붙여나가면 좀더 빠름


def solution(new_id):
    valid_symbols = '-_.'
    answer = ''
    new_id = new_id.lower()

    for char in new_id:
        if char.islower() or char.isnumeric():  # 1
            answer += char
        elif char.isupper():  # 2
            answer += char.lower()
        elif char in valid_symbols:  # 2
            if char == '.':
                if len(answer) == 0:  # 4-1
                    continue
                if answer[-1] == '.':  # 3
                    continue
            answer += char

    if len(answer) > 0 and answer[-1] == '.':  # 4-2
        answer = answer[:-1]

    if len(answer) == 0:  # 5
        answer = 'a'

    if len(answer) > 15:  # 6-1
        answer = answer[:15]

    if answer[-1] == '.':  # 6-2
        answer = answer[:-1]

    if len(answer) == 2:
        answer += answer[-1]
    elif len(answer) == 1:
        answer += answer[-1] * 2

    return answer


id_ = "abcdefghijklmn.p"
print(solution(id_))
