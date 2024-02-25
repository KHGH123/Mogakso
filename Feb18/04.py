def make_one(n):
    dp = [0] * (n + 1) # 연산 횟수를 저장하는 DP 테이블
    
    for i in range(2, n + 1):
        # 1을 뺀 경우와 2로 나누어 떨어지는 경우를 비교하여 최솟값을 저장
        dp[i] = dp[i - 1] + 1
        if i % 2 == 0:
            dp[i] = min(dp[i], dp[i // 2] + 1)
        # 3으로 나누어 떨어지는 경우를 비교하여 최솟값을 저장
        if i % 3 == 0:
            dp[i] = min(dp[i], dp[i // 3] + 1)
    
    return dp[n]

# 입력 받기
n = int(input())

# 함수 호출 및 결과 출력
print(make_one(n))