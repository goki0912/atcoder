H, W = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(H)]

row_sums = [sum(row) for row in A]
col_sums = [sum(A[i][j] for i in range(H)) for j in range(W)]

B = [[row_sums[i] + col_sums[j] - A[i][j]  for j in range(W)] for i in range(H)]
for i in range(H):
  for j in range(W):
    B[i][j] = row_sums[i] + col_sums[j] - A[i][j]

for i in B:
  print(*i)