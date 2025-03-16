N, K = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

diff_sum = 0
for i in range(N):
    diff_sum+= A[i] - B[i]

if diff_sum%2 == K%2:
    print("Yes")
else:
    print("No")
