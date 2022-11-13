import sys
input= sys.stdin.readline
for _ in range(int(input())):
    n= int(input())
    s= input()
    ans= 0
    for i in range(n):
        distinct= 0
        freq= [0]*10
        for j in range(i, min(i+100, n)):
            if freq[int(s[j])] == 0:
                distinct += 1
            freq[int(s[j])] += 1
            if distinct >= max(freq):
                ans += 1
    print(ans)