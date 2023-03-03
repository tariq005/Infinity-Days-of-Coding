for _ in range(int(input())):
    n= int(input())
    s= input()
    ss= s[2:]
    count= 1
    i, j= 0, 0

    while i<n-2:
        if s[i] != ss[j]:
            count += 1
        i += 1
        j += 1
    print(count)