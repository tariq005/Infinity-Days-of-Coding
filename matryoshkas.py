from collections import defaultdict
for _ in range(int(input())):
    n= int(input())
    a= list(map(int, input().split()))
    a.sort()
    check= defaultdict(lambda: 0)
    for num in a:
        check[num] += 1

    dic= []
    for num in check:
        dic.append((num, check[num]))
    res = dic[0][1]
    for i in range(1, len(dic)):
        if dic[i][0] == dic[i - 1][0] + 1:
            res += max(0, dic[i][1] - dic[i - 1][1])
        else:
            res += dic[i][1]
    print(res)