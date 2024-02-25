n = int(input())
a = [*map(int, input().split())]

m = [1 for _ in range(n)]

for i in range(n-1, -1, -1):
    for j in range(i+1, n):
        if a[i] < a[j]:
            m[i] = max(m[j]+1, m[i])
print(max(m))
