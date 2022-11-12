s= set()
d= {}
s.add(0)
for _ in range(int(input())):
    sign, x= map(str, input().split())
    x= int(x)

    if sign == '+':
        s.add(x)
    else:
        if x not in d:
            d[x]= x
        while d[x] in s:
            d[x] += x
        print(d[x])