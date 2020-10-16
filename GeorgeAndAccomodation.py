n = int(input())
cnt = 0
for i in range(n):
	pi, qi = input().split()
	pi = int(pi)
	qi = int(qi)
	available = qi - pi
	if(available>=2):
		cnt = cnt+1
print(cnt)