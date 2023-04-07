n, m= map(int, input().split())
p= n*n
row, col= {}, {}
a= []

for _ in range(m):
    x, y= map(int, input().split())
    row[x]= 1
    col[y]= 1
    r= (n-(len(row)))*(n-(len(col)))
    a.append(str(r))

print(' '.join(a))