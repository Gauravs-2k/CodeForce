str = input()
str = dict.fromkeys(str)
# cnt = 0
# for i in range(0,len(str)):
# 	for j in range(i+1,len(str)):
# 		if(str[i]==str[j]):
# 			cnt = cnt+1
# sum = len(str) - (cnt)
if(len(str)%2 == 0):
	print("CHAT WITH HER!")
else:
	print("IGNORE HIM!")
