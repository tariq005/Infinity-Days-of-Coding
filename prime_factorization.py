n= int(input())
i= 2
while i*i <= n:
    count= 0
    while n%i == 0:
        count += 1
        n /= i
    if count>0:
        print(i, '**', count)
    i += 1
if n>1:
    print(int(n), '**', 1)