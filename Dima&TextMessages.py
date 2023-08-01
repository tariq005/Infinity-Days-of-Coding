n = int(input())
t = '<3'
for i in range(n):
    t += input() + '<3'

p = input()
s = "yes"
j = 0

for c in t:
    j = p.find(c, j)+1
    if j == 0:
        s = 'no'
        break

print(s)
