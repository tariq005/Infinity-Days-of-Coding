s= input()
a= input()
b= input()
x= []

if (a in s) and (b in s[s.index(a)+len(a):]):
    x.append('forward')
s= s[::-1]
if (a in s) and (b in s[s.index(a)+len(a):]):
    x.append('backward')

if len(x) == 0:
    print('fantasy')
elif len(x) == 1:
    print(x[0])
else:
    print('both')