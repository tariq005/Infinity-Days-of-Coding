for _ in range(int(input()):
    q = int(input())
    a = list(map(int, input.split()))
    last = a[0]
    s = '1'
    flag = False
    
    for i in range(1, q):
        if a[i] >= last:
            if flag == Flase or a[i] <= a[0]:
                s += '1'
                last = a[i]
            else:
                s += '0'
        elif flag == False and a[i] <= a[0]:
            s += '1'
            last = a[i]
            flag = True
        else:
            s += '0'
            
    print(s)
