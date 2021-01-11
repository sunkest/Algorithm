def solution(p):
    if len(p) == 0:
        return ''
    if check_proper(p):
        return p
    u, v = get_balanced_uv(p)
    if check_proper(u):
        return u + solution(v)
    else:
        new_u = u[1:-1]
        new_u = flip(new_u)
        return '(' + solution(v) + ')' + new_u


def flip(p):
    new_str = ''
    for ch in p:
        if ch == '(':
            new_str += ')'
        elif ch == ')':
            new_str += '('
    return new_str


def check_proper(p):
    count = 0
    for ch in p:
        if ch == '(':
            count += 1
        elif ch == ')':
            count -= 1
        if count < 0:
            return False
    if count == 0:
        return True
    else:
        return False


def get_balanced_uv(p):
    count = 0
    for i, ch in enumerate(p):
        if ch == '(':
            count += 1
        elif ch == ')':
            count -= 1
        if count == 0:
            return p[0:i+1], p[i+1:]


input_str = "()))((()"
print(solution(input_str))
