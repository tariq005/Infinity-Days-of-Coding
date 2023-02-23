for _ in range(int(input())):
    n= int(input())
    
    if n == 0:
        print(4, 6, 1, 5)
    elif n == 1:
        print(1, 4, 3, 2)
    elif n == 2:
        print(2, 4, 3, 1)
    elif n == 3:
        print(1, 2, 7, 4)
    else:
        print(1, 2, 3, 3^n)
