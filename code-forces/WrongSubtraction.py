number, times = map(int, input().split())

for i in range(times):
    number = number // 10 if number % 10 == 0 else number - 1

print(number)
