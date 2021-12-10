# ACAYKP
# CAPCAK
import sys
sys.setrecursionlimit(3000)

string1 = sys.stdin.readline().strip()
string2 = sys.stdin.readline().strip()
a = len(string1)
b = len(string2)
result = [[0 for _ in range(b+1)] for _ in range(a+1)]

for i in range(1, a+1):
  for j in range(1, b+1):
    if string1[i-1] == string2[j-1]:
      result[i][j] = result[i-1][j-1]+1
    else:
      result[i][j] = max(result[i-1][j], result[i][j-1])
    
print(result[-1][-1])