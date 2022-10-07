for i in range(int(input())):
    w, s = map(str, input().split())
    d = int(w) - 28
    dic = {'mon': 0, 'tues': 1, 'wed': 2, 'thurs': 3, 'fri': 4, 'sat': 5, 'sun': 6}
    res = [4,4,4,4,4,4,4]
    
    for i in range(d):
        res[(dic[s] + i) % 7] += 1

    print(*res)
