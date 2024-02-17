n=list(map(int, input().split()))
total=0
for r in n:
    total+=int(r)*int(r)

print(total%10)