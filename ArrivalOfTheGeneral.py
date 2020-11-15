n = int(input())
a = list(map(int,input().strip().split()))[:n]
max = 0
min = 1000
max_ind = 0
min_ind = 0
for i in range(n):
	x = a[i]
	if(x > max):
		max_ind = i
		max = x
	if(x<=min):
		min_ind = i
		min = x
if(max_ind>min_ind):
	cnt = (max_ind-1)+(n-min_ind)-1
else:
	cnt = (max_ind-1) + (n-min_ind)
print(cnt)