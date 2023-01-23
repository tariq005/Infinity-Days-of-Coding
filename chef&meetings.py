t= int(input())
a= str()
for _ in range(t):
    p= input()
    u= p[-2:]
    h= p[:2]
    m= p[3:5]
    if u == 'AM':
        if h == '12':
            meet= int(m)
        else:
            meet= int(h)*60 +int(m)
    else:
        if h == '12':
            meet= int(m)+ 12*60
        else:
            meet= int(h)*60 +int(m)+ 12*60
    n= int(input())
    for i in range(n):
        b= input()
        l= b[:8]
        r= b[9:]
        v1= l[-2:]
        v2= r[-2:]
        j1= l[:2]
        j2= r[:2]
        k1= l[3:5]
        k2= r[3:5]
        if v1 == 'AM':
            if j1 == '12':
                meet1= int(k1)
            else:
                meet1= int(j1)*60 +int(k1)
        else:
            if j1 == '12':
                meet1= int(k1) +12*60
            else:
                meet1= int(j1)*60 +int(k1)+ 12*60
        if v2 == 'AM':
            if j2 == '12':
                meet2= int(k2)
            else:
                meet2= int(j2)*60 +int(k2)
        else:
            if j2 == '12':
                meet2= int(k2)+ 12*60
            else:
                meet2= int(j2)*60 +int(k2)+ 12*60
        if meet1 <= meet and meet <= meet2:
            a += '1'
        else:
            a += '0'
            
    print(a)
    a= str()
