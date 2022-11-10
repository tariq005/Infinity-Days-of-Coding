n= int(input())
prime= [1]*(n+1)
prime[0]= 0
prime[1]= 0

i= 2
while i*i <= n:
    if prime[i]:
        j= i*i
        while j <= n:
            prime[j]= 0
            j += i
    i += 1

for k in range(n+1):
    if prime[k] == 1:
        print(k)