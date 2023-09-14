for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    ans = [0]*n
    
    for i in range(1, n, 2):
        ans[i] = a.pop()
    for i in range(0, n, 2):
        ans[i] = a.pop()
        
    for j in range(1, n-1):
        if not ((ans[j-1] > ans[j] < ans[j+1]) or (ans[j-1] < ans[j] > ans[j+1])):
            print(-1)
            break
    else:
        print(*ans)
