def solution(s):
    length = len(s)
    min_length = length
    for i in range(1, int(length+1 / 2)):
        temp = s
        unit = temp[0:i]
        count = 1
        compressed_str = ""
        while len(temp) > 0:
            temp = temp[i:]
            new_unit = temp[0:i]
            if unit == new_unit:
                count += 1
                continue
            else:
                if count > 1:
                    compressed_str = compressed_str + str(count) + unit
                else:
                    compressed_str += unit
                unit = new_unit
                count = 1
        if min_length > len(compressed_str):
            min_length = len(compressed_str)

    return min_length


input_str = 'ababcdcdababcdcd'
print(solution(input_str))
