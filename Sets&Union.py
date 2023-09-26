for _ in range(int(input())):
    n = int(input())
    b = []
    union = set()
    for i in range(n):
        s = list(map(int, input().split()))
        b.append(s[1:])
        union.update(set(s[1:]))

    m = 0
    for x in union:
        a = set()
        for j in b:
            if x not in j:
                for z in j:
                    a.add(z)
        if len(a) > m:
            m = len(a)
    print(m)
