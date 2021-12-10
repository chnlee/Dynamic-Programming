#LCS(Longest Common Sequence)
# 가장 긴 공통 부분 문자 수열 또는 최장 공통 문자 수열을 의미함
# LCS 테이블을 어떻게 작성할 수 있는지를 아는 것이 이 문제의 핵심
# 같은 문자인 경우 : 결국 같은 문자를 만나면 대각선의 수에서 +1, 같은게 없는 경우: 전의 오른쪽의 리스트 값과 위쪽의 리스트 값을 비교해서 더 큰 값을 설정
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
