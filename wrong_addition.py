for _ in range(int(input())):
    a, s= map(str, input().split())
    n, m= len(s), len(a)
    b= ['0']*m
    j= n-1

    for i in range(m-1, -1, -1):
        if j<0:
            print(-1)
            break
        if s[j] < a[i]:
            if j-1 >= 0:
                p= s[j-1]+s[j]
                q= a[i]
                r= int(p)-int(q)
                if r<0 or r>9:
                    print(-1)
                    break
                else:
                    b[i]= str(r)
                j -= 2
            else:
                print(-1)
                break

        else:
            r= int(s[j])-int(a[i])
            if r<0 or r>9:
                print(-1)
                break
            else:
                b[i]= str(r)
            j -= 1
    else:
        d= str()
        if j >= 0:
            d= s[:j+1]
        c= ''.join(b)
        f= d+c
        print(int(f))