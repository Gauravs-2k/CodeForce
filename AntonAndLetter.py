a = input()
st = set()
for i in a:
	if(i>="a" and i <= "z"):
		st.add(i)

print(len(st))