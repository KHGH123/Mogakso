v=set()
b=set()
a=[1,2,3]
b.add((*a, 4))
a=[2,3,4]
b.add((*a, 4))

print(b)
