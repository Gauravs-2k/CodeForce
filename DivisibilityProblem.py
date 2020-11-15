t = int(input())
for i in range(t):
    def find(a, b):
        x = a%b
        ans = b-x
        print(ans)
    a, b = [int(j) for j in input().split()]
    if (a % b == 0):
        print(0)
    elif(b>a):
        print(b-a)
    else:
        find(a,b)