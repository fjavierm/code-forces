numbers = list(map(int, input().split()[:4]))

numbers.sort(reverse=True)

for i in range(1, 4):
    print(numbers[0] - numbers[i], end=' ')
