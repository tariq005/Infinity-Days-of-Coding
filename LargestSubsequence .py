for _ in range(int(input())):
    n = int(input())
    s = input()

    if s == ''.join(sorted(s)):
        print(0)
    else:
        stack = []
        for x in s:
            while stack and x > stack[-1]:
                stack.pop()
            stack.append(x)

        t = ''.join(stack)
        m = len(t)
        a = str()
        j = 0
        for i in range(n):
            if s[i] == t[j]:
                a += t[m-j-1]
                j += 1
            else:
                a += s[i]

        co = 0
        for j in range(1, m):
            if len(set(t[:j+1])) == 1:
                co += 1
            else:
                break
        if a == ''.join(sorted(s)):
            print(m-co-1)
        else:
            print(-1)
