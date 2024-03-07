for _ in range(int(input())):
    n = int(input())
    a = input()
    b = input()
    s = a[0]
    count = 1
    track = 1
    i = 0

    while i < n-1:
        if track == 2:
            s += b[i+1]
            i += 1
            continue
        if a[i+1] < b[i]:
            s += a[i+1]
            i += 1
            count = 1
        elif a[i+1] > b[i]:
            s += b[i]
            track = 2
        elif a[i+1] == b[i]:
            s += a[i+1]
            count += 1
            i += 1

    if track == 1:
        s += b[i]
    print(s)
    print(count)
