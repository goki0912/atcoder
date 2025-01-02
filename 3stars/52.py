# 因数分解してみる

N = int(input())
A = [list(map(int, input().split())) for _ in range(N)]
result = 1

for i in range(N):
  d_sum = sum(A[i])
  result = (d_sum * result) % (10**9 +7)

print(result)