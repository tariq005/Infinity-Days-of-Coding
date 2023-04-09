for _ in range(int(input())):
    k= int(input())
    s= str()

    while k>0:
        s += str(k%9)
        k //= 9
    s= s[::-1]

    t= str()
    for x in s:
        if x>'3':
            t += str(int(x)+1)
        else:
            t += x
    print(t)
    