import sys
from collections import defaultdict

input = sys.stdin.readline

n = int(input())
words = []
max_digit = defaultdict(lambda: 0)

for _ in range(n):
    word = input()
    words.append(word[:-1])
    for i, ch in enumerate(reversed(word[:-1])):
        max_digit[ch] += + 10 ** i

letters = list(max_digit.keys())
letters.sort(key=lambda x: max_digit[x], reverse=True)
numbers = defaultdict(lambda: -1)

for i, ch in enumerate(letters):
    numbers[ch] = 9 - i

total = 0
for word in words:
    temp = 0
    for i, ch in enumerate(reversed(word)):
        temp += 10 ** i * numbers[ch]
    total += temp

print(total)