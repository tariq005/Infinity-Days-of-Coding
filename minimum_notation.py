for _ in range(int(input())):
    s= input()
    m= s[-1]
    final= []
    s= reversed(s)
    for x in s:
        if x>m:
            final.append(str(min(9, int(x)+1)))
        else:
            final.append(x)
            m= x
    print(''.join(sorted(final)))