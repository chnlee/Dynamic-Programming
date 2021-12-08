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