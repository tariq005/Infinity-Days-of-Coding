results= []

for _ in range(int(input())):
    n= int(input())
    s= input()

    a= s.count('1')
    b= n-a
    m= a*b

    c= s[0]
    d= 1
    for i in range(1, n):
        if c == s[i]:
            d += 1
        else:
            m= max(m, d*d)
            c= s[i]
            d= 1

    m= max(m, d*d)
    results.append(m)

print("\n".join(map(str, results)))