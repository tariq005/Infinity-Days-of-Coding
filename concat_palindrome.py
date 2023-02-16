for _ in range(int(input())):
    n, m= map(int, input().split())
    a= input()
    b= input()
    freq= [0]*26
    if n>m:
        a, b= b, a
        
    for c in b:
        freq[ord(c)-ord('a')] += 1
    for c in a:
        freq[ord(c)-ord('a')] -= 1
    count= 0
    
    for x in freq:
        if x<0:
            print('NO')
            break
        else:
            count += x%2
    else:
        if count == sum(freq)%2:
            print('YES')
        else:
            print('NO')
