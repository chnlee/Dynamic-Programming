n, k = map(int,input().split())
_list = []
for i in range(n):
  _list.append(int(input()))
d = [0] * (k+1)
# # 풀이 1번
# d[0] = 0

# for i in _list:
#   for j in range(1,k+1):
#     if j == i:
#       d[j] += 1
#     if j > i:
#       d[j] += d[j-i]

# print(d[n])
# 풀이 2번
# d[0]을 0을 만드는 개수가 아닌 n가지 종류의 동전을 1개만 사용했을 때의 경우의 수이다.
# 풀이 2번

d[0] = 1

for i in _list:
  for j in range(i,k+1):
    if j>=i:
      d[j] += d[j-i]
    
print(d[k])
