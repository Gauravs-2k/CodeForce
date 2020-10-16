n = int(input())
lst = list(map(int,input().strip().split()))[:n]
sum = 0
for i in range(n):
	sum += (lst[i]/100)
val = sum/n
final = val * 100
print(final)