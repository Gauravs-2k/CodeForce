x = input()
num = int(x)
cnt = 0
for i in range(len(x)):
	if(x[i]=='4'or x[i]=='7'):
		cnt = cnt + 1
if(cnt==4 or cnt==7):
	print("YES")
else:
	print("NO")