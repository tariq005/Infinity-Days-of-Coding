n, q = map(int, input().split())
a = list(map(int, input().split()))

if n == 1:
    b = [1]
elif n == 2:
    b = [1, 2]
else:
    b = [1, 2]
    for i in range(2, n):
        if a[i-2] >= a[i-1] >= a[i]:
            b.append(b[-1])
        else:
            b.append(b[-1]+1)

for i in range(q):
    l, r = map(int, input().split())
    d = b[r - 1] - b[l - 1] + 1
    if d == 1 and r == l:
        print(d)
    else:
        if b[l] == b[l-1]:
            print(d+1)
        else:
            print(d)
