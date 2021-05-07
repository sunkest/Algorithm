from itertools import permutations

OPERAND_TYPES = ['+', '-', '*']


def solution(expression):
    numbers = []
    operands = []
    num = ''
    for ch in expression:
        if ch.isdecimal():
            num += ch
        else:
            numbers.append(int(num))
            num = ''
            operands.append(ch)
    numbers.append(int(num))

    orders = list(permutations(OPERAND_TYPES, 3))
    results = []
    for order in orders:
        temp_numbers = numbers[:]
        temp_operands = operands[:]
        for op in order:
            i = 0
            while i < len(temp_operands):
                if temp_operands[i] == op:
                    if op == '+':
                        agg = temp_numbers[i] + temp_numbers[i + 1]
                    elif op == '-':
                        agg = temp_numbers[i] - temp_numbers[i + 1]
                    else:   # '*'
                        agg = temp_numbers[i] * temp_numbers[i + 1]
                    temp_numbers[i] = agg
                    temp_numbers.pop(i + 1)
                    temp_operands.pop(i)
                    continue
                i += 1
        results.append(temp_numbers[0])
    answer = max(results, key=lambda x: abs(x))
    return abs(answer)


print(solution("100-200*300-500+20"))
