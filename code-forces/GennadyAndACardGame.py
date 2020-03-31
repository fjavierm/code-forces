hand = input()
table = input().split()[:5]
answer = 'NO'

for card in table:
    if hand[0] == card[0] or hand[1] == card[1]:
        answer = 'YES'
        break

print(answer)
