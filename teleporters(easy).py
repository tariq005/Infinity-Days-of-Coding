for _ in range(int(input())):
    n, c= map(int, input().split())
    a= list(map(int, input().split()))
    count= 0

    for i in range(n):
        a[i] += i+1
    a.sort()

    for x in a:
        if x <= c:
            c -= x
            count += 1
        else:
            break

    print(count)