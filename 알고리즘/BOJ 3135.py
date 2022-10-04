a,b = map(int,input().split())
x = []
n = int(input())
for i in range(n):
    q = int(input())
    x.append(abs(q-b))
print(min(x)+1)