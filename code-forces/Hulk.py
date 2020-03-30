levels = int(input())
feelings = ''

for i in range(levels):
    if i > 0:
        feelings += ' that '

    feelings += 'I hate' if i % 2 == 0 else 'I love'

feelings += ' it'

print(feelings)
