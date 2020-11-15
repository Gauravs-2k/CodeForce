a = list(map(int,input().split()))
cnt = 0
for i in range(len(a)):
	for j in range(i+1,len(a)):
		#print(a[i])
		if(a[i]==a[j]):
			#print(a[i])
			cnt += 1
if(cnt==6):
	print(3)
elif(cnt == 3):
	print(2)
else:
	print(cnt)

