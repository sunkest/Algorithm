from queue import PriorityQueue
import heapq
stock = 5
dates = [3,5,6,8,9]
supplies = [1,2,4,2,1]
k = 13
answer = 0

heap = []
for i in range(len(dates)):
    if dates[i] > stock:
        stock += heapq.heappop(heap)[1]
        answer += 1
        heapq.heappush(heap, (-supplies[i], supplies[i]))
        continue
    if dates[i] > stock:
        stock += heapq.heappop(heap)[1]
        answer += 1
    heapq.heappush(heap, (-supplies[i], supplies[i]))

for h in heap:
    if stock >= k+1:
        break
    stock += h[1]
    answer += 1



print(answer)