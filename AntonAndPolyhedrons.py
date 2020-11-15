n = int(input())
face = 0
for i in range(n):
	a = input()
	if(a=="Tetrahedron"):
		face += 4
	elif(a=="Cube"):
		face += 6
	elif(a=="Octahedron"):
		face += 8
	elif(a == "Dodecahedron"):
		face += 12
	elif(a == "Icosahedron"):
		face += 20
print(face)	