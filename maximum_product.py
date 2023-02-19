def prod(a):
    product= 1
    for x in a:
        product *= x
    return product

for _ in range(int(input())):
    n= int(input())
    a= list(map(int, input().split()))
    a.sort()
    shot1= prod(a[-5:])
    shot2= prod(a[-3:]+a[:2])
    shot3= prod(a[-1:]+a[:4])
    print(max(shot3, shot2, shot1))