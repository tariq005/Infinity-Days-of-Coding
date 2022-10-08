for i in range(int(input())):
    n, s, r= int(input()), input(), 0
    for j in range(n):
        if (j+2<n and s[j] == '0' and s[j+1] == '1' and s[j+2] == '0'): r+= 1
        if (j+1<n and s[j] == '0' and s[j+1] == '0'): r+= 2
    print(r)