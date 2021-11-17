# 개미전사
# 0 번째의 값 : EXIST
# 1 번째의 값 : 0번째와 1번째 값을 비교함
# 2 번째의 값 2번쨰 값 = 1번째와, 0번째 값+2번쨰값
# 3 번째의 값 : 바로 그 전의 합 VS 3번째의 값을 포함한 그 전과 전의 값

N = int(input())
K = list(map(int,input().split()))

d = [0] * 1000

d[0] = K[0]
d[1] = max(K[0],K[1])
for i in range(2,N):
  d[i] = max(d[i-1],d[i-2]+K[i])

print(d[N-1])