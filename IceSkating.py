n= int(input())
x, y= [], []
drifts= 1
for _ in range(n):
    x1, y1= map(int, input().split())
    x.append({x1})
    y.append({y1})

for i in range(n-1):
    for j in range(i+1, n):
        if x[i]&x[j] or y[i]&y[j]:
            x[j] |= x[i]
            y[j] |= y[i]
            drifts += 1
            break
print(n-drifts)
