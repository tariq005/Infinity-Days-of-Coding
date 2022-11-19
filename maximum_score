for _ in range(int(input())):
    n=int(input())
    score= []
    for i in range(n):
        a= list(map(int, input().split()))
        a.sort()
        score.append(a)
    score= score[::-1]
    maxx= max(score[0])
    p= max(score[0])
    for j in range(1, len(score)):
        b= score[j]
        b= sorted(b, reverse= True)
        for value in b:
            if value<p:
                maxx += value
                p= value
                break
        else:
            maxx= -1
            break
    print(maxx)
