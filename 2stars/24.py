N, K = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

diff_sum = sum(abs(A[i] - B[i]) for i in range(N))

print("Yes" if K >= diff_sum and diff_sum%2 == K%2 else "No")