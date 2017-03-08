i = 1
while i <= 100:
    print(i, ' ', end='')
    i = i + 1
print()
i = 1
while i <= 100:
    if i % 3 == 0:
        if i % 5 == 0:
            print('BazQux', ' ', end='')
        else:
            print('Baz', ' ', end='')
    elif i % 5 == 0:
        print('Qux', ' ', end='')
    else:
        print(i, ' ', end='')
    i = i + 1
