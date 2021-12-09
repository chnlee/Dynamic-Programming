#Knapsack 문제 ( 담을 수 있는 물건이 나누어질 수 없을 때 dp로 푼다)
# 핵심 알고리즘은 물건을 담을 때 
#(현재 물건의 가치 + 현재 가방의 무게 - 현재 물건의 무게에 해당하는 index의 가방의 가치) 와 현재 가방의 무게에 해당하는 이전 물건의 가치를 비교하는 것이다.

N, K = map(int,input().split())

result = [ [0 for _ in range(K+1)] for _ in range(N) ]

for i in range(N):
  weight, value = map(int,input().split())
  
  for idx in range(1,K+1):
    if idx >= weight:
      result[i][idx] = max(result[i-1][idx], result[i-1][idx-weight]+value)
    else:
      result[i][idx] = result[i-1][idx] 

print(max(result[-1]))
