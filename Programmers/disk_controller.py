from queue import PriorityQueue
jobs = [[0, 3], [1, 9], [2, 6]]


jobs = sorted(jobs, key=lambda a: 10000*a[0]+a[1])
# jobs is sorted by inc order of request([0]) and then duration([1])

pq = PriorityQueue()
time = jobs[0][0]
answer = 0
i = 0
# !!!!!!!!!!!!!!!!!!!pq contains [duration, request time]
while i < len(jobs):
    if jobs[i][0] <= time:   # 실행하지 못하고 지나간 task OR 앞의 task 종료와 동시에 요청된 task
        pq.put((jobs[i][1], jobs[i][0]))
        i += 1
    else:
        if not pq.empty():
            (dur, rq) = pq.get()
            time += dur
            answer += time - rq
        else:
            time = jobs[i][0] + jobs[i][1]
            answer += jobs[i][1]
            i += 1

while not pq.empty():
    (dur, rq) = pq.get()
    time += dur
    answer += time - rq

answer = int(answer / len(jobs))
print(answer)
