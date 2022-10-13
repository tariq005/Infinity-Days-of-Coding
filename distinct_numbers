for _ in range(int(input())):
    n,k=map(int,input().split())
    d={}
    a=list(map(int,input().split()))
    m=0
    
    for i in a:
        d[i]=1
    m=max(a)
    
    a.sort()
    cnt=0
    temp=k
    x=1
    
    while(k!=0):
        if(x not in d):
            cnt+=m-x
            k-=1
        x+=1
        
    k=temp
    cnt1=0
    if(2*n not in d):
        m=2*n
        k-=1
    x=1
    
    while(k!=0):
        if(x not in d):
            cnt1+=m-x
            k-=1
        x+=1
        
    print(max(cnt, cnt1))
