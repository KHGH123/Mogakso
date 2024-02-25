n = int(input())
dp = []
m = [[0]*3 for _ in range(n)]
for i in range(n):
    dp.append([*map(int, input().split())])

m[0] = dp[0]

def func(x, y):
    if m[x][y] != 0:
        return m[x][y]
    if y == 0:
        m[x][y] = min(func(x+1, 1), func(x+1, 2)) + dp[x][y]
    elif y == 1:
        m[x][y] = min(func(x+1, 0), func(x+1, 2)) + dp[x][y]
    elif y == 2:
        m[x][y] = min(func(x+1, 0), func(x+1, 1)) + dp[x][y]
    return m[x][y]

for i in range(1, n):
    m[i][0] = min(m[i-1][1], m[i-1][2]) + dp[i][0]
    m[i][1] = min(m[i-1][0], m[i-1][2]) + dp[i][1]
    m[i][2] = min(m[i-1][0], m[i-1][1]) + dp[i][2]
print(min(m[-1]))
