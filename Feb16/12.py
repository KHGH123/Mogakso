a,b,c = int(input()), int(input()), int(input())
a = str(a*b*c)
for r in range(10):
    print(a.count(str(r)))