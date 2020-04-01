participants, pens, notebooks = map(int, input().split())

print('Yes' if participants <= pens and participants <= notebooks else 'No')
