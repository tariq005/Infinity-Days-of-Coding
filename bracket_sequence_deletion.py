for _ in range(int(input())):
    n= int(input())
    s= input()
    count=i=j=0

    while i<n-1:
        if (s[i] == '(' or (s[i] == ')' and s[i+1] == ')')):
            i += 2
        else:
            j= i+1
            while j<n and s[j] != ')':
                j += 1

            if j == n:
                break
            i= j+1
        count += 1

    print(count, n-i)