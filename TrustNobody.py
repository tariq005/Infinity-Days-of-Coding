for _ in range(int(input())):
    n= int(input())
    l= list(map(int, input().split()))

    for i in range(n+1):
        count= 0
        for x in l:
            if x>i:
                count += 1
        if i == count:
            print(count)
            break
    else:
        print(-1)