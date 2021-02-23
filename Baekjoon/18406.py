# BOJ 18406 # Lucky Strike # Bronze 2
# Simulation
# 이것이 취업을 위한 코딩테스트다 - part 3 - 구현

n = input()
half = int(len(n) / 2)
left = n[:half]
right = n[half:]

sum_left = 0
sum_right = 0
for i in range(half):
    sum_left += int(left[i])
    sum_right += int(right[i])

if sum_left == sum_right:
    print("LUCKY")
else:
    print("READY")
