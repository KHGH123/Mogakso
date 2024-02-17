s = set()

for i in range(10001):
    a=i
    for r in list(map(int, str(i))):
        a+=r
    if a <= 10000:
        s.add(a)

s=list(s)
answer = [i for i in range(10001) if i not in s]
for a in answer:
    print(a)
