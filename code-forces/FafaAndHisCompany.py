employees = int(input())

combinations = 0
for i in range(1, (employees // 2) + 1):
    if employees % i == 0:
        combinations += 1

print(combinations)
