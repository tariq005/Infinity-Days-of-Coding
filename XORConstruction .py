n = int(input())
a = list(map(int, input().split()))
b = [0]*n
for i in range(1, n):
    b[i] = b[i-1] ^ a[i-1]

for i in range(20):
    one, zero = 0, 0
    for j in range(n):
        if (b[j] >> i) & 1:
            one += 1
        else:
            zero += 1

    if one > zero:
        for j in range(n):
            b[j] ^= (1 << i)
print(*b)
