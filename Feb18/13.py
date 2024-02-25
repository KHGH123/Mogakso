n = int(input())
a=[]
m=[[0] * (i+1) for i in range(n)]
for i in range(n):
    a.append([*map(int, input().split())])
m[0] = a[0]

for i in range(1, n):
    m[i][0] = m[i-1][0] + a[i][0]
    m[i][-1] = m[i-1][-1] + a[i][-1]
    for j in range(1, len(m[i])-1):
        m[i][j] = max(m[i-1][j-1], m[i-1][j]) + a[i][j]
print(max(m[-1]))