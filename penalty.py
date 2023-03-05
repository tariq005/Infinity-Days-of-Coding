for _ in range(int(input())):
    s= input()
    a=b=0
    ans1=ans2=10

    for i in range(10):
        baki = (10 - i) // 2
        if a + baki < b:
            ans1 = i
            break
        if i%2:
            if s[i] == '1' or s[i] == '?':
                b += 1
        else:
            if s[i] == '1':
                a += 1

    a=b=0
    for i in range(10):
        baki = (10 - i + 1) // 2
        if b + baki < a:
            ans2 = i
            break
        if i%2:
            if s[i] == '1':
                b += 1
        else:
            if s[i] == '1' or s[i] == '?':
                a += 1

    print(min(ans1, ans2))