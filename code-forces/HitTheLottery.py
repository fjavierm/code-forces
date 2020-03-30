amount = int(input())
bills = 0

notes = [100, 20, 10, 5, 1]

while amount > 0:
    if amount >= notes[0]:
        bills += amount // notes[0]
        amount %= notes[0]

    notes.pop(0)

print(bills)
