import sys
input = sys.stdin.readline

for _ in range(int(input())):
    a, b, c, k = map(int, input().split())

    for x in range(10**(a-1), 10**a):
        min_b = max(10**(b-1), 10**(c-1)-x)
        max_b = min(10**b-1, 10**c-1-x)
        options = max(0, max_b-min_b+1)

        if options >= k:
            print(x, ' + ', min_b+k-1, ' = ', x+min_b+k-1)
            break
        else:
            k -= options
    else:
        print(-1)
