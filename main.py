n= int(input())
a= []

for x in range(max(1, n-99), n+1):
    print(x)
    if x+ sum(map(int, str(x))) == n:
        a.append(x)

print(len(a))
print(*a)
