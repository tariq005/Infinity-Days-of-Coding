import sys
input= sys.stdin.readline
n= int(input())
maxx= 0

for x in input().split():
    x= int(x)+ maxx
    maxx= max(x, maxx)
    print(x)