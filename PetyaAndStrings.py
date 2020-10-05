# n = input()
# n = n.lower()
# s= 0
# for i in range(len(n)):
# 	s = s + ord(n[i]) 
# m = input()
# m = m.lower()
# t = 0
# for j in range(len(m)):
# 	t = t + ord(m[i])
# if(s>t):
# 	print(1)
# elif(s<t):
# 	print(-1)
# else:
# 	print(0)
m = input().lower()
n = input().lower()
if m == n:
    print(0)
elif m > n :
    print(1)
else:
    print(-1)