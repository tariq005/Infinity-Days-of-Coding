for i in range(int(input())):
    n= int(input())

    if n == 1 or n == 2:
        print(n)
    else:
        u= str()
        v= n//3
        w= n%3

        u += '21'*v
        if w == 1:
            u= '1'+u
        elif w == 2:
            u += '2'
        print(u)