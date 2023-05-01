n, k, m= map(int, input().split())
index= {x: i for i, x in enumerate(input().split())}
a= list(map(int, input().split()))

for i in range(k):
    b= [int(x)-1 for x in input().split()[1:]]
    z= min(a[x] for x in b)
    for x in b:
        a[x]= z

print(sum(a[index[x]] for x in input().split()))
