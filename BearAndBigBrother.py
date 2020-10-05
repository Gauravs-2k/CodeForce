a,b = input().split()
a = int(a)
b = int(b)
yr = 0
for i in range(1,10):
	a = a*3
	b = b*2
	yr = yr+1
	if(a>b):
		break;
print(yr)

