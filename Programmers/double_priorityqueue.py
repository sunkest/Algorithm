import heapq

operations = ['I 16','D 1', 'D -1']

maxheap = [] # maxheap has opposite number
minheap = []
for op in operations:
    if op[0] == 'I':
        num = int(op.split(' ')[1])
        heapq.heappush(maxheap, -num)
        heapq.heappush(minheap, num)
    else:
        if not minheap:
            continue
        if op[2] == '1': # max pop
            p = heapq.heappop(maxheap)
            minheap.remove(-p)
        else: # min pop
            p = heapq.heappop(minheap)
            maxheap.remove(-p)

if minheap:
    answer = [-maxheap[0], minheap[0]]
else:
    answer = [0,0]
print(answer)