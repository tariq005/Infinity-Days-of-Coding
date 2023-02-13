n= int(input())
s= input()
count= 0

for i in range(n):
    for j in range(i+1, n+1):
        u= s[i:j]
        count += u.count('U') == u.count('D') and u.count('R') == u.count('L')

print(count)