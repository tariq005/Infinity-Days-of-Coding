for _ in range(int(input())):
    s= input()
    n= len(s)

    if len(set(s)) == 1:
        print(0)
        print('\n')
    elif len(set(s)) == 2 or len(set(s)) == 3:
        if 'L' in s and 'R' in s:
            print(2)
            print('LR')
        elif 'U' in s and 'D' in s:
            print(2)
            print('UD')
        else:
            print(0)
            print('\n')
    else:
        lcount = s.count('L')
        ucount = s.count('U')
        dcount = s.count('D')
        rcount = s.count('R')
        rl= min(lcount, rcount)
        ud= min(ucount, dcount)
        print(2*rl + 2*ud)
        c= rl*'R'+ud*'U'+rl*'L'+ud*'D'
        print(c)