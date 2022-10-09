for i in range(int(input())):
    a1, a2, a3= map(int, input().split())
    p= a1+a3- (2*a2)

    if p%3 == 0:
        print(0)
    else:
        print(1)