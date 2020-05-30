answer = []
progresses = [93, 30, 55]
speeds = [1, 30, 5]

stack = []   #python list = stack

for i in range(len(progresses)):
    q = (100-progresses[i]) // speeds[i]
    if not (100-progresses[i]) % speeds[i] == 0:
        q += 1

    if len(stack) == 0 or q <= stack[0]:
        stack.append(q)
    else:
        answer.append(len(stack))
        stack.clear()
        stack.append(q)

answer.append(len(stack))
print(answer)