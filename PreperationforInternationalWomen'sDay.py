n, k= map(int, input().split())
d= list(map(int, input().split()))

boxes= [0]*k
for x in d:
    boxes[x%k] += 1
gifts= 0

gifts += boxes[0]//2
if k%2 == 0:
    gifts += boxes[k//2]//2
    for i in range(1, k//2):
        gifts += min(boxes[i], boxes[k-i])

else:
    for i in range(1, (k//2)+1):
        gifts += min(boxes[i], boxes[k-i])
print(gifts*2)