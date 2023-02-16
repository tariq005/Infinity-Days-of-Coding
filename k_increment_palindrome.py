for _ in range(int(input())):
	n, k = map(int, input().split())
	a = list(map(int, input().split()))
	
	if n == k:
		print('Yes' if a == a[::-1] else 'No')
	elif n%2 == 1 or k%2 == 1:
		print('Yes')
	else:
	    print('Yes' if sum(a)%2 == 0 else 'No')
