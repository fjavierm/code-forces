numberOfPeople = int(input())
valuations = list(map(int, input().split()[:numberOfPeople]))

print('HARD' if any(valuations) else 'EASY')
