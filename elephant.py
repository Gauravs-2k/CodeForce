x = int(input())
if(x>=5):
	cnt = x
else:
	cnt = 1
while(x>=5):
	cnt = cnt//5
	x = x%5
	if(x==0):
		break;
	else:
		cnt = cnt+1
print(cnt)