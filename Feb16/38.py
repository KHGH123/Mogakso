n=int(input())
a=1
for i in range(1, n+1):
    a*=i
b = list(str(a))
b.reverse()
for i in range(len(b)):
    if b[i]!="0":
        print(i)
        break