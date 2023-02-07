for _ in range(int(input())):
    n, x= map(int, input().split())
    a= list(map(int, input().split()))
    odd, even= 0, 0

    for z in a:
        if z%2:
            odd += 1
        else:
            even += 1

    i= 1
    while i <= odd:
        if even == 0 and x%2 == 0:
            print('No')
            break
        if x-i <= even:
            print('Yes')
            break
        i += 2
    else:
        print('No')