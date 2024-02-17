n=int(input())
for r in range(n):
    a, b = input().split()
    c = set(b)
    for k in c:
        b = b.replace(k, k*int(a))
    print(b)