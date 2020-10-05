n = int(input())
cnt = 0
for i in range(n):
	a,b,c = input().split()
	if(int(a)+int(b)+int(c) >=2):
		cnt = cnt+1

print(cnt)