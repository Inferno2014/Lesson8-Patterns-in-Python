s = "welcome"
for i in range(1, len(s) + 1):
    print(s[:i])
for i in range(1,6):
    for j in range(i):
        print('*', end='')
    print()
for i in range(1,9):
    for j in range(1,i):
        print(j, end='')
    print()
k = 0
for i in range(1,9):
    for j in range(1,i):
        k+=1
        print(k, end='')
    print()
for i in range(1,9):
    for j in range(1,14):
        print(i, end='')
    print()