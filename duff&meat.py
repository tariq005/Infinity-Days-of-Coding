n= int(input())
meat= 0
duff= 100

for _ in range(n):
    a, p= map(int, input().split())
    duff= min(duff, p)
    meat += duff*a

print(meat)