n = int(input())
str = input()
a = 0
d = 0
for i in range(len(str)):
	if(str[i]=='A'):
		a = a+1
	elif(str[i]=='D'):
		d= d+1
if(a<d):
	print('Danik')
elif(a==d):
	print('Friendship')
else:
	print('Anton')