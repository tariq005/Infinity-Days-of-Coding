for _ in range(int(input())):
    n= int(input())
    a, b, c= map(int, input().split())
    s= input()
    alice= ['0']*n
    count= 0

    for i in range(n):
        if s[i] == 'S' and a>0:
            a -= 1
            count += 1
            alice[i]= 'R'
        elif s[i] == 'R' and b>0:
            b -= 1
            count += 1
            alice[i]= 'P'
        elif s[i] == 'P' and c>0:
            c -= 1
            count += 1
            alice[i]= 'S'

    for j in range(n):
        if alice[j] == '0':
            if a>0:
                alice[j]= 'R'
                a -= 1
            elif b>0:
                alice[j]= 'P'
                b -= 1
            else:
                alice[j]= 'S'
                c -= 1

    alice= ''.join(alice)
    if count >= (n+1)//2:
        print('YES')
        print(alice)
    else:
        print('NO')