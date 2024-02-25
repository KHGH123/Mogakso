a, b, c = map(int, input().split())

def func(a, b, c):
    if b == 1:
        return a
    x = func(a, b//2, c)
    if b%2 == 0:
        return (x * x) % c
    else:
        return (x * x * a) % c
    
print(func(a,b,c))