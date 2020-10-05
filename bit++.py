n = int(input())
val = 0
for i in range(n):
	str = input()
	if(str[1] == '+'):
		val+=1
	else:
		val-=1
print(val)