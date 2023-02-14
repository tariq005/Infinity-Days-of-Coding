for _ in range(int(input())):
    n= int(input())
    a= sorted(list(map(int, input().split())), reverse= True)
    alice= 0
    bob= 0

    for i in range(n):
        if i%2:
            if a[i]%2:
                bob += a[i]
        else:
            if a[i]%2 == 0:
                alice += a[i]

    if alice == bob:
        print('Tie')
    elif alice>bob:
        print('Alice')
    else:
        print('Bob')