input()
n = list(map(int, input().split()))
nn = [a/max(n)*100 for a in n]
print(sum(nn) / len(nn))