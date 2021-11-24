#N가지 종류의 화폐가 있다. 이 화폐들의 개수를 최소한으로 이용해서 그 가치의 합이 M원이 되도록 해야한다.

N, M = map(int,input().split())
_list = []
for i in range(N):
  _list.append(int(input()))

d = [10001] * (M+1)

d[0] = 0

for i in range(N):
  for j in range(_list[i],M+1):
    if d[j-_list[i]] != 10001:
      d[j] = min(d[j],d[j-_list[i]]+1)

if d[M] == 10001:
  print(-1)
else :
  print(d[M])
