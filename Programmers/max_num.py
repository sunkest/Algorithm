
numbers = [1,10,101,102,100,1000,0]


def comp(x):
    c = 0
    while len(x) < 4:
        x += x[c]
        c += 1
    print(x)
    return x


strings = []
for n in numbers:
    strings.append(str(n))

strings.sort(key=comp, reverse=True)
print(strings)
answer = ''.join(strings)
if answer[0] == '0':
    print('0')
print(answer)