for _ in range(int(input())):
    n, k= map(int, input().split())
    s= input()
    dic= [0]*26
    for i in range(n):
        dic[ord(s[i])- 97] += 1

    books= str()
    p= n//k
    for i in range(k):
        j= 0
        while j<p and j<25 and dic[j] != 0:
            dic[j] -= 1
            j += 1
        books += chr(j+97)

    print(books)
