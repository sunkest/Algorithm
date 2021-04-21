import sys

input = sys.stdin.readline

n = int(input())
a = map(int, input().split())
check = set(a)

m = int(input())
b = map(int, input().split())
for num in b:
    if num in check:
        print(1)
    else:
        print(0)
