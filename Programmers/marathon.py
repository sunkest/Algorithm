
participant = ['mislav', 'stanko', 'mislav', 'ana']
completion = ['stanko', 'ana', 'mislav']

answer = ''

hash = {}

for c in completion:
    if hash.get(c) == None:
        hash[c] = 1
    else:
        hash[c] = hash[c] + 1

for p in participant:
    if hash.get(p) == None or hash.get(p) == 0:
        answer = p
    else:
        hash[p] = hash[p] - 1

print(answer)