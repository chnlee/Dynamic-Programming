# # 내 풀이
# N, M = map(int,input().split())
# d = [list(map(int,input().split())) for _ in range(N)]

# for i in range(N):
#   for j in range(M):
#     if i == 0 and j > 0:
#       d[i][j] += d[i][j-1]
#     if j == 0 and i > 0:
#       d[i][j] += d[i-1][j]
#     if i > 0 and j > 0:
#       d[i][j] = max(d[i][j] + d[i][j-1], d[i][j] + d[i-1][j])

# print(d[N-1][M-1])

# 답지 풀이(d를 따로 만들어서 구하는 방법)

N, M = map(int,input().split())

maze = [list(map(int,input().split())) for _ in range(N)]

d = [[0] * (M+1) for _ in range(N+1)]

for i in range(1,N+1):
  for j in range(1,M+1):
    d[i][j] = maze[i-1][j-1] + max(d[i-1][j],d[i-1][j-1],d[i][j-1])

print(d[N][M])
