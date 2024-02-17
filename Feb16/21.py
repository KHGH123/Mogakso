p1 = ['BWBWBWBW','WBWBWBWB']*4
p2 = ['WBWBWBWB','BWBWBWBW']*4

ans = float("inf")
n, m = map(int, input().split())
str = []
for r in range(n):
    str.append(input())

for i in range(n-7):
    for j in range(m-7):
        aa=0
        bb=0
        for k in range(8):
            for x in range(8):
                if str[i+k][j+x] != p1[k][x]:
                    aa += 1
                if str[i+k][j+x] != p2[k][x]:
                    bb += 1
        ans = min(ans, aa, bb)

print(ans)
                