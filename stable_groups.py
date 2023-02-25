n, k, x= map(int, input().split())
a= list(map(int, input().split()))
a.sort()
count= 1
d= []

for i in range(1, n):
    if a[i]-a[i-1] > x:
        d.append((a[i]-a[i-1]-1)//x)
        count += 1

d.sort()
m= len(d)
i= 0
while i<m:
    if k >= d[i]:
        k -= d[i]
        count -= 1
        i += 1
    else:
        break
print(count)