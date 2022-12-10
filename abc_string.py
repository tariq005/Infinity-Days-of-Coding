for _ in range(int(input())):
    a = input()
    n = len(a)
    m = n//2

    x = a.count('A')
    y = a.count('B')
    z = a.count('C')

    if x > m or y > m or z > m:
        print('NO')
    else:
        if x == m:
            if a[0] == 'A':
                a = a.replace('A', '(')
                a = a.replace('B', ')')
                a = a.replace('C', ')')
            else:
                a = a.replace('A', ')')
                a = a.replace('B', '(')
                a = a.replace('C', '(')
        elif y == m:
            if a[0] == 'B':
                a = a.replace('B', '(')
                a = a.replace('A', ')')
                a = a.replace('C', ')')
            else:
                a = a.replace('B', ')')
                a = a.replace('A', '(')
                a = a.replace('C', '(')
        else:
            if a[0] == 'C':
                a = a.replace('C', '(')
                a = a.replace('A', ')')
                a = a.replace('B', ')')
            else:
                a = a.replace('C', ')')
                a = a.replace('A', '(')
                a = a.replace('B', '(')

        stack = []
        for c in a:
            if len(stack) > 0:
                if stack[-1] == '(' and c == ')':
                    stack.pop()
                else:
                    stack.append(c)
            else:
                stack.append(c)

        if len(stack) == 0:
            print('YES')
        else:
            print('NO')
