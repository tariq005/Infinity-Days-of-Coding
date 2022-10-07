n= 10
psum= 0
i= 0
p= 0
j= 0

while j<n:
    p += 1
    psum += p
    i += 1
    while i == j+1:
        print(psum)
        i= 0
        j += 1
        psum= 0