H, W = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(H)]

row_sums = [sum(row) for row in A]
col_sums = [sum(A[i][j] for i in range(H)) for j in range(W)]

B = []
for i in range(H):
  for j in range(W):
    B[i][j] = row_sums[i] + col_sums[j] - A[i][j]

print(B)


# col_sums = [0] * W  # 各列の合計を格納するリストを初期化
# for j in range(W):  # 列ごとに
#     for i in range(H):  # 各行の値を足す
#         col_sums[j] += A[i][j]  # 列ごとに合計を計算

