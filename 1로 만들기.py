# DP의 가장 기본적인 문제라고 할 수 있다.
# 보텀업을 통해서 최소 값을 구하는 방식 

# 정수 X 입력받기
x = int(input())
d = [0] * 30001

for i in range(2,x+1):
  d[i] = d[i-1] + 1
  if i % 2 == 0:
    d[i] = min(d[i],d[i//2] + 1)
  if i % 3 == 0:
    d[i] = min(d[i],d[i//3] + 1)
  if i % 5 == 0:
    d[i] = min(d[i],d[i//5] + 1)

print(d[x])
  