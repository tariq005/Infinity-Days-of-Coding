for _ in range(int(input())):
    n, c= map(str, input().split())
    n= int(n)
    s= input()

    if len(set(s)) == 1 and s[0] == c:
        print(0)
    else:
        i= n-1
        while i >= n//2:
            if s[i] == c:
                print(1)
                print(i+1)
                break
            i -= 1
        else:
            print(2)
            print(n, n-1)