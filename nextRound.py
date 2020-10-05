n, k = input().split()
cnt = 0

lst = list(map(int,input().strip().split()))[:int(n)] 
temp = lst[int(k)-1]
for i in range(int(n)):
	if(lst[i]>=temp and lst[i]>0):
		cnt = cnt+1
print(cnt)