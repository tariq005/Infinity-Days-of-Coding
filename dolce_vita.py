for _ in range(int(input())):
    n, x= map(int, input().split())
    a= list(map(int, input().split()))
    a.sort()
    count, sum= 0, 0
    for j in range(n):
        sum += a[j]
        if sum>x:
            break
        p= x-sum
        r= p//(j+1)
        count += r+1
    print(count)