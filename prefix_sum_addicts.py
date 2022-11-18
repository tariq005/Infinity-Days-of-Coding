for _ in range(int(input())):
    n, k= map(int, input().split())
    s= list(map(int, input().split()))

    if k == 1:
        print('Yes')
    elif s[1]- s[0] < s[0]/(n-k+1):
        print('No')
    else:
        for i in range(1, k-1):
            if s[i]- s[i-1]> s[i+1]- s[i]:
                print('No')
                break
        else:
            print('Yes')