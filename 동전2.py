n, k = map(int,input().split())
_list = []
for i in range(n):
  _list.append(int(input()))
d = [100001] * (k+1)

d[0] = 0

for i in range(n):
  for j in range(_list[i],k+1):
    if d[j-_list[i]] != 100001:
      d[j] = min(d[j],d[j-_list[i]]+1)

if d[k] == 100001:
  print(-1)
else:
  print(d[k])
