n = int(input())

dp = [0]*9999
dp[1], dp[2], dp[3]= 1, 2, 4
for i in range(4, 9999):
    dp[i]+=dp[i-1]
    dp[i]+=dp[i-2]
    dp[i]+=dp[i-3]

for j in range(n):
    print(dp[int(input)])


        
