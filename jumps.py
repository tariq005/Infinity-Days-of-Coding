sum_n= [0]*1415
for i in range(1, 1415):
    sum_n[i]= (i*(i+1))//2

for _ in range(int(input())):
    x= int(input())
    if x in sum_n:
        print(sum_n.index(x))
    else:
        i= 0
        while sum_n[i]<x:
            i += 1
        p= sum_n[i]
        if x+1 == p:
            print(i+1)
        else:
            print(i)