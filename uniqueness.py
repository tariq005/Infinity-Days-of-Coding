n= int(input())
a= list(map(int, input().split()))
m= n

for i in range(n+1):
    s= set(a[:i])
    print(s)
    if len(s)<i:
        break
    for j in range(n-1, i-1, -1):
        if a[j] not in s:
            s.add(a[j])
            print(s)
        else:
            break
    m= min(m, j-i+1)
    print(m)

print(m)