n=int(input())
k = {}
k[1] = 0

def dp(n, d):
    if d>100 : return float("inf")
    if n in k.keys(): return k[n]
    x = float("inf")
    y = float("inf")
    z = float("inf")
        
    if n%3 == 0:
        x = dp(n//3, d+1)

    if n%2 == 0:
        y = dp(n//2, d+1)
    
    z = dp(n-1, d+1)

    k[n] = min(x, y, z)+1
    return k[n]

dp(n, 0)
print(k[n])