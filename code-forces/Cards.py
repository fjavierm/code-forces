from collections import Counter

length = int(input())
word = input()

counts = Counter(word)
ones = counts.get('n') if counts.get('n') is not None else 0
zeros = counts.get('z') if counts.get('z') is not None else 0

for _ in range(0, ones):
    print('1 ', end='')

for _ in range(0, zeros):
    print('0 ', end='')

print()
