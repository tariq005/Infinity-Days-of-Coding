from math import *
for i in range(int(input())):
    k= int(input())

    sqrt1= int(sqrt(k))
    sqrt2= sqrt1+1

    if sqrt(k)-sqrt1 == 0:
        print(sqrt1, 1)
    else:
        dif= k- (sqrt1**2)

        if dif<sqrt2:
            print(dif, sqrt2)
        elif dif>sqrt2:
            print(sqrt2, (sqrt2**2)-k+1)
        else:
            print(sqrt2, sqrt2)