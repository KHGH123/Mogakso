a=0
b=0

for r in range(9):
    n = int(input())
    if a < n:
        a = n
        b = r+1
print(a)
print(b)