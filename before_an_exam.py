d, sumTime= map(int, input().split())
a, rem= [], []

for _ in range(d):
    minTime, maxTime= map(int, input().split())
    a.append(minTime)
    rem.append(maxTime-minTime)

p= sum(a)
if p == sumTime:
    print('YES')
    print(*a)
elif p>sumTime:
    print('NO')
else:
    i= 0
    while i<d:
        r= min(rem[i], sumTime-p)
        a[i] += r
        p += r
        if p == sumTime:
            print('YES')
            print(*a)
            break
        i += 1
    else:
        print('NO')