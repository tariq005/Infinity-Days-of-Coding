import sys
input= sys.stdin.readline
for _ in range(int(input())):
    n= int(input())
    a= list(map(int, input().split()))
    pleasant= 0

    for i in range(1, n+1):
        for j in range(a[i-1]-i, n+1, a[i-1]):
            if i<j and a[i-1]*a[j-1] == i+j:
                pleasant += 1

    print(pleasant)