def schedule(j, x):
    if x == -1:
        return 'r' if a[j] == 0 else 'c' if a[j] == 1 else 'g' if a[j] == 2 else \
            'c' if j < n-1 and schedule(j+1, x) != 'c' else 'g'
    if a[j] == 0:
        return 'r'
    elif a[j] == 1 and x != 'c':
        return 'c'
    elif a[j] == 2 and x != 'g':
        return 'g'
    elif a[j] == 3:
        if x == 'g':
            return 'c'
        elif x == 'c':
            return 'g'
    else:
        return 'r'


n = int(input())
a = list(map(int, input().split()))
count = 0
k = -1
for i in range(n):
    d = schedule(i, k)
    k = d
    if k == 'r':
        count += 1

print(count)
