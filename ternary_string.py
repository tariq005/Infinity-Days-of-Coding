for _ in range(int(input())):
	s= input()
	n= len(s)
	con= n

	if len(set(s))<3:
		print(0)
	else:
		i= 0
		j= 0
		while i+1<n:
			if s[i] != s[i+1]:
				j= i+1
				while j+1<n:
					if s[j] != s[j+1]:
						j += 1
						break
					else:
						j += 1
				if len(set(s[i:j+1])) == 3:
					con= min(con, j-i+1)
				i += 1
				j= i
			else:
				i += 1

		print(con)