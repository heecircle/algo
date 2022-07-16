import sys
input = sys.stdin.readline
n=int(input())
elec = [0]*(501)
dp = [1]*(501)

for i in range(n):
  a,b = map(int,input().split())
  elec[a]=b

for i in range(1,501):
  for j in range(0,i):
    if elec[i]==0:
      continue
    if elec[j]<elec[i]:
      dp[i]=max(dp[i],dp[j]+1)

print(n-(max(dp)-1))
#longest increasing sequence 활용 문제,,
