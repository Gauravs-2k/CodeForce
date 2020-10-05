n = int(input())
for i in range(n):
	s = input()
	l = len(s)
	if(l>10):
		first = s[0]
		last = s[l-1]
		print(first+str(l-2)+last)
	else:
		print(s)