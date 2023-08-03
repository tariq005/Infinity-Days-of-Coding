for _ in range(int(input())):
    n, m = map(int, input().split())
    s = input()
    leftmost_0 = [0]*n
    rightmost_1 = [0]*n

    leftmost_0[0] = -1
    for i in range(n):
        if i > 0:
            leftmost_0[i] = leftmost_0[i-1]
        if s[i] == '0':
            leftmost_0[i] = i

    rightmost_1[n-1] = n
    for i in range(n-1, -1, -1):
        if i+1 < n:
            rightmost_1[i] = rightmost_1[i+1]
        if s[i] == '1':
            rightmost_1[i] = i

    a = set()
    for i in range(m):
        l, r = map(int, input().split())
        nearest_leftmost_1 = rightmost_1[l-1]
        nearest_rightmost_0 = leftmost_0[r-1]

        if nearest_rightmost_0 < nearest_leftmost_1:
            a.add((-1, -1))
        else:
            a.add((nearest_leftmost_1, nearest_rightmost_0))
    print(len(a))
