for _ in range(int(input())):
    x= int(input())
    
    if x == 1:
        print(1, 5, 9)
    else:
        if x%2 == 0:
            print(x, x+1, x+2)
        else:
            print(1, x-1, x)
